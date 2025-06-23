from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_secret():
    secret_name = "pgagi-api-key-new"
    region_name = os.getenv("AWS_REGION", "ap-south-1")

    print(f"Fetching secret from Secrets Manager: {secret_name} in {region_name}")

    client = boto3.client("secretsmanager", region_name=region_name)

    try:
        response = client.get_secret_value(SecretId=secret_name)
        secret = response['SecretString']
        print("Secret fetched:", secret)
        return json.loads(secret)
    except Exception as e:
        print("Error fetching secret:", str(e))
        return {}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "message": "Backend is running successfully"}

@app.get("/api/message")
async def get_message():
    secret_data = get_secret()
    print("Secret data:", secret_data)  # Log for debugging

    api_key = secret_data.get("key", "No key found")
    return {
        "message": "You've successfully integrated the backend!",
        "secret_key": api_key
    }