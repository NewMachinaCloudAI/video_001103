import json
from boto3 import Session
from botocore.exceptions import ClientError


def detect_sentiment(text, language_code):
    
    # setup session and clientObject
    session = Session(region_name="us-east-1")
    comprehend_client = session.client("comprehend")
    sentiment = "Couldn't detect sentiment"
    
    try:
        response = comprehend_client.detect_sentiment( Text=text, LanguageCode=language_code )
        sentiment = response["Sentiment"]
    except ClientError:
        print("Client error!")
        
    # return sentiment
    return sentiment


def lambda_handler(event, context):
    
    # detect sentiment
    sentiment = detect_sentiment("Hey you did a really awesome job... keep it up!","en")
    print("Detected primary sentiment %s.", sentiment )
    
    # return status
    return{
        'statusCode': 200,
        'body': json.dumps('Successful Lambda integration with Comprehend!')
    }
