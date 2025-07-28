# Lab 2: Storage Services Pratice

This repository documents hands-on experience with Huawei Cloud's block storage (EVS), object storage (OBS), and scalable file service (SFS) technologies. 

It includes practical steps to purchase, configure, and validate various storage operations on Windows and Linux environments.

# Elastic Volume Service (EVS)

**Objectives**

1. Purchase EVS Disks

2. Attach EVS Disks to ECS

3. Initialize and use disks on Windows & Linux

4. Transfer and verify disk data between ECSs

5. Use EVS Snapshots

# Windows ECS Workflow

1. Create VPC & ECS
   
2. Region: AP-Singapore

3. OS: Windows Server 2012 R2

4. Disk: 40GB system + 20GB EVS (High I/O)

# Attach & Initialize EVS Disk

1. Attach disk from EVS console

2. Initialize and partition using Disk Management

3. Format the volume and assign a drive letter

<img width="720" height="584" alt="image" src="https://github.com/user-attachments/assets/61673d94-8cca-4a94-8538-f6f35d0dc531" />

<img width="720" height="275" alt="image" src="https://github.com/user-attachments/assets/74673bd7-9a29-468c-8945-34182741f261" />

<img width="720" height="194" alt="image" src="https://github.com/user-attachments/assets/f5bc4ea4-bb0a-4109-891f-790c167a968c" />

# Verify Portability

Create a file on ecs-vivi

Detach and reattach disk to ecs-test

Confirm file presence to validate persistence

<img width="720" height="336" alt="image" src="https://github.com/user-attachments/assets/f780047c-e136-4a39-b6cf-2265cac58d02" />

<img width="720" height="336" alt="image" src="https://github.com/user-attachments/assets/ac4db0ff-bf34-4bc3-bc8d-f6b3ab167a4c" />

<img width="720" height="373" alt="image" src="https://github.com/user-attachments/assets/7c9393c3-2a08-4bc6-922d-d6f95b8c404f" />

<img width="560" height="472" alt="image" src="https://github.com/user-attachments/assets/955db205-6c54-48a5-8fd7-77fb33fa1f3a" />

# Initializing an EVS Disk

After a data disk is attached to an ECS, you must log in to the ECS and initialize the disk before us ing it.

Step 1: Locate the row that contains the target ECS and click Remote Login in the Operation colu mn.

Step 2: Log in using Remote Login on the management console. On the desktop of the ECS, choo se Start > Server Manager.

On the dashboard, choose Tools > Computer Management.

<img width="720" height="150" alt="image" src="https://github.com/user-attachments/assets/769f14cc-e024-4cd4-b9d2-76812454cfb3" />

<img width="720" height="633" alt="image" src="https://github.com/user-attachments/assets/e34cbe66-f130-47c1-bec0-f487cfe43d80" />

Step 3: In the navigation tree on the left, choose Storage > Disk Management.

Step 4: On the Disk Management page, if the status of new disk is Offline, right-click Offline and c hoose Online to online the disk. 

If the status is Not Initialized, right-click the status and choose Ini tialize Disk.

In the Initialize Disk window, select the target disk, click MBR (Master Boot Record) or GPT (GUID Partition Table), and click OK.

<img width="720" height="582" alt="image" src="https://github.com/user-attachments/assets/9d548a6d-71c5-415f-9967-74ea92026da1" />

<img width="720" height="569" alt="image" src="https://github.com/user-attachments/assets/6581473d-e45d-410f-9298-2231dea6053a" />

<img width="709" height="558" alt="image" src="https://github.com/user-attachments/assets/c22a9263-6616-4942-8013-f9472e1fa930" />

<img width="720" height="640" alt="image" src="https://github.com/user-attachments/assets/11e53d79-1b04-415f-b7ac-bc80d61d9ca1" />


<img width="720" height="514" alt="image" src="https://github.com/user-attachments/assets/0218463e-a5b0-4547-b8aa-43d83868e37f" />

# Detaching an EVS Disk and Performing Verification

Before you detach an EVS disk on the console, log in to the ECS and unmount the disk.

To verify that data on a detached EVS disk can still be used, we will detach the disk and then attac h it to another ECS for verification.

Step 1 Locate the row that contains the target ECS and click Remote Login in the Operation colu mn.

Step 2 Create a test file test.txt on the attached EVS disk.

<img width="720" height="61" alt="image" src="https://github.com/user-attachments/assets/1a22750b-9b0c-486d-a02d-8206e71e1d38" />

<img width="720" height="623" alt="image" src="https://github.com/user-attachments/assets/04cff9dc-4603-4d82-b9ee-7b2629f6f570" />

<img width="720" height="459" alt="image" src="https://github.com/user-attachments/assets/f3404b1f-8fe4-4d5a-8066-576d3a594bcd" />

<img width="720" height="720" alt="image" src="https://github.com/user-attachments/assets/2aea2cc7-f560-4a9d-8d38-d7ae126192f9" />

# Attaching an EVS Disk to a Linux ECS

Hands-On: Linux ECS

Create CentOS ECS and attach EVS

Partition and format disk using fdisk and mkfs

Mount to /mnt/sdc, optionally add to /etc/fstab for auto-mount

Test snapshot: create a file → take snapshot → create disk from snapshot → mount and verify

<img width="720" height="457" alt="image" src="https://github.com/user-attachments/assets/5b83b63a-b2c5-4033-a374-ff1f92ac2180" />

<img width="720" height="145" alt="image" src="https://github.com/user-attachments/assets/9791ccd0-c9ec-4d57-a900-872e9f0ada21" />

# Object Storage Service (OBS)

**Overview**

OBS is a scalable, secure, and durable object storage platform for unstructured data like images, videos, logs, etc.

It supports access via web, SDKs, or APIs and is ideal for backup, cloud-native apps, and static websites.

# Objectives

1. Create buckets

2. Upload/download/delete objects

3. Delete buckets

# Steps

1. Log in to Huawei Cloud (AP-Singapore)

2. Create Bucket

3. Name: test-vivi

4. Storage Class: Standard

5. Policy: Private

6. Upload File

7. Click Upload Object → select file (e.g., background.jpg) → Upload

8. Download File

9. Click object → Download

10. Delete Object / Bucket

11. Use More > Delete

# Scalable File Service (SFS Turbo)

**Overview**

SFS Turbo provides high-performance, shared file systems across ECS, CCE (Kubernetes), and containers.

Ideal for applications that require simultaneous access to data.

Supports NFS protocol

Shared among multiple ECS instances

Easy to scale and manage

# Objectives

Create an SFS Turbo file system

Mount on Linux and Windows ECS

Enable file sharing across ECSs

# Mount SFS on Linux ECS

**Steps**

**Create ECS (CentOS 7.6)**

**Install NFS tools**

*yum install -y nfs-utils bind-utils*

**Create mount directory**
 
*kdir /localfolder*

**Mount file system**

mount -t nfs -o vers=3,timeo=600,nolock \
<SFS_MOUNT_ADDRESS>:/share-id /localfolder
Add to /etc/fstab for auto-mount

echo "<SFS_MOUNT_ADDRESS>:/share-id /localfolder nfs vers=3,timeo=600,nolock 0 0" >> /etc/fstab

# Mount SFS on Windows ECS

**Install NFS Client**

1. Go to Server Manager → Add Roles & Features

2. Select Server for NFS and Client for NFS

**Configure NFS Service**

1. Set transport protocol to TCP

2. Use hard mounts

**Mount File System**

mount -o nolock -o casesensitive=yes <IP>:/share X:

**Verify Shared File**

Open Explorer → X: should show file created from Linux ECS

<img width="720" height="348" alt="image" src="https://github.com/user-attachments/assets/56e0c6d2-fb78-497b-92b0-ba3469997f2d" />

