# Lab 2: Storage Services Pratice
## Introduction
As cloud computing grows, so does the need for scalable, durable, and efficient storage solutions. Huawei Cloud provides multiple storage services designed for specific use cases — from block-level storage for compute servers to scalable object storage and shared file systems. This lab explores three essential Huawei Cloud storage services: Elastic Volume Service (EVS), Object Storage Service (OBS), and Scalable File Service (SFS). The exercises guide the user through provisioning, attaching, formatting, and verifying storage operations across both Windows and Linux environments.

# 1. Managing Elastic Volume Service (EVS)
## 1.1 Overview and Objectives
Elastic Volume Service provides persistent block storage for Elastic Cloud Servers and Bare Metal Servers. These disks feature high durability, low latency, and data redundancy. This section covers purchasing, attaching, initializing, detaching, and verifying EVS disks across Windows and Linux servers.

## 1.2 Attaching and Initializing EVS on Windows Servers
Two ECS instances named ecs-vivi and ecs-test are created in the AP Singapore region

A new EVS disk is purchased and initially attached to ecs-vivi

The disk is initialized, formatted, and a test file is created

The disk is then detached and attached to ecs-test to verify data persistence

## 1.3 EVS Disk Operations on Linux Servers
A Linux ECS is created and a new EVS disk is attached

The disk is partitioned and formatted using fdisk and mkfs

A mount point is created and the disk is mounted using mount

Optionally, the disk is set to mount automatically on system boot using the fstab file

## 1.4 Using Snapshots for Data Protection
A test file is created on the Linux EVS disk

A snapshot is created from the disk

A new disk is created from this snapshot and mounted

File existence is verified, confirming snapshot integrity

# 2. Using Object Storage Service (OBS)
## 2.1 Introduction to OBS and Objectives
Object Storage Service is a reliable and scalable solution for storing unstructured data such as media files, backups, and documents. It supports REST APIs, browser-based access, and third-party tools. In this lab, users learn to create buckets, manage files, and use upload and download features.

## 2.2 Working with Buckets and Objects
A bucket is created in the AP Singapore region with private access policy and standard storage class

Files and folders are uploaded using the web interface

Files are downloaded locally and later deleted through the object list interface

## 2.3 Authentication Mechanism for External Access
Console access is done through Huawei Cloud credentials

When accessing via APIs or tools like OBS Browser or obsutil, users must authenticate using Access Key and Secret Key pairs

IAM users can perform the same operations with proper permissions

# 3. Managing Shared Storage with Scalable File Service (SFS)
## 3.1 Introduction to SFS and Objectives
Scalable File Service provides a shared file system accessible by multiple ECS instances across operating systems and networks. It supports NFS protocols and is ideal for workloads requiring simultaneous read and write operations from different nodes. This lab demonstrates how to mount and verify SFS Turbo on both Linux and Windows ECS instances.

## 3.2 Creating and Configuring the File System
A file system named sfs-mp is created with 500 GB capacity using the NFS protocol

Both a Linux and a Windows ECS are created, and EIPs are bound to them

The file system is mounted on both ECSs to simulate a shared-access environment

## 3.3 Mounting the File System on Linux ECS
Necessary NFS packages are checked and installed

The mount point is created using mkdir and mounted using the mount command with NFS parameters

The file system is added to the fstab file to persist across reboots

File creation and content verification confirms successful mount

## 3.4 Mounting the File System on Windows ECS
The NFS client is installed via Server Manager

Mounting is configured using Control Panel and Command Prompt

After setting properties, the file system is mounted using an NFS mount command

Verification shows the same file created from Linux is accessible on Windows

<img width="720" height="194" alt="image" src="https://github.com/user-attachments/assets/9cd1d510-57b8-4310-ac3f-c83e3c173392" />

<img width="720" height="336" alt="image" src="https://github.com/user-attachments/assets/75999b9f-7c88-4fa6-a93c-421a9936184b" />

<img width="720" height="591" alt="image" src="https://github.com/user-attachments/assets/94afb61a-8a49-4c47-ba51-5c46d52bf5e9" />

<img width="720" height="348" alt="image" src="https://github.com/user-attachments/assets/42aacd00-7c47-4ac5-8139-722624e52a87" />

# Conclusion
This lab demonstrated the practical usage of Huawei Cloud's storage services across various scenarios. EVS was used to provide persistent, block-level storage and verified across different ECS instances. OBS was used for object-based file storage and management. SFS provided shared file access between Linux and Windows systems. Together, these services offer powerful and flexible storage options to meet the growing demands of cloud applications.





