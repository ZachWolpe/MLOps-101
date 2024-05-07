# Kubernetes Key Features

Kubernetes, often abbreviated as `K8s`, is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. Here are some of its key features:

1. **Automated Scheduling**:
Kubernetes scheduler automatically places containers based on their resource requirements and other constraints, without sacrificing availability.

2. **Self-Healing Capabilities**:
Kubernetes automatically replaces or restarts containers that fail, kills containers that don't respond to user-defined health checks, and doesn't advertise them to clients until they are ready to serve.

3. **Horizontal Scaling**:
You can scale applications up or down with simple commands, a UI, or automatically based on CPU usage.

4. **Service Discovery and Load Balancing**:
Kubernetes can expose a container using the DNS name or using their own IP address. If traffic to a container is high, Kubernetes is able to load balance and distribute the network traffic so that the deployment is stable.

5. **Automated Rollouts and Rollbacks**:
You can describe the desired state for your deployed containers using Kubernetes, and it can change the actual state to the desired state at a controlled rate. For example, you can automate Kubernetes to create new containers for your deployment, remove existing containers, and adopt all their resources to the new container.

6. **Secret and Configuration Management**:
Kubernetes lets you store and manage sensitive information, such as passwords, OAuth tokens, and SSH keys. You can deploy and update secrets and application configuration without rebuilding your container images and without exposing secrets in your stack configuration.

7. **Storage Orchestration**:
Kubernetes allows you to automatically mount a storage system of your choice, whether from local storage, a public cloud provider such as GCP or AWS, or a network storage system like NFS, iSCSI, etc.

8. **Batch Execution**:
In addition to services, Kubernetes can manage your batch and CI workloads, replacing containers that fail, if desired.

9. **IPv4/IPv6 Dual-Stack**:
Support for IPv4 and IPv6 addresses in a single cluster, enabling the allocation of both types of addresses to Pods and Services.

These features make Kubernetes a powerful tool for managing complex containerized applications, providing robust, scalable, and efficient infrastructure for deploying modern software systems.