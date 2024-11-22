import boto3

def lambda_handler(event, context):
    ec2_resource = boto3.resource('ec2')

    # Iterates over all Elastic IP addresses in the account
    for elastic_ip in ec2_resource.vpc_addresses.all():
        
        # Checks if the Elastic IP has no associated instance (it's unattached)
        if elastic_ip.instance_id is None:
            # Logs a message specifying the IP address being released.
        
            print(f"\nNo association for Elastic IP: {elastic_ip}. Releasing...\n")
            
            # Releases the unattached Elastic IP to avoid incurring costs
            elastic_ip.release()

    # Returns a success message and HTTP status code
    return {
        'statusCode': 200,
        'body': 'Processed Elastic IPs.'
    }

