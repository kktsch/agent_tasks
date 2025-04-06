import os
from dotenv import load_dotenv

# AWS Configuration
AWS_ACCESS_KEY_ID = "AKIA5LDZXN5MAOOKL4NJ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_REGION = "us-west-2"
BEDROCK_MODEL_ID = "meta.llama3-1-70b-instruct-v1:0"

# Tavily Configuration
TAVILY_API_KEY = "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"

def validate_config():
    """Gerekli environment variable'ların varlığını kontrol et"""
    if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, TAVILY_API_KEY]):
        raise ValueError("Eksik environment variable'lar.")
