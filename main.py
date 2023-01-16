import boto3
tableName = 'cricketCaptains_sm'

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
db = dynamodb.Table(tableName)

#Table creation
table = dynamodb.create_table(
    TableName=tableName,
    KeySchema=[
        {
            'AttributeName': 'full_name', #partition key
            'KeyType': 'HASH' 
        },
        {
            'AttributeName': 'year_od_start', #hash key
            'KeyType': 'RANGE' 
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'full_name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'year_od_start',
            'AttributeType': 'N' 
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table status", table.table_status)

