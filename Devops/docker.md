# Complete Docker Learning Guide

## Table of Contents
1. [What is Docker?](#what-is-docker)
2. [Core Concepts](#core-concepts)
3. [Installation](#installation)
4. [Basic Commands](#basic-commands)
5. [Docker Images](#docker-images)
6. [Docker Containers](#docker-containers)
7. [Dockerfile](#dockerfile)
8. [Docker Compose](#docker-compose)
9. [Volumes and Storage](#volumes-and-storage)
10. [Networking](#networking)
11. [Multi-stage Builds](#multi-stage-builds)
12. [Best Practices](#best-practices)
13. [Troubleshooting](#troubleshooting)
14. [Advanced Topics](#advanced-topics)

---

## What is Docker?

Docker is a containerization platform that packages applications and their dependencies into lightweight, portable containers. It solves the "it works on my machine" problem by ensuring consistent environments across development, testing, and production.

- Docker is a **runtime environment** that manages containers.
- Containers offer **isolation**, not full virtualization.
- Containers are **OS-level virtualization**; VMs are **hardware-level virtualization**.
- Containers share the **host OS kernel** — no separate OS per application.
- VMs need their own OS; containers use the host OS for compute resources.

### Docker vs Virtual Machines
| Docker Containers | Virtual Machines |
|------------------|------------------|
| Share host OS kernel | Each has own OS |
| OS-level virtualization | Hardware-level virtualization |
| Lightweight (MBs) | Heavy (GBs) |
| Fast startup | Slow startup |
| Better resource utilization | More resource overhead |

---

## Core Concepts

### Docker Architecture
```
Docker → Desktop | Client | Host | Daemon | Registry
```
- **Desktop** — GUI app for managing Docker locally
- **Client** — CLI that sends commands to the Daemon
- **Host** — machine running the Docker Daemon
- **Daemon** — background service managing containers/images
- **Registry** — stores and distributes images (e.g. Docker Hub)

### 1. Images
- Read-only templates used to create containers
- Built in layers using union file system; each instruction creates a layer
- Immutable once created
- Called **repositories** on Docker Hub
- Containers run *from* images

### 2. Containers
- Running instances of images
- Mutable during runtime; data is lost when deleted (use volumes to persist)
- Isolated — own filesystem, network, and process space

### 3. Dockerfile
- Text file with instructions to build an image
- Declarative; each instruction is cached as a layer

### 4. Registry
- Storage and distribution system for images
- **Docker Hub** — default public registry
- Private registries for internal use

### 5. Docker Compose
- Tool for defining and running multi-container applications via a YAML file

---

## Installation

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update && sudo apt install docker-ce

# Add user to docker group (avoids needing sudo)
sudo usermod -aG docker ubuntu   # replace 'ubuntu' with your username
```

### macOS
```bash
brew install --cask docker
# Or download Docker Desktop from docker.com
```

### Windows
Download Docker Desktop from the official website.

### Verify
```bash
docker --version
docker run hello-world
```

---

## Basic Commands

```bash
# System info
docker info
docker system df

# Images
docker images / docker image ls
docker pull nginx
docker pull nginx:1.21
docker rmi nginx
docker build -t myapp .
docker tag myapp:latest myapp:v1.0
docker push myapp:v1.0

# Containers
docker run nginx
docker run -d nginx                    # detached
docker run -p 8080:80 nginx           # port mapping
docker run --name webserver nginx
docker run -it ubuntu bash            # interactive terminal

docker ps                              # running containers
docker ps -a                          # all containers
docker stop / start / restart <id>
docker rm <id>
docker rm -f <id>                     # force remove

# Interact with running container
docker exec -it <id> bash            # login/interact with container
docker logs -f <id>
docker inspect <id>                   # gives metadata about container
docker stats <id>
docker top <id>

# Cleanup
docker volume prune                   # remove unused volumes
docker system prune                   # remove all unused resources
docker system prune -a                # includes unused images
```

---

## Docker Images

```bash
docker history nginx          # inspect layers
docker save -o nginx.tar nginx
docker load -i nginx.tar
```

### Naming Convention
```
[registry]/[username]/[repository]:[tag]
nginx                          # official image
nginx:1.21                     # specific version
myregistry.com/myapp:v1.0     # private registry
```

---

## Docker Containers

### Lifecycle
`Created → Running → Paused → Stopped → Deleted`

### Useful Run Options
```bash
docker run -e ENV_VAR=value nginx
docker run --env-file .env nginx
docker run -v /host/path:/container/path nginx
docker run --network mynetwork nginx
docker run --memory 512m --cpus 0.5 nginx
docker run --restart always nginx
docker run --read-only nginx
```

---

## Dockerfile

### Basic Structure
```dockerfile
FROM node:16-alpine
LABEL maintainer="you@example.com"

ENV APP_HOME=/app NODE_ENV=production
WORKDIR $APP_HOME

COPY package*.json ./
RUN npm ci --only=production

COPY . .
EXPOSE 3000
CMD ["node", "src/index.js"]
```

### Key Instructions

| Instruction | Purpose |
|---|---|
| `FROM` | Base image |
| `RUN` | Execute command during build |
| `COPY` | Copy files (preferred over ADD) |
| `ADD` | Like COPY but also handles URLs and tar extraction |
| `WORKDIR` | Set working directory |
| `ENV` | Set environment variables |
| `EXPOSE` | Document port usage |
| `ARG` | Build-time variable (can be overridden with `--build-arg`) |
| `VOLUME` | Create mount point |
| `USER` | Switch user |
| `HEALTHCHECK` | Define container health check |

### CMD vs ENTRYPOINT

```dockerfile
# CMD — default command, fully overridden by user args
CMD ["node", "app.js"]

# ENTRYPOINT — always executed; cannot be overridden easily
ENTRYPOINT ["node"]
CMD ["app.js"]          # CMD becomes default argument to ENTRYPOINT
```

**Key rules:**
- When both are used, **ENTRYPOINT** is the executable and **CMD** provides default arguments.
- If the user passes arguments at `docker run`, they **overwrite CMD** but not ENTRYPOINT.
- If ENTRYPOINT is set with no CMD, the user **must** pass arguments.

```dockerfile
# Example
ENTRYPOINT ["node"]
CMD ["app.js"]
# docker run myimage          → runs: node app.js
# docker run myimage server.js → runs: node server.js  (CMD overwritten)
```

### .dockerignore
```
node_modules
.git
.env
*.md
tests/
coverage/
```

### Build Commands
```bash
docker build -t myapp .
docker build -t myapp:v1.0 --build-arg NODE_VERSION=16 .
docker build -f Dockerfile.dev -t myapp:dev .
docker build --target development -t myapp:dev .   # specific stage
```

---

## Docker Compose

### Basic docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    depends_on:
      - db
    volumes:
      - ./src:/app/src
    networks:
      - app-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app-network

volumes:
  postgres_data:

networks:
  app-network:
    driver: bridge
```

### Compose Commands
```bash
docker-compose up -d
docker-compose up --build
docker-compose down
docker-compose down -v          # also remove volumes
docker-compose logs -f web
docker-compose exec web bash
docker-compose ps
docker-compose up --scale web=3
```

---

## Volumes and Storage

There are **2 main ways** to persist container data: **volumes** and **bind mounts**.

### Volume Types

| Type | Command | Notes |
|---|---|---|
| **Named volume** | `docker run -v myvolume:/data` | Managed by Docker; stored at `/var/lib/docker/volumes` |
| **Bind mount** | `docker run -v /host/path:/container/path` | Injects data from host machine into container |
| **Anonymous volume** | `docker run -v /data` | No name; managed by Docker |
| **tmpfs** | `docker run --tmpfs /tmp` | Stored in RAM only; lost on stop |

```bash
docker volume create myvolume
docker volume ls
docker volume inspect myvolume
docker volume rm myvolume
docker volume prune
```

### Backup & Restore
```bash
# Backup
docker run --rm -v myvolume:/data -v $(pwd):/backup alpine \
  tar czf /backup/backup.tar.gz -C /data .

# Restore
docker run --rm -v myvolume:/data -v $(pwd):/backup alpine \
  tar xzf /backup/backup.tar.gz -C /data
```

---

## Networking

### Network Types

| Type | Description |
|---|---|
| **Bridge** (default) | Container communicates internally; port mapping required for external access |
| **Host** | Shares host network stack; no container-level isolation |
| **None** | No network access |
| **Overlay** | Communication between containers across multiple hosts (Swarm) |
| **Macvlan** | Assigns MAC address; container appears as a physical device on the network |
| **User-defined bridge** | Containers communicate using **names** instead of IP addresses — best practice for custom setups |

### Commands
```bash
docker network ls
docker network create mynetwork
docker network inspect mynetwork
docker network connect mynetwork container_name
docker network disconnect mynetwork container_name
docker network rm mynetwork
```

### Port Mapping
```bash
docker run -p 8080:80 nginx          # host:container
docker run -p 8080:80 -p 8443:443 nginx
docker run -p 127.0.0.1:8080:80 nginx
docker run -P nginx                  # random host port
```

### Service Discovery
Containers on the same network can reach each other by **container name** (bridge) or **service name** (Compose).

```bash
docker network create app-network
docker run -d --name db --network app-network postgres
docker run --name app --network app-network myapp  # connects to 'db' by hostname
```

---

## Multi-stage Builds

Reduces final image size by only copying what's needed into the production stage.

```dockerfile
# Build stage
FROM node:16 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:16-alpine AS production
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

**Benefits:** Smaller images, fewer attack vectors, better caching, flexible per-environment stages.

---

## Best Practices

### Dockerfile
- Use official, versioned base images (`node:16.17.0-alpine3.16` not `node:latest`)
- Combine RUN commands to reduce layers; clean up in the same layer
- Copy `package.json` first, run install, then copy source — maximizes cache reuse
- Use non-root user in production
- Always use `.dockerignore`
- Use multi-stage builds for production

### Security
```bash
docker scout cves myimage          # scan for vulnerabilities
docker run --read-only --tmpfs /tmp myapp
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myapp
docker run --memory 512m --cpus 0.5 myapp
```

### Health Checks
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:3000/ || exit 1
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Container exits immediately | `docker logs <id>`, run with `-it` for interactive debug |
| Permission denied | `RUN chown -R node:node /app` + `USER node` |
| Port already in use | `lsof -i :8080`, use a different host port |
| Out of disk space | `docker system prune -a`, `docker volume prune` |
| Build context too large | Add `node_modules` etc. to `.dockerignore` |

```bash
docker inspect <id>             # full metadata
docker exec -it <id> /bin/bash  # shell into container
docker diff <id>                # filesystem changes
docker stats <id>               # resource usage

# Health check status
docker inspect --format='{{.State.Health.Status}}' <id>
```

---

## Advanced Topics

### Docker Swarm
```bash
docker swarm init
docker stack deploy -c docker-compose.yml mystack
docker service scale mystack_web=3
```

### BuildKit (Faster Builds)
```dockerfile
# syntax=docker/dockerfile:1
RUN --mount=type=cache,target=/root/.npm npm install
```

### Logging Drivers
```bash
docker run --log-driver json-file myapp     # default
docker run --log-driver syslog myapp
```

### Resource Constraints
```bash
docker run --memory=512m --cpus=0.5 myapp
```

### Registry Operations
```bash
docker login myregistry.com
docker tag myapp myregistry.com/myapp:v1.0
docker push myregistry.com/myapp:v1.0
docker pull myregistry.com/myapp:v1.0
```

---

## Key Takeaways

- Start with simple containers and gradually learn advanced features
- Use multi-stage builds for production
- Use named volumes for production data; bind mounts for development
- Use user-defined bridge networks so containers talk by name
- Keep images small, versioned, and scanned for vulnerabilities
- Monitor containers with `docker stats`, `docker logs`, and health checks

### Next Steps
1. Practice with real applications
2. Learn Kubernetes for orchestration
3. Explore CI/CD integration
4. Study security hardening

### Resources
- [Docker Docs](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Compose File Reference](https://docs.docker.com/compose/compose-file/)