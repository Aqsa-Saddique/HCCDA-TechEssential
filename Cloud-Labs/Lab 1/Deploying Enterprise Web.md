# LAB 1: Deploying an Enterprise Web
## Introduction
In the modern digital era, enterprises demand scalable, secure, and highly available infrastructure to support business-critical applications. Cloud platforms, such as Huawei Cloud, provide the tools and flexibility to build such environments efficiently. This lab demonstrates the end-to-end deployment of an enterprise-grade website using Huawei Cloud’s core services — Elastic Cloud Server (ECS), Relational Database Service (RDS), Elastic Load Balancer (ELB), and Auto Scaling (AS). The architecture is based on a distributed model, isolating web and database workloads to improve performance, manageability, and fault tolerance.

# 1. Establishing the Cloud Network Environment
Before provisioning compute or storage services, it is essential to establish a secure and isolated network environment. Huawei Cloud provides the Virtual Private Cloud (VPC) service, allowing users to define IP ranges, subnets, and traffic routing policies. Alongside this, Security Groups are configured to control access to resources, functioning as virtual firewalls.

## 1.1 Deploying a Virtual Private Cloud (VPC)
A VPC was deployed in the AP-Singapore region to serve as the foundation for all subsequent resources. The creation process automatically generated an associated subnet, enabling internal communication and routing within the cloud infrastructure.

<img width="563" height="111" alt="image" src="https://github.com/user-attachments/assets/3fdc7670-1a90-4c8e-a4ce-254fd4018812" />

## 1.2 Defining Security Group Rules
A custom Security Group was configured with an inbound rule allowing full access from IP range 0.0.0.0/0. This open configuration is suitable for testing and demonstration purposes but should be restricted to specific IPs in production for enhanced security.

<img width="722" height="502" alt="image" src="https://github.com/user-attachments/assets/7a7f54ad-a726-4d5f-9fea-f834be0d39af" />

# 2. Provisioning Compute and Database Services
With the network environment in place, the next step involves provisioning compute and database resources. Huawei Cloud’s ECS service is used to deploy a Linux-based web server, while the RDS service is used to provision a highly available, managed MySQL database instance. Both components are assigned to the previously configured VPC for seamless communication.

## 2.1 Launching an ECS Instance for Web Hosting
An ECS instance was provisioned to host the website's application layer. Configuration parameters included:

Billing Mode: Pay-per-use

Operating System: CentOS 7.6 (64-bit)

Instance Type: 1 vCPU, 1 GB RAM

Login Method: Password authentication

Network: VPC-integrated with associated security group

Elastic IP (EIP): Automatically allocated

This instance serves as the primary web node for hosting the LAMP stack and WordPress.

<img width="720" height="54" alt="image" src="https://github.com/user-attachments/assets/9fab31a6-7fb1-4d56-8326-f3140a0272cb" />

## 2.2 Provisioning the RDS Instance for Data Management
A managed MySQL RDS instance was deployed to serve as the backend database. Key configurations included:

Instance Type: 2 vCPU, 4 GB RAM

Storage: Cloud SSD

Deployment Mode: Primary/Standby for high availability

Network Integration: Same VPC and security group as ECS

This architecture ensures secure, high-speed communication between the web and database layers.

# 3. Installing and Configuring the Web Application
This phase involves preparing the application environment by installing the required LAMP stack components on the ECS, creating the WordPress database in RDS, and completing the WordPress installation through the web interface.

## 3.1 Setting Up the LAMP Stack
The following packages were installed via yum:

**yum install -y httpd php php-fpm php-mysql mysql**

The Apache configuration file (httpd.conf) was modified to define the server name, and the latest WordPress package was downloaded, extracted to /var/www/html/, and given appropriate permissions. 

Services httpd and php-fpm were started and configured to auto-start on boot.

## 3.2 Creating a Dedicated WordPress Database
A new MySQL database named wordpress was created using the RDS web-based console. SQL query used:

CREATE DATABASE wordpress;
This database acts as the data store for the WordPress application.

## 3.3 Running the WordPress Installation Wizard
The WordPress installer was accessed by entering the ECS’s public EIP in a browser. Required database connection details were filled in using the RDS floating IP, username, and password. The setup was completed by defining site name, admin user credentials, and email.

# 4. Enabling High Availability and Scalability
To ensure enterprise-grade reliability, Huawei Cloud’s Load Balancer and Auto Scaling services were integrated. These features allow the infrastructure to handle varying traffic loads and minimize service interruptions due to server failure.

## 4.1 Deploying an Elastic Load Balancer (ELB)
An ELB of type Shared/Public was deployed and attached to the existing VPC. A listener was configured on port 80 to forward HTTP traffic to the ECS instance. Health checks were manually disabled for simplicity, but in production, they are crucial for automatic fault detection and rerouting.

## 4.2 Creating a Custom ECS System Image
To enable scaling, a system disk image of the configured ECS was created using the Image Management Service. This image captures all installed packages, configurations, and WordPress files, ensuring consistency across any new instances launched by the Auto Scaling group.

## 4.3 Setting Up Auto Scaling Policies
An Auto Scaling group was created using the ECS image. The group was linked to the ELB and configured with two CPU-based policies:

Scale-Out Policy: Add one instance when CPU usage ≥ 60%

Scale-In Policy: Remove one instance when CPU usage ≤ 20%

The configuration was validated by observing the automatic provisioning of additional ECS instances in response to simulated CPU load.

# 5. Verifying Deployment and Monitoring Performance
In the final phase, we tested the availability of the deployed application and monitored resource usage using Huawei Cloud’s built-in observability tools.

## 5.1 Accessing the WordPress Site via ELB
The WordPress homepage was accessed using the public IP of the ELB. Successful page load and dashboard login confirmed the proper integration of ECS, RDS, and ELB. Load balancing functionality was verified by ensuring that requests reached backend ECS instances as expected.

## 5.2 Monitoring Resources via Cloud Eye
Huawei Cloud Eye was used to observe ECS and RDS metrics such as CPU usage, memory utilization, and network traffic. Alarm records and historical data were reviewed to verify the functioning of auto scaling policies. This tool helps ensure service reliability by enabling proactive monitoring and timely response to performance issues.

<img width="720" height="133" alt="image" src="https://github.com/user-attachments/assets/f35d4958-609b-4d40-805f-e5e21ba7271a" />

<img width="722" height="342" alt="image" src="https://github.com/user-attachments/assets/cc0eba36-c1c4-4ce0-b227-a41299615b86" />



