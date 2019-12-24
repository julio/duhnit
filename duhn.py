import sys
import boto3
import datetime
import uuid

class DuhnIt:
    def __init__(self, email):
        boto3.setup_default_session(profile_name='duhnit')
        dynamodb = boto3.resource('dynamodb')
        self.deeds_table = dynamodb.Table('deeds')
        self.email = email

    def add_deed(self, deed):
        self.deeds_table.put_item(Item={
            "author-email": self.email,
            "deed-type": "work-{uuid}".format(uuid=uuid.uuid4()),
            "deed": deed,
            "done-at": str(datetime.datetime.now()),
            "detail":
                [
                    {
                    }
                ]
            }
        )

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('What have you dunh!?')
        exit(1)

    DuhnIt('julio@morgane.com').add_deed(sys.argv[1])