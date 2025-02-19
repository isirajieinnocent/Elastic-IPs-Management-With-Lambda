**Architecture**

![image](https://github.com/user-attachments/assets/6b3ccea1-d022-4214-a5c7-5dd40669283b)


**Technical Implementation Explanation**

This project involves the automation of Elastic IP management in AWS by using a Lambda function to detect and release unattached Elastic IPs (EIPs). 
These are public IP addresses that AWS EC2 instances can use. If an Elastic IP is not associated with any running instance, it could incur additional costs, so releasing them back to AWS helps reduce unnecessary charges.

**Here’s a breakdown of how the implementation works:**

AWS Lambda: The solution utilizes AWS Lambda, a serverless compute service, to automate the cleanup process. 
Lambda functions are event-driven, which means they can be triggered automatically based on predefined schedules or AWS events, making them ideal for background tasks like this.

Boto3 SDK: The function uses Boto3, the AWS SDK for Python, to interact with EC2 services. Boto3 provides a Python interface for managing AWS resources, allowing the Lambda function to list and manage Elastic IPs programmatically.

**Iterating Over Elastic IPs:**

The Lambda function iterates through all Elastic IPs allocated in the AWS account by using vpc_addresses.all() from the Boto3 EC2 resource.
For each IP, the function checks if it's unattached by verifying whether the instance_id attribute is None. If the instance ID is None, this indicates the IP is not associated with any EC2 instance and is thus eligible for release.
Release Unattached IPs: Once an unattached Elastic IP is identified, the function releases it back to AWS to prevent unnecessary charges.
This is done using the elastic_ip.release() method, which releases the Elastic IP and makes it available for reuse.

Logging: To keep track of the actions being performed, a log message is printed whenever an unattached Elastic IP is detected and released. This helps with monitoring and troubleshooting.

Return Status: After processing all Elastic IPs, the function returns a 200 status code with a success message, indicating that the cleanup task has been successfully completed.

This implementation ensures cost optimization by automatically managing unused resources, preventing Elastic IPs from accumulating and incurring unnecessary costs.

**summary**
This is a solution that automates the release of unattached Elastic IPs (EIPs) in an AWS account. Elastic IPs that aren't associated with running EC2 instances can incur unnecessary costs,
so the Lambda function identifies and releases these unused IPs automatically, optimizing costs for the infrastructure.
The solution leverages the Boto3 SDK for AWS resource management and generates logs to track every action, ensuring visibility and control
