import boto3
import argparse
import os

def main(image_name):
    client = boto3.client('rekognition', region_name=os.environ['AWS_REGION'])

    with open(f'/app/data/{image_name}.JPEG', 'rb') as image_file:
        image_data = image_file.read()

    response = client.detect_labels(
        Image={'Bytes': image_data},
        MaxLabels=10,
        MinConfidence=80
    )

    labels = response['Labels']
    print('*' * 20)
    for label in labels:
        name = label['Name']
        confidence = label['Confidence']
        print(f'{name} ({confidence:.2f}%)')
    print('*' * 20)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='API calls to AWS Rekognition')
    parser.add_argument('arg1', type=str, help='image name')
    args = parser.parse_args()
    image_name = args.arg1
    main(image_name)