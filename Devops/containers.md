# Difference between Container and Virtual machine
## Virtual Machine
There will be a host os after on top of that there will a hyperviser.Virtul machine runs on top of an emulating software called the hypervisor which sits between the hardware and the virtual machine. The hypervisor is the key to enabling virtualization. It manages the sharing of physical resources into virtual machines. Each virtual machine runs its guest operating system. They are less agile and have lower portability than containers.
## containers
It sits on the top of a physical server and its host operating system. They share a common operating system that requires care and feeding for bug fixes and patches. They are more agile and have higher portability than virtual machines.

    Containers offer Isolation and not virtualization.

    For virtualization we can use Virtual Machine.

    For understanding we can think containers as OS virtualization.
## Docker
Docker is an open-source platform that enables developers to automate the deployment, scaling, and management of applications in lightweight, portable containers. Containers package an application and its dependencies (such as libraries, configurations, and binaries) into a single, isolated unit that can run consistently across different environments, whether it's on a developer's local machine, a testing server, or a production cloud environment. They are light weight,portable, isolation, containrization, virson control and reusablity, scalling and archestration.
It is a container runtime environment for developing, sheeping and running applications.Docker registry is place where Docker Container Images are stored.Docker containers are created from Docker Images.





