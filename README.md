Set up aws account
- aws configure --profile duhnit
- AWS Access Key ID [None]: ...
- AWS Secret Access Key [None]: ...
- Default region name [None]: us-west-1
- Default output format [None]:

Verify AWS Account
- cat ~/.aws/credentials

Check if table already exists
- aws --profile=duhnit dynamodb describe-table --table-name=deeds

Consider deleting the table if already exists
- aws --profile=duhnit dynamodb delete-table --table-name=deeds

Create if table does not exist
- aws --profile=duhnit dynamodb create-table --cli-input-json file://duhn-it-create-table.json
