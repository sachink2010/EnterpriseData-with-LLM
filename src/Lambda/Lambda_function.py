import boto3, json
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#sagemaker = boto3.client("sagemaker")
#!pip install --upgrade boto3==1.26.163 --force-reinstall

def lambda_handler(event, context):

    kendra = boto3.client("kendra")
    print("*************************")
    print(boto3.__version__)
    
    thenewline,bold, unbold = "\n", "\033[1m", "\033[0m"
    # Provide the index ID
    
    if "kendra_index_id" not in event or "user_query" not in event or "language" not in event:
        logging.info("## Received request without a kendra_index_id, user_query or language")
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Bad request"}),
        }
    
    kendra_index_id = event["kendra_index_id"]
    user_query = event["user_query"]
    language = event["language"]
    
    result = kendra.retrieve(
        IndexId = kendra_index_id,
        QueryText = user_query,
        AttributeFilter = {
        "EqualsTo": {      
            "Key": "_language_code",
            "Value": {
                "StringValue": language
                }
            }
        })

    print("\nRetrieved passage results for query: " + user_query + "\n")   
    theexcerpt = ""
    for item in result["ResultItems"]:
        theexcerpt = theexcerpt + thenewline + item["Content"]
#    context = "Context:" + thenewline + theexcerpt + thenewline 
    context = theexcerpt 
    print(context)
    return {
        "statusCode": 200,
        "body": json.dumps(context)
    }
