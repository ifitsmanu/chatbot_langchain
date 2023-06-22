import boto3


def create_dynamotable(databasename):
    session=boto3.Session()
    dynamodb=session.resource('dynamodb',region_name='us-east-1')
    try:
        dynamodb.create_table(
            TableName=databasename,
            KeySchema=[{"AttributeName": "SessionId", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "SessionId", "AttributeType": "S"}],
            BillingMode="PAY_PER_REQUEST",
        )
        session_table = dynamodb.Table(databasename)
        session_table.meta.client.get_waiter("table_exists").wait(TableName=databasename)
    except Exception as e:
        # print(e)
        print("{} already exists".format(databasename))


if __name__ == "__main__":
    #ask user for confirmation
    print("This will create the following tables in us-east-1 region:")
    print("1. SessionTable")
    print("2. SessionSummaryTable")
    answer = input("Do you want to continue? (y/n): ")
    if answer != "y":
        print("Aborting...")
        exit(0)
    create_dynamotable("SessionTable")
    create_dynamotable("SessionSummaryTable")


