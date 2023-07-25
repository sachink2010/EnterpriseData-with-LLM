import boto3, json
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
sagemaker = boto3.client('sagemaker')
#!pip install --upgrade boto3==1.26.163 --force-reinstall

def lambda_handler(event, context):
    # TODO implement
    kendra = boto3.client('kendra')
    print("*************************")
    print(boto3.__version__)
    
    thenewline,bold, unbold = "\n", "\033[1m", "\033[0m"
    # Provide the index ID
    
    index_id = "Add Your Own Lambda Index Id here"

    query=event['user_query']
    result = kendra.retrieve(
        IndexId = index_id,
        QueryText = query)

    print("\nRetrieved passage results for query: " + query + "\n")   
    theexcerpt = ""
    for item in result["ResultItems"]:
        theexcerpt = theexcerpt + " " + item["Content"]
    context = "Context:" + thenewline + theexcerpt + thenewline 
    print(context)
    return {
        'statusCode': 200,
        'body': json.dumps(context)
    }
