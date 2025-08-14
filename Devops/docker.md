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
13. [Common Use Cases](#common-use-cases)
14. [Troubleshooting](#troubleshooting)
15. [Advanced Topics](#advanced-topics)

---

## What is Docker?

Docker is a containerization platform that packages applications and their dependencies into lightweight, portable containers. It solves the "it works on my machine" problem by ensuring consistent environments across development, testing, and production.

### Key Benefits
- **Portability**: Run anywhere Docker is installed
- **Consistency**: Same environment across all stages
- **Efficiency**: Lightweight compared to virtual machines
- **Scalability**: Easy to scale applications
- **Isolation**: Applications don't interfere with each other

### Docker vs Virtual Machines
| Docker Containers | Virtual Machines |
|------------------|------------------|
| Share host OS kernel | Each has own OS |
| Lightweight (MBs) | Heavy (GBs) |
| Fast startup | Slow startup |
| Better resource utilization | More resource overhead |

---

## Core Concepts

### 1. Images
- **Definition**: Read-only templates used to create containers
- **Layers**: Built in layers using union file system
- **Immutable**: Cannot be changed once created
- **Base Images**: Starting point (e.g., ubuntu, alpine, node)

### 2. Containers
- **Definition**: Running instances of images
- **Mutable**: Can be modified during runtime
- **Ephemeral**: Data is lost when container is deleted
- **Isolated**: Own filesystem, network, and process space

### 3. Dockerfile
- **Definition**: Text file with instructions to build images
- **Declarative**: Describes desired state
- **Cached**: Each instruction creates a layer

### 4. Registry
- **Definition**: Storage and distribution system for images
- **Docker Hub**: Default public registry
- **Private Registries**: For internal use

---

## Installation

### Linux (Ubuntu/Debian)
```bash
# Update package index
sudo apt update

# Install prerequisites
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Add Docker GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add Docker repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Install Docker
sudo apt update
sudo apt install docker-ce

# Add user to docker group (optional)
sudo usermod -aG docker $USER
```

### macOS
```bash
# Using Homebrew
brew install --cask docker

# Or download Docker Desktop from docker.com
```

### Windows
Download Docker Desktop from the official website and follow the installation wizard.

### Verify Installation
```bash
docker --version
docker run hello-world
```

---

## Basic Commands

### Information Commands
```bash
# Docker version
docker --version
docker version

# System information
docker info
docker system df

# Help
docker --help
docker <command> --help
```

### Image Commands
```bash
# List images
docker images
docker image ls

# Search images
docker search nginx

# Pull image
docker pull nginx
docker pull nginx:1.21

# Remove image
docker rmi nginx
docker image rm nginx

# Build image
docker build -t myapp .
docker build -t myapp:v1.0 .

# Tag image
docker tag myapp:latest myapp:v1.0

# Push image
docker push myapp:v1.0
```

### Container Commands
```bash
# Run container
docker run nginx
docker run -d nginx                    # detached mode
docker run -p 8080:80 nginx           # port mapping
docker run --name webserver nginx     # custom name
docker run -it ubuntu bash            # interactive terminal

# List containers
docker ps                              # running containers
docker ps -a                          # all containers

# Stop container
docker stop <container-id>
docker stop webserver

# Start stopped container
docker start <container-id>

# Restart container
docker restart <container-id>

# Remove container
docker rm <container-id>
docker rm -f <container-id>           # force remove

# Execute command in running container
docker exec -it <container-id> bash
docker exec webserver ls /var/log

# View logs
docker logs <container-id>
docker logs -f <container-id>         # follow logs

# Inspect container
docker inspect <container-id>

# Copy files
docker cp file.txt <container-id>:/path/
docker cp <container-id>:/path/file.txt ./
```

---

## Docker Images

### Understanding Images
Images are built in layers, where each layer represents a set of file changes. This layered approach enables:
- **Caching**: Unchanged layers are reused
- **Efficiency**: Multiple images can share layers
- **Version Control**: Easy to track changes

### Image Naming Convention
```
[registry]/[username]/[repository]:[tag]

Examples:
nginx                           # Official nginx image
nginx:1.21                      # Specific version
docker.io/nginx:latest          # Full name
myregistry.com/myapp:v1.0      # Private registry
```

### Working with Images
```bash
# Inspect image layers
docker history nginx

# Save image to file
docker save nginx > nginx.tar
docker save -o nginx.tar nginx

# Load image from file
docker load < nginx.tar
docker load -i nginx.tar

# Export container as image
docker export <container-id> > container.tar

# Import container
docker import container.tar myimage:latest
```

---

## Docker Containers

### Container Lifecycle
1. **Created**: Container exists but not started
2. **Running**: Container is executing
3. **Paused**: Container processes are paused
4. **Stopped**: Container has exited
5. **Deleted**: Container is removed

### Container Options
```bash
# Environment variables
docker run -e ENV_VAR=value nginx
docker run --env-file .env nginx

# Volume mounting
docker run -v /host/path:/container/path nginx
docker run -v myvolume:/data nginx

# Network
docker run --network mynetwork nginx
docker run --network host nginx

# Resource limits
docker run --memory 512m nginx
docker run --cpus 0.5 nginx

# Restart policy
docker run --restart always nginx
docker run --restart unless-stopped nginx

# Security
docker run --user 1000:1000 nginx
docker run --read-only nginx
```

### Container Monitoring
```bash
# Resource usage
docker stats
docker stats <container-id>

# Process list
docker top <container-id>

# Port mapping
docker port <container-id>

# Container diff
docker diff <container-id>
```

---

## Dockerfile

A Dockerfile is a text file containing instructions to build a Docker image.

### Basic Structure
```dockerfile
# Use base image
FROM ubuntu:20.04

# Set metadata
LABEL maintainer="your-email@example.com"
LABEL version="1.0"

# Set environment variables
ENV APP_HOME=/app
ENV NODE_ENV=production

# Set working directory
WORKDIR $APP_HOME

# Copy files
COPY package.json .
COPY src/ ./src/

# Run commands
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    rm -rf /var/lib/apt/lists/*

RUN npm install --only=production

# Expose port
EXPOSE 3000

# Set default command
CMD ["node", "src/index.js"]
```

### Dockerfile Instructions

#### FROM
```dockerfile
# Base image
FROM node:14-alpine

# Multi-stage build
FROM node:14 AS builder
FROM nginx:alpine AS runtime
```

#### RUN
```dockerfile
# Install packages
RUN apt-get update && apt-get install -y git

# Multiple commands
RUN apt-get update && \
    apt-get install -y \
        git \
        curl \
        vim && \
    rm -rf /var/lib/apt/lists/*
```

#### COPY vs ADD
```dockerfile
# COPY (preferred)
COPY src/ /app/src/
COPY package*.json ./

# ADD (has additional features)
ADD https://example.com/file.tar.gz /tmp/
ADD archive.tar.gz /app/
```

#### WORKDIR
```dockerfile
# Set working directory
WORKDIR /app

# Equivalent to RUN cd /app
```

#### ENV
```dockerfile
# Set environment variables
ENV NODE_ENV=production
ENV API_URL=https://api.example.com
ENV DEBUG=false
```

#### EXPOSE
```dockerfile
# Document port usage
EXPOSE 3000
EXPOSE 8080/tcp
EXPOSE 53/udp
```

#### CMD vs ENTRYPOINT
```dockerfile
# CMD - can be overridden
CMD ["node", "app.js"]
CMD node app.js

# ENTRYPOINT - always executed
ENTRYPOINT ["node"]
CMD ["app.js"]

# Combined usage
ENTRYPOINT ["node", "app.js"]
```

#### USER
```dockerfile
# Switch user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
USER nextjs
```

#### VOLUME
```dockerfile
# Create volume mount point
VOLUME ["/data"]
VOLUME /var/log /var/db
```

#### ARG
```dockerfile
# Build-time variables
ARG NODE_VERSION=14
FROM node:${NODE_VERSION}-alpine

# Can be overridden during build
# docker build --build-arg NODE_VERSION=16 .
```

### Build Context and .dockerignore
Create `.dockerignore` to exclude files:
```
node_modules
npm-debug.log
.git
.gitignore
README.md
.env
.nyc_output
coverage
.cache
```

### Building Images
```bash
# Basic build
docker build -t myapp .

# Build with tag
docker build -t myapp:v1.0 .

# Build with build args
docker build --build-arg NODE_VERSION=16 -t myapp .

# Build from different Dockerfile
docker build -f Dockerfile.dev -t myapp:dev .

# Build with specific context
docker build -t myapp ./context/
```

---

## Docker Compose

Docker Compose is a tool for defining and running multi-container applications.

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

### Service Configuration

#### Build Context
```yaml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile.dev
      args:
        - NODE_VERSION=16
```

#### Environment Variables
```yaml
services:
  web:
    environment:
      - DEBUG=true
      - API_URL=https://api.example.com
    env_file:
      - .env
      - .env.local
```

#### Volumes
```yaml
services:
  web:
    volumes:
      # Bind mount
      - ./src:/app/src
      # Named volume
      - node_modules:/app/node_modules
      # Anonymous volume
      - /app/temp
```

#### Networks
```yaml
services:
  web:
    networks:
      - frontend
      - backend

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true
```

#### Dependencies
```yaml
services:
  web:
    depends_on:
      - db
      - redis
    
  # With health checks
  web:
    depends_on:
      db:
        condition: service_healthy
```

#### Health Checks
```yaml
services:
  web:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

#### Resource Limits
```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

### Docker Compose Commands
```bash
# Start services
docker-compose up
docker-compose up -d                   # detached mode
docker-compose up --build             # rebuild images

# Stop services
docker-compose down
docker-compose down -v                 # remove volumes
docker-compose down --rmi all          # remove images

# View logs
docker-compose logs
docker-compose logs web               # specific service
docker-compose logs -f                # follow logs

# Scale services
docker-compose up --scale web=3

# Execute commands
docker-compose exec web bash
docker-compose run web npm test

# View status
docker-compose ps
docker-compose top
```

### Environment Files
Create `.env` file:
```env
NODE_ENV=production
DATABASE_URL=postgres://user:pass@db:5432/myapp
REDIS_URL=redis://redis:6379
API_KEY=your-secret-key
```

Reference in compose file:
```yaml
services:
  web:
    environment:
      - NODE_ENV=${NODE_ENV}
      - DATABASE_URL=${DATABASE_URL}
```

---

## Volumes and Storage

Docker provides several options for persisting data.

### Volume Types

#### 1. Anonymous Volumes
```bash
docker run -v /data nginx
```

#### 2. Named Volumes
```bash
# Create volume
docker volume create myvolume

# Use volume
docker run -v myvolume:/data nginx

# List volumes
docker volume ls

# Inspect volume
docker volume inspect myvolume

# Remove volume
docker volume rm myvolume
```

#### 3. Bind Mounts
```bash
# Absolute path
docker run -v /host/path:/container/path nginx

# Relative path
docker run -v $(pwd):/app nginx

# Read-only
docker run -v /host/path:/container/path:ro nginx
```

#### 4. tmpfs Mounts
```bash
# Temporary filesystem in memory
docker run --tmpfs /tmp nginx
docker run --mount type=tmpfs,destination=/tmp nginx
```

### Volume Commands
```bash
# Create volume
docker volume create --driver local \
  --opt type=tmpfs \
  --opt device=tmpfs \
  --opt o=size=100m,uid=1000 \
  myvolume

# Backup volume
docker run --rm -v myvolume:/data -v $(pwd):/backup alpine \
  tar czf /backup/backup.tar.gz -C /data .

# Restore volume
docker run --rm -v myvolume:/data -v $(pwd):/backup alpine \
  tar xzf /backup/backup.tar.gz -C /data --strip 1

# Copy data between volumes
docker run --rm -v oldvolume:/from -v newvolume:/to alpine \
  ash -c "cd /from ; cp -av . /to"
```

### Best Practices for Volumes
- Use named volumes for production data
- Use bind mounts for development
- Backup important data regularly
- Use volume drivers for network storage
- Consider using tmpfs for temporary data

---

## Networking

Docker provides several networking options for containers.

### Network Types

#### 1. Bridge Network (Default)
```bash
# Create custom bridge network
docker network create mynetwork

# Run container with custom network
docker run --network mynetwork nginx

# Connect running container to network
docker network connect mynetwork container_name
```

#### 2. Host Network
```bash
# Use host network stack
docker run --network host nginx
```

#### 3. None Network
```bash
# No network access
docker run --network none nginx
```

#### 4. Container Network
```bash
# Share network with another container
docker run --network container:other_container nginx
```

### Network Commands
```bash
# List networks
docker network ls

# Inspect network
docker network inspect bridge

# Create network
docker network create --driver bridge mynetwork

# Remove network
docker network rm mynetwork

# Connect container to network
docker network connect mynetwork container_name

# Disconnect container from network
docker network disconnect mynetwork container_name
```

### Port Mapping
```bash
# Map single port
docker run -p 8080:80 nginx

# Map multiple ports
docker run -p 8080:80 -p 8443:443 nginx

# Map to specific interface
docker run -p 127.0.0.1:8080:80 nginx

# Map random port
docker run -P nginx

# UDP ports
docker run -p 53:53/udp nginx
```

### Service Discovery
Containers can communicate using:
- Container names (within same network)
- Service names (in Docker Compose)
- IP addresses
- External DNS

Example:
```bash
# Create network
docker network create app-network

# Run database
docker run -d --name db --network app-network postgres

# Run app (can connect to 'db' hostname)
docker run --name app --network app-network myapp
```

---

## Multi-stage Builds

Multi-stage builds allow you to use multiple FROM statements in a Dockerfile to create smaller, more secure production images.

### Basic Multi-stage Build
```dockerfile
# Build stage
FROM node:16 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

# Production stage
FROM node:16-alpine AS production
WORKDIR /app

# Copy only production dependencies
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./

EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Advanced Multi-stage Example
```dockerfile
# Base stage with common dependencies
FROM node:16 AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci

# Development stage
FROM base AS development
ENV NODE_ENV=development
RUN npm ci --include=dev
COPY . .
CMD ["npm", "run", "dev"]

# Build stage
FROM base AS build
COPY . .
RUN npm run build
RUN npm prune --omit=dev

# Test stage
FROM build AS test
ENV NODE_ENV=test
RUN npm ci --include=dev
RUN npm test

# Production stage
FROM node:16-alpine AS production
ENV NODE_ENV=production
WORKDIR /app

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

# Copy built application
COPY --from=build --chown=nextjs:nodejs /app/dist ./dist
COPY --from=build --chown=nextjs:nodejs /app/node_modules ./node_modules
COPY --from=build --chown=nextjs:nodejs /app/package.json ./package.json

USER nextjs
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Building Specific Stages
```bash
# Build development stage
docker build --target development -t myapp:dev .

# Build production stage (default)
docker build -t myapp:prod .

# Build test stage
docker build --target test -t myapp:test .
```

### Benefits of Multi-stage Builds
- **Smaller images**: Only production dependencies included
- **Security**: Fewer attack vectors in production image
- **Flexibility**: Different stages for different environments
- **Caching**: Better layer caching strategies

---

## Best Practices

### Dockerfile Best Practices

#### 1. Use Official Base Images
```dockerfile
# Good
FROM node:16-alpine

# Avoid
FROM ubuntu
RUN apt-get update && apt-get install -y nodejs
```

#### 2. Minimize Layers
```dockerfile
# Good
RUN apt-get update && \
    apt-get install -y git curl && \
    rm -rf /var/lib/apt/lists/*

# Avoid
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y curl
```

#### 3. Leverage Build Cache
```dockerfile
# Copy package files first
COPY package*.json ./
RUN npm install

# Copy source code later
COPY . .
```

#### 4. Use Non-root User
```dockerfile
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
USER nextjs
```

#### 5. Use .dockerignore
```
node_modules
.git
.env
*.md
tests/
```

#### 6. Multi-stage for Production
```dockerfile
FROM node:16 AS builder
# Build steps

FROM node:16-alpine AS production
COPY --from=builder /app/dist ./dist
```

### Security Best Practices

#### 1. Scan Images for Vulnerabilities
```bash
# Using Docker Scout
docker scout quickview
docker scout cves myimage

# Using Trivy
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy image myimage
```

#### 2. Use Specific Tags
```dockerfile
# Good
FROM node:16.17.0-alpine3.16

# Avoid
FROM node:latest
```

#### 3. Read-only Root Filesystem
```bash
docker run --read-only --tmpfs /tmp myapp
```

#### 4. Resource Limits
```bash
docker run --memory 512m --cpus 0.5 myapp
```

#### 5. Drop Capabilities
```bash
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myapp
```

### Performance Best Practices

#### 1. Use Alpine Images
```dockerfile
FROM node:16-alpine
```

#### 2. Minimize Image Layers
```dockerfile
RUN apt-get update && \
    apt-get install -y package1 package2 && \
    rm -rf /var/lib/apt/lists/*
```

#### 3. Use Build Cache
```dockerfile
# Dependencies first
COPY package.json .
RUN npm install

# Source code second
COPY . .
```

#### 4. Health Checks
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/ || exit 1
```

---

## Common Use Cases

### 1. Web Application (Node.js)
```dockerfile
FROM node:16-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm ci --only=production

# Copy source code
COPY . .

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
USER nextjs

EXPOSE 3000

CMD ["node", "index.js"]
```

### 2. Database (PostgreSQL)
```yaml
version: '3.8'
services:
  db:
    image: postgres:14
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

### 3. Microservices Architecture
```yaml
version: '3.8'
services:
  api-gateway:
    build: ./api-gateway
    ports:
      - "80:80"
    depends_on:
      - user-service
      - product-service

  user-service:
    build: ./user-service
    environment:
      - DATABASE_URL=postgres://user:pass@user-db:5432/users

  product-service:
    build: ./product-service
    environment:
      - DATABASE_URL=postgres://user:pass@product-db:5432/products

  user-db:
    image: postgres:14
    environment:
      POSTGRES_DB: users
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass

  product-db:
    image: postgres:14
    environment:
      POSTGRES_DB: products
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
```

### 4. Development Environment
```yaml
version: '3.8'
services:
  app:
    build:
      context: .
      target: development
    volumes:
      - .:/app
      - /app/node_modules
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
    command: npm run dev

  db:
    image: postgres:14
    environment:
      POSTGRES_DB: myapp_dev
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: dev
    ports:
      - "5432:5432"
```

### 5. CI/CD Pipeline
```dockerfile
# Multi-stage build for CI/CD
FROM node:16 AS dependencies
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM dependencies AS test
COPY . .
RUN npm test

FROM dependencies AS build
COPY . .
RUN npm run build

FROM node:16-alpine AS production
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
COPY package.json ./
CMD ["node", "dist/index.js"]
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Container Exits Immediately
```bash
# Check exit code
docker ps -a

# View logs
docker logs <container-id>

# Run interactively
docker run -it myimage sh
```

#### 2. Permission Denied
```bash
# Check file permissions
ls -la

# Fix with proper user
RUN chown -R node:node /app
USER node
```

#### 3. Port Already in Use
```bash
# Find process using port
lsof -i :8080
netstat -tulpn | grep :8080

# Use different port
docker run -p 8081:80 nginx
```

#### 4. Out of Disk Space
```bash
# Clean up
docker system prune -a

# Remove unused volumes
docker volume prune

# Remove unused networks
docker network prune
```

#### 5. Build Context Too Large
```bash
# Use .dockerignore
echo "node_modules" > .dockerignore

# Check build context size
docker build --no-cache .
```

### Debugging Commands
```bash
# Inspect container
docker inspect <container-id>

# View container processes
docker top <container-id>

# Execute shell in container
docker exec -it <container-id> /bin/bash

# View container filesystem changes
docker diff <container-id>

# Export container filesystem
docker export <container-id> > container.tar

# View resource usage
docker stats <container-id>
```

### Health Check Debugging
```bash
# View health status
docker inspect --format='{{.State.Health.Status}}' <container-id>

# View health check logs
docker inspect --format='{{range .State.Health.Log}}{{.Output}}{{end}}' <container-id>
```

---

## Advanced Topics

### 1. Docker Swarm Mode
```bash
# Initialize swarm
docker swarm init

# Join as worker
docker swarm join --token <token> <manager-ip>:2377

# Deploy stack
docker stack deploy -c docker-compose.yml mystack

# List services
docker service ls

# Scale service
docker service scale mystack_web=3
```

### 2. Custom Networks
```bash
# Create overlay network
docker network create -d overlay --attachable mynetwork

# Create bridge with custom subnet
docker network create --subnet=172.20.0.0/16 mynetwork
```

### 3. BuildKit Features
```dockerfile
# syntax=docker/dockerfile:1
FROM node:16 AS base

# Mount secrets
RUN --mount=type=secret,id=apikey \
    curl -H "Authorization: $(cat /run/secrets/apikey)" \
    https://api.example.com/data

# Mount cache
RUN --mount=type=cache,target=/root/.npm \
    npm install
```

### 4. Resource Constraints
```bash
# Memory limit
docker run --memory=512m myapp

# CPU limit
docker run --cpus=0.5 myapp

# Block IO limit
docker run --blkio-weight=300 myapp
```

### 5. Logging Drivers
```bash
# JSON file (default)
docker run --log-driver json-file myapp

# Syslog
docker run --log-driver syslog myapp

# Fluentd
docker run --log-driver fluentd --log-opt fluentd-address=localhost:24224 myapp
```

### 6. Container Runtime Security
```bash
# AppArmor profile
docker run --security-opt apparmor:myprofile myapp

# SELinux labels
docker run --security-opt label=level:TopSecret myapp

# Seccomp profile
docker run --security-opt seccomp=myprofile.json myapp
```

### 7. Init System
```dockerfile
# Use init system for proper signal handling
FROM node:16
RUN apt-get update && apt-get install -y tini
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["node", "server.js"]
```

### 8. Registry Operations
```bash
# Login to registry
docker login myregistry.com

# Tag for registry
docker tag myapp myregistry.com/myapp:v1.0

# Push to registry
docker push myregistry.com/myapp:v1.0

# Pull from registry
docker pull myregistry.com/myapp:v1.0
```

---

## Conclusion

Docker is a powerful containerization platform that revolutionizes application deployment and development. This guide covers the essential concepts and commands needed to effectively use Docker in various scenarios.

### Key Takeaways
- Start with simple containers and gradually learn advanced features
- Always follow security best practices
- Use multi-stage builds for production applications
- Leverage Docker Compose for multi-container applications
- Keep images small and secure
- Monitor and log your containers properly

### Next Steps
1. Practice with real applications
2. Learn Kubernetes for orchestration
3. Explore CI/CD integration
4. Study security hardening techniques
5. Learn about monitoring and observability

### Useful Resources
- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)

Happy containerizing! 

---
---
- container shares host os kernel so it not required os per application.
- container offers isolation not virtualization.
- containers are os virtualization.
- vms are hardware virtualization.
- vms need os
- container dont need os
- container uses host os for compute resources.
- docker manages container
- docker is runtime environment.
- add docker engine image for more details
- usemod -aG docker ubuntu # this command is used to add ubuntu user in docker group
- containers runs from image
- images are called repository in dockerhub
- exec and -it is used to login intract with the container
- docker inspect is give meta data
- when we run a docker conatiner it runs cmd then entrypoint
- there are 2 ways to store container data volume and bindmount
- volume is managed by the docker
- bindmount is used to inject data from host machine to container
- if there is a entrypoint with command and no arguments the user have to pass argumment.
- if entrypoint and cmd are used together then cmd will be the default argument. if user provide argument then it will overwrite cmd argument.
- docker volume prune
- docker system prune