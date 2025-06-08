import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log the entire incoming event (user data)
    logger.info(f"Received user data: {json.dumps(event)}")
    
    # Optionally, you can extract some fields for clearer logs
    user_id = event.get("id", "unknown")
    first_name = event.get("first_name", "unknown")
    last_name = event.get("last_name", "unknown")
    
    logger.info(f"Processing user ID: {user_id}, Name: {first_name} {last_name}")
    
    # Return success or any other info if needed
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "User info logged"})
    }
