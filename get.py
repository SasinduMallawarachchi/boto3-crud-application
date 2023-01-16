import boto3
tableName = 'cricketCaptains_sm'

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
db = dynamodb.Table(tableName)

allCrickerters = db.scan()
print(allCrickerters)