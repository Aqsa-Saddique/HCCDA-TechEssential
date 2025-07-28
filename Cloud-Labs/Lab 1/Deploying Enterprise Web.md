# LAB 1: Deploying an Enterprise Web
Full WordPress Site Deployment with LAMP, RDS, ELB, Auto Scaling, and Monitoring

This project demonstrates how to deploy a highly available and scalable WordPress website on Huawei Cloud infrastructure. The setup includes ECS for compute, RDS for database, LAMP stack for serving web content, Elastic Load Balancer for traffic distribution, and Auto Scaling for elasticity, following enterprise architecture standards.

# Technologies Used
**Cloud Services:** 
Huawei Cloud ECS, RDS, VPC, ELB, AS, IMS, Cloud Eye


**Web Stack:**
Linux, Apache, MySQL, PHP (LAMP)

**App:**
WordPress 4.9.10

**OS:** 
CentOS 7.6 (64-bit)

**Region:**
AP-Singapore

# Deployment Steps

**Cloud Login & Region Setup**

1. Logged into Huawei Cloud IAM user portal using lab credentials.
2. Set region to AP-Singapore for all services

<img width="643" height="332" alt="Login To huaweiCloud" src="https://github.com/user-attachments/assets/ec80363e-94b3-49ec-9678-d278fb39d174" />

**VPC and Network Configuration**

**Created a Virtual Private Cloud (VPC):**

1. Default CIDR and settings.
2. Named vpc-mp

<img width="567" height="115" alt="Created VPC" src="https://github.com/user-attachments/assets/34519998-b8d0-42f1-a310-e4e1e308e373" />


 
**Created a Security Group:**

1. Added inbound rule allowing all traffic (0.0.0.0/0) for all protocols/ports

# ECS (Elastic Cloud Server) Setup
**Launched a new ECS with:**

Billing: Pay-per-use

CPU: 1 vCPU, RAM: 1 GB

OS: CentOS 7.6 64-bit

System Disk: 40 GB High I/O

EIP: Dynamic BGP (2 Mbit/s)

Login: Username root, password-based

Connected ECS to created VPC and Security Group.

<img width="720" height="351" alt="image" src="https://github.com/user-attachments/assets/34c0dabf-34fd-4a01-98b3-4c901597560b" />

<img width="720" height="54" alt="image" src="https://github.com/user-attachments/assets/fcdd23e0-6e4a-49c9-8626-49414281e18d" />


# RDS (Relational Database Service) Setup

Purchased a MySQL 8.0 Primary/Standby RDS instance with:

1. 2 vCPUs, 4 GB RAM

2. Cloud SSD storage

3. VPC and security group assigned

4. Password set for root user

Waited 6–10 minutes for RDS creation.

Retrieved floating IP address of the database

<img width="720" height="489" alt="image" src="https://github.com/user-attachments/assets/cf7d90af-24d3-4baa-b1e6-fbc2ec27331d" />

<img width="720" height="185" alt="image" src="https://github.com/user-attachments/assets/fcd6dbb2-cf9a-4583-b1ab-3e050e75b760" />

<img width="720" height="822" alt="image" src="https://github.com/user-attachments/assets/88a6a5d8-a99b-414e-a4d9-99f049b0d19d" />

<img width="720" height="391" alt="image" src="https://github.com/user-attachments/assets/0a9140da-739b-453f-85a1-2ecaeed0625d" />

# Setting Up the Linux, Apache, MySQL, PHP (LAMP) Environment

Connected to ECS via Remote Login (VNC).

Go back to the ECS console and click Remote Login in the Operation column of the purchased ECS.

In the VNC window, enter the username (root for Linux ECSs by default) and password for login.

<img width="720" height="130" alt="image" src="https://github.com/user-attachments/assets/a39f5bc3-4b5e-4650-86c1-e2d52156c58d" />

**Run the following command to install LAMP and enable the services you will need:**

*yum install -y httpd php php-fpm php-mysql mysql*

**Edited Apache config:**

*vim /etc/httpd/conf/httpd.conf*

# Added: ServerName localhost:80
Enabled and started required services:


systemctl start httpd

systemctl enable httpd

systemctl start php-fpm

systemctl enable php-fpm

<img width="720" height="137" alt="image" src="https://github.com/user-attachments/assets/0538e743-419f-4731-8a14-6c1cb826c17c" />

<img width="720" height="189" alt="image" src="https://github.com/user-attachments/assets/4969e008-aeec-46fc-ba02-4d444c6fc4b8" />

# WordPress Installation and Setup

**Downloaded and extracted WordPress:**

wget -c https://koolabsfiles.obs.ap-southeast-3.myhuaweicloud.com:443/20220731/wordpress-4.9.10.tar.gz
tar -zxvf wordpress-4.9.10.tar.gz -C /var/www/html
chmod -R 777 /var/www/html

**Accessed WordPress setup via browser:**

http://<ECS_EIP>/wordpress/

**In RDS Console:**

Logged into the DB using the GUI.

**Ran SQL query:**

*CREATE DATABASE wordpress;*

**In WordPress setup:**

DB Name: wordpress

DB User: root

DB Password: (your RDS password)

DB Host: (floating IP of RDS)

Finalized WordPress site title, admin user, password, and email.

<img width="720" height="314" alt="image" src="https://github.com/user-attachments/assets/5914a523-31d0-4f25-baa8-4a2d69a77fba" />

<img width="722" height="734" alt="image" src="https://github.com/user-attachments/assets/e704eb2e-44fd-4e10-925c-2e9f6a3b2b91" />

<img width="628" height="558" alt="image" src="https://github.com/user-attachments/assets/d446cb5b-4f26-4bf0-8e71-30885c723980" />

# Load Balancer (ELB) Configuration

**Created a Shared ELB with:**

Public EIP, HTTP listener on port 80

Backend server group linked to ECS

Health Check: Disabled for demo purpose

<img width="720" height="134" alt="image" src="https://github.com/user-attachments/assets/fff386d8-fca9-4dfd-a370-91e0a13d22e7" />

<img width="720" height="413" alt="image" src="https://github.com/user-attachments/assets/0fa69c39-e91d-4f0a-88ad-40ff21cfa1a9" />

  <img width="720" height="531" alt="image" src="https://github.com/user-attachments/assets/cb19b5c6-65bc-4a80-bd97-baaf4f0f452a" />
 
# Creating an ECS Image (IMS)

Stopped the existing ECS instance.

Created a System Disk Image (ims-mp) using Image Management Service (IMS).

Restarted ECS after image status changed to Normal.

<img width="720" height="550" alt="image" src="https://github.com/user-attachments/assets/bb9c8bca-0fb0-4569-b714-ecdf0cd9544b" />

# Auto Scaling (AS) Configuration
**Created an AS Configuration:**

Used ECS image

No EIP (used behind ELB)

Same security group

**Created an AS Group:**

Attached ELB created earlier

Allowed dynamic scaling

**Configured Scaling Policies:**

Scale out: If CPU ≥ 60%, add 1 ECS

Scale in: If CPU ≤ 20%, remove 1 ECS

**Verified scaling:**

2 ECS instances were added dynamically to backend group.

<img width="722" height="566" alt="image" src="https://github.com/user-attachments/assets/bd4ba30f-d01a-4a22-9d05-dc8f3a66dda3" />

3 Final Testing
Visited: http://<LoadBalancer_EIP>/wordpress/

**Verified:**

WordPress website loaded correctly

Multiple ECS backend servers serving requests via ELB

<img width="722" height="768" alt="image" src="https://github.com/user-attachments/assets/8b01b2a0-f853-4f5b-b34f-8506e5404054" />

# Monitoring with Cloud Eye

**Navigated to Cloud Eye for:**

Resource monitoring overview

Alarm statistics

ECS-level metrics

Reviewed:

Alarm history

ECS CPU and memory usage

Scaling events triggered by policies

<img width="720" height="432" alt="image" src="https://github.com/user-attachments/assets/f7f6f498-8b34-4e07-9c8b-f0dc109afc60" />

<img width="720" height="222" alt="image" src="https://github.com/user-attachments/assets/306557ca-cf8f-46a2-9178-5484a60a2d91" />

<img width="722" height="342" alt="image" src="https://github.com/user-attachments/assets/0d797e3b-130a-4916-9b44-de10fe8131dc" />

