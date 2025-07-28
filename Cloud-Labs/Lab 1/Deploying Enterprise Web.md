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
 
**Created a Security Group:**

1. Added inbound rule allowing all traffic (0.0.0.0/0) for all protocols/ports


 




   



