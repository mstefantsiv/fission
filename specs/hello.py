import boto3 as boto

def get_file_content_from_s3(bucket_name, file_key):
    """
    Retrieves a file from Amazon S3 and returns its content.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_key (str): The key (path) of the file in the S3 bucket.

    Returns:
        str: The content of the file.
    """
    # Set the LocalStack S3 endpoint URL
    endpoint_url = 'http://localhost:4566'

    # Create an S3 client
    s3 = boto.client('s3', endpoint_url=endpoint_url)

    # Retrieve the file object
    response = s3.get_object(Bucket=bucket_name, Key=file_key)

    # Read the content of the file
    content = response['Body'].read().decode('utf-8')

    return content


if __name__ == '__main__':
    bucket_name = 'your_bucket_name'
    file_key = 'path/to/your_file.txt'

    file_content = get_file_content_from_s3(bucket_name, file_key)

    print(file_content)
