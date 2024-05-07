# What is a Hypervisor?

A hypervisor, also known as a virtual machine monitor (VMM), is software, firmware, or hardware that creates and runs virtual machines (VMs). It allows multiple VMs to run on a single physical machine, with each VM having access to the underlying hardware's resources such as CPU, memory, and storage. Hypervisors are crucial in virtualization technology, enabling efficient resource management and isolation between different VMs.
There are two types of hypervisors:

1. **Type 1 (Bare Metal)**: This type of hypervisor runs directly on the host's hardware to control the hardware and to manage guest operating systems. Examples include VMware ESXi, Microsoft Hyper-V, and Xen.

2. **Type 2 (Hosted)**: This hypervisor runs on a conventional operating system just as other computer programs do. Examples include VMware Workstation and Oracle VirtualBox.