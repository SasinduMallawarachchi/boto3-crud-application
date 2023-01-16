import boto3
tableName = 'cricketCaptains_sm'

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
db = dynamodb.Table(tableName)

deletePlayer = db.delete_item(
        Key={
            'full_name': 'Sasindu',
            'year_od_start': 1998
        }
    )
    
print("Successfully deleted")    