import argparse
import boto3
from botocore import UNSIGNED
from botocore.client import Config
from warrant.aws_srp import AWSSRP

argp = argparse.ArgumentParser(description='Get a IdToken JWT by providing a Cognito Userpool, a Client ID, username and password')

argp.add_argument('-u', '--username', required=True, help='Cognito Userpool username')
argp.add_argument('-p', '--password', required=True, help='Cognito Userpool password')
argp.add_argument('-i', '--user-pool-id', required=True, help='Cognito Userpool ID')
argp.add_argument('-c', '--client-id', required=True, help='Cognito Userpool Client ID')
argp.add_argument('-s', '--client-secret', required=False, help='Cognito Userpool Client secret')
args=argp.parse_args()

boto_client = boto3.client('cognito-idp', config=Config(region_name=args.user_pool_id.split('_')[0], signature_version=UNSIGNED))
aws = AWSSRP(username=args.username, password=args.password, pool_id=args.user_pool_id,
             client_id=args.client_id, client_secret=args.client_secret, client=boto_client)
tokens = aws.authenticate_user()

id_token = tokens['AuthenticationResult']['IdToken']
print(id_token)
