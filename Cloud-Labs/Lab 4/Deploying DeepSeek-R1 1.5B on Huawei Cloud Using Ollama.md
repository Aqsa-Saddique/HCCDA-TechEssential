# LAB 4 : Deploying DeepSeek-R1 1.5B on Huawei Cloud Using Ollama
# Introduction
This lab provides a detailed, step-by-step guide for deploying the DeepSeek-R1 1.5B large language model on Huawei Cloud. The deployment process includes provisioning an Elastic Cloud Server (ECS), installing the Ollama runtime environment, and running the model using either Ollama's online registry or a Huawei OBS backup.

# 1. Prerequisites
Before starting, ensure you have access to the Huawei Cloud Lab Desktop using the provided IAM account. An active internet connection is required to download necessary files and packages. Tip: 
If login fails, refresh the lab page and re-enter your IAM credentials to ensure access to the Huawei Cloud console.

<img width="624" height="533" alt="image" src="https://github.com/user-attachments/assets/fd580822-b1a7-4179-ac9f-e17d8bec1c5e" />


# 2. Preparing the Lab Environment
## 2.1 Creating an ECS Instance
To begin, log in to the Huawei Cloud Console and navigate to the Elastic Cloud Server (ECS) section, either from the service list or by searching "ECS". Click on Buy ECS and choose Custom Configuration. Configure the ECS instance with the following specifications:

Set the Billing Mode to Pay-per-use,

Choose the Region as AP-Singapore,

Select the Architecture as x86,

Pick the Flavor as c6.xlarge.2 which provides 4 vCPUs and 8 GiB RAM,

Use CentOS 8.2 64bit as the image with a 40 GiB system disk.

For network configuration, use the default VPC and Security Group (or create them if not available). Set the EIP to Auto-assign, select Dynamic BGP for EIP Type, and set the Bandwidth to 100 Mbit/s.

Assign a name to the ECS instance such as ecs-cent, and set the login password to Huawei1234%. Once all settings are configured, click Submit, followed by Agree and Submit to launch the instance.

## 2.2 Logging In to ECS
After deployment, open CloudShell in the Huawei Cloud Console. Use it to connect to your ECS instance. When prompted, enter the password Huawei1234% to access the server terminal.

<img width="624" height="41" alt="image" src="https://github.com/user-attachments/assets/a731530a-c8c0-4927-8a76-ca236412e520" />

<img width="624" height="64" alt="image" src="https://github.com/user-attachments/assets/aebc2b5c-6487-4910-ae2f-bfde809b5c08" />


# 3. Installing Ollama
Ollama is a lightweight runtime that allows you to run large language models locally. You can install it using one of two methods—either directly from GitHub or from a Huawei Cloud OBS backup if GitHub is inaccessible.

## 3.1 Solution 1: Install via GitHub
To install Ollama from GitHub, run the following command in your ECS terminal:

curl -fsSL https://ollama.com/install.sh | sh

ollama -v

This method installs Ollama and verifies the version. If the script fails due to network restrictions, proceed with Solution 2.

## 3.2 Solution 2: Install via Huawei Cloud OBS Backup
If GitHub is not accessible, download the pre-built binary and set up Ollama manually:

wget https://sandbox-experiment-files.obs.cn-north-4.myhuaweicloud.com/deepseek/ollama-linux-amd64.tgz

sudo tar -C /usr -xzf ollama-linux-amd64.tgz

sudo chmod +x /usr/bin/ollama

Check whether the ollama user exists by running:

If the user is not found, create it using:

sudo useradd -r -s /bin/false -m -d /usr/share/ollama ollama

Now, create a systemd service file to manage Ollama as a background service:

cat << EOF > /etc/systemd/system/ollama.service

[Unit]

Description=Ollama Service

After=network-online.target

[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"

ExecStart=/usr/bin/ollama serve

User=ollama

Group=ollama

Restart=always

RestartSec=3

[Install]
WantedBy=default.target

EOF

Finally, enable and start the service with the following commands:

sudo systemctl daemon-reload

sudo systemctl enable ollama

sudo systemctl start ollama

ollama -v

<img width="372" height="55" alt="image" src="https://github.com/user-attachments/assets/beefc257-e3b0-4e54-8876-0208b7d4c754" />

<img width="624" height="91" alt="image" src="https://github.com/user-attachments/assets/6a619a92-fb22-449d-8b39-5ac6e375f093" />

<img width="624" height="67" alt="image" src="https://github.com/user-attachments/assets/e9d73f2c-43eb-43d1-a1de-a768d79cd180" />

# 4. Deploying the DeepSeek-R1 1.5B Model
Once Ollama is installed and running, you can deploy the DeepSeek model using one of two options: downloading from Ollama’s public registry or loading from Huawei OBS.

## 4.1 Solution 1: Pull from Ollama Registry
To download the model directly, run the following:

ollama pull deepseek-r1:1.5b

ollama run deepseek-r1:1.5b

This command fetches the model and launches it. If the download is interrupted, press Ctrl+C and re-run the command—it will resume from where it stopped.

## 4.2 Solution 2: Download from Huawei Cloud OBS
If registry access is blocked or slow, you can use a pre-packaged model archive hosted on Huawei OBS:

wget https://sandbox-experiment-files.obs.cn-north-4.myhuaweicloud.com/deepseek/ollama_deepseek_r1_1.5b.tar.gz

sudo tar -C /usr/share/ollama/.ollama/models -xzf ollama_deepseek_r1_1.5b.tar.gz

cd /usr/share/ollama/.ollama/models

mv ./deepseek/sha256* ./blobs

mkdir -p ./manifests/registry.ollama.ai/library/deepseek-r1

mv ./deepseek/1.5b ./manifests/registry.ollama.ai/library/deepseek-r1

rm -rf deepseek/

After unpacking, list available models and start DeepSeek:

ollama list

ollama run deepseek-r1:1.5b

<img width="624" height="65" alt="image" src="https://github.com/user-attachments/assets/f4932d2d-818b-4ea6-93d7-f359cec7444f" />

<img width="624" height="52" alt="image" src="https://github.com/user-attachments/assets/f59eee53-e518-4e94-baa1-fa488858c231" />

# 5.Final notes
You can now interact with the DeepSeek-R1 1.5B model in your terminal. If the responses seem inconsistent or context gets lost, type /bye to reset the model session.

# Conclusion
This lab demonstrated how to deploy a lightweight and private LLM setup using Ollama on Huawei Cloud ECS. You successfully created a virtual server, installed the Ollama runtime, and deployed the DeepSeek-R1 1.5B model using both GitHub and Huawei OBS options. This solution is cost-effective, self-contained, and ideal for rapid prototyping or private inference workflows.
  
