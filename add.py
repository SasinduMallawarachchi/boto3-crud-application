import boto3
tableName = 'cricketCaptains_sm'

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
db = dynamodb.Table(tableName)

#add items to the table
item1 = db.put_item(
    Item={
        'full_name': 'Aravinda de Silva',
        'year_od_start': 1992,
        'odi_runs': 9284,
        'odi_runs_average': 34,
        'win_precentage_%':27
        }
    )
print(item1)

item2 = db.put_item(
    Item={
        'full_name': 'Sanath Jayasuriya',
        'year_od_start': 1998,
        'odi_runs':13430 ,
        'odi_runs_average':40 ,
        'win_precentage_%':55
        }
    )
print(item2)

item3 = db.put_item(
    Item={
        'full_name': 'Marvan Atapattu',
        'year_od_start': 2001,
        'odi_runs': 8529,
        'odi_runs_average': 37,
        'win_precentage_%':55
        }
    )
print(item3)

item4 = db.put_item(
    Item={
        'full_name': 'Mahela Jayawardene',
        'year_od_start': 2001,
        'odi_runs': 12650,
        'odi_runs_average': 33,
        'win_precentage_%':49
        }
    )
print(item4)

# item5 = db.put_item(
#     Item={
#         'full_name': 'Dasun Shanaka',
#         'year_od_start': 2019,
#         'odi_runs': 1067,
#         'odi_runs_average': 28,
#         'win_precentage_%':46
#         }
#     )
  
item5 = db.put_item(
    Item={
        'full_name': 'Dasun Shanaka',
        'year_od_start': 2019,
        'odi_runs': 1067,
        'odi_runs_average': 28,
        'win_precentage_%':46
        }
    )
print(item5)