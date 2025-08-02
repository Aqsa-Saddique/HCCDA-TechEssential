# LAB:3 Provisioning and Managing Elastic Cloud Servers on Huawei Cloud
# Introduction
Elastic Cloud Servers (ECS) are the foundation of compute resources in cloud infrastructure. This lab provides hands-on experience with creating both Windows and Linux ECS instances using Huawei Cloud. It also covers customizing ECS specifications, creating private system images, and managing those images for reuse and sharing. By the end of the lab, students will have created ECS instances, configured their environments, and replicated custom server setups through image management.

# 1. Deploying and Managing ECS Instances
## 1.1 Creating Windows and Linux ECS Instances
To begin, a Virtual Private Cloud (VPC) and subnet were created in the AP Singapore region with defined CIDR blocks. Two ECS instances were provisioned — one running Windows Server 2012 R2 and the other CentOS 7.6. Basic configurations included general-purpose specifications, public images, 40 GB system disks, and login via password. The Windows ECS was created without EIP, while the Linux ECS was assigned one automatically for remote access.

<img width="720" height="194" alt="image" src="https://github.com/user-attachments/assets/042d786f-871b-4365-8fd2-d58ca47b44b1" />

<img width="720" height="208" alt="image" src="https://github.com/user-attachments/assets/119e99b1-6d98-4e37-94ec-544a1c3b56fc" />

## 1.2 Logging In to the ECS Instances
Remote access was established through Huawei Cloud’s built-in VNC console. For the Windows ECS, login was done through the Remote Login interface using the predefined password. For the Linux ECS, access was also performed via Remote Login, using root credentials. GUI was not available for Linux, so the login confirmation was based on terminal welcome messages.

<img width="720" height="336" alt="image" src="https://github.com/user-attachments/assets/a8de8ae7-6fe7-4ea6-991f-7a6ecbe671d9" />

<img width="720" height="275" alt="image" src="https://github.com/user-attachments/assets/6b080d1b-1aab-4529-98f9-9e30ef355ade" />

## 1.3 Modifying ECS Specifications for the Windows Server
To simulate performance scaling, the Windows ECS was stopped and its specifications were modified. The memory was increased from 4 GB to 8 GB using the Modify Specifications feature in the ECS console. After submitting the changes, the ECS was restarted with the new configuration successfully applied.

# 2. Creating and Managing a Windows ECS System Image
## 2.1 Preparing the Windows ECS for Imaging
The Windows ECS was configured to support image creation. DHCP settings were confirmed and enabled. Remote desktop access was allowed through Windows settings and the firewall. Cloudbase-Init, a required agent for injecting instance metadata, was verified to be preinstalled as it came with the public image.

## 2.2 Creating a Windows Private System Image
A private image was created from the configured Windows ECS using the Image Management Service. The system disk image type was selected, and the ECS was used as the source. After submission, the image status was monitored until it changed to Normal, indicating successful creation.

## 2.3 Updating Image Information
After the image was created, its metadata — such as name and description — was modified directly from the Image Management console. This step ensured clarity and traceability when the image was reused or shared.

## 2.4 Duplicating the Image Within the Same Region
The image was replicated under a different name using the Replicate function. This created an identical copy within the same region without encryption. The new image appeared in the private image list with its updated name.

## 2.5 Creating ECS Instances from Private Images
To validate image functionality, a new ECS was created using the previously saved private image. On the ECS purchase page, the system automatically selected the custom image. The new ECS inherited all the configurations and software from the original ECS setup.

# 3. Creating and Managing a Linux ECS System Image
## 3.1 Configuring the Linux ECS for Image Creation
The Linux ECS was accessed remotely, and configuration was verified. DHCP was ensured using the PERSISTENT_DHCLIENT variable in the network configuration file. Two agents — CloudResetPwdAgent and Cloud-Init — were confirmed to be preinstalled. Network rule files were checked and deleted if present to avoid interface conflicts when deploying from the image.

## 3.2 Creating a Linux Private System Image
The Linux ECS was used to create a system disk image through the Image Management Service. The image was named clearly and monitored until its status changed to Normal. This private image now serves as a template for future Linux ECS deployments.

## 3.3 Sharing Private Images with Other Projects
The lab demonstrated image sharing by retrieving the user’s project ID from the credentials menu and adding it to the image’s share settings. This enabled the image to be accessed from another account or project. The recipient then accepted the image from the Shared Images tab.

## 3.4 Granting Permissions to Image Consumers
To allow a tenant to launch instances from a shared image, the image owner added the recipient project as a tenant. The tenant ID was added via the Add Tenant function on the Shared with Tenants tab of the image. This step finalized access control for collaborative use.

<img width="720" height="264" alt="image" src="https://github.com/user-attachments/assets/24023c34-2277-4cf8-8507-4864b0b5c0ac" />

<img width="720" height="562" alt="image" src="https://github.com/user-attachments/assets/23df990d-a8ed-4a10-bd1e-16bb737cde50" />

# Conclusion
This lab guided users through the complete lifecycle of Elastic Cloud Servers on Huawei Cloud. From initial provisioning of both Windows and Linux instances to configuring, customizing, and creating reusable system images, learners gained in-depth experience with compute service management. By learning to replicate and share private images, users can now build scalable, consistent, and efficient cloud server deployments.

