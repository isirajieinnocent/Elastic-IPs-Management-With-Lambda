<h1> Project Overview </h1>
  
This project showcases my ability to automate Elastic IP (EIP) management in AWS using a serverless architecture. It detects and releases unattached Elastic IPs to prevent unnecessary costs, ensuring cost optimization for AWS infrastructure.

<h1> The Architecture </h1>

![image](https://github.com/user-attachments/assets/6b3ccea1-d022-4214-a5c7-5dd40669283b)

<h1> Solution Overview </h1>
  
**AWS Lambda:** Automates the cleanup process by detecting and releasing unattached Elastic IPs.

**Boto3 SDK:** Used to interact with AWS EC2 services, enabling programmatic management of Elastic IPs.

**Iteration & Validation:**

The Lambda function iterates through all Elastic IPs in the account.

Checks if an Elastic IP is unattached (i.e., instance_id is None).

**Release Unattached IPs:**

Unattached Elastic IPs are released using the elastic_ip.release() method.

**Logging & Monitoring:**

Logs are generated for each action (e.g., detection and release of unattached IPs).

A 200 status code is returned upon successful completion.

<h1> Key Technologies </h1>
  
**AWS Lambda:** Serverless compute service for automation.

**Boto3 SDK:** Python library for AWS resource management.

**AWS EC2:** Manages Elastic IPs and associated instances.

<h1> Impact </h1>
  
**Cost Optimization:** Prevents unnecessary charges by releasing unattached Elastic IPs.

**Automation:** Eliminates manual intervention, saving time and effort.

**Visibility:** Logs provide transparency and aid in troubleshooting.

<h1> Key Achievements </h1>
  
Designed a serverless solution to automate Elastic IP management.

Leveraged Boto3 SDK for seamless interaction with AWS EC2 services.

Implemented logging for monitoring and troubleshooting.

**This project highlights my expertise in AWS serverless architecture, Python programming, and cost optimization strategies.**
