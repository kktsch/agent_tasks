import json
import boto3
from typing import Optional
from config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    BEDROCK_MODEL_ID
)

class LLMHelper:
    """
    AWS Bedrock üzerinden LLM modellerine erişim sağlayan yardımcı sınıf
    """
    
    def __init__(self):
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        
    def get_response(self, prompt: str, temperature: float = 0.1) -> Optional[str]:
        """
        LLM modelinden yanıt al

        Args:
            prompt: Modele gönderilecek istek
            temperature: Yaratıcılık seviyesi (0.0-1.0)

        Returns:
            Optional[str]: Model yanıtı veya None (hata durumunda)
        """
        try:
            response = self.bedrock.invoke_model(
                modelId=BEDROCK_MODEL_ID,
                contentType='application/json',
                accept='application/json',
                body=json.dumps({
                    "prompt": prompt,
                    "max_gen_len": 512,
                    "temperature": temperature,
                    "top_p": 0.9
                })
            )
            
            response_body = json.loads(response['body'].read())
            return response_body['generation']
            
        except Exception as e:
            print(f"LLM Hatası: {str(e)}")
            return None
        
if __name__ == "__main__":
    # Test kullanımı
    llm = LLMHelper()
    
    test_prompts = [
        "Merhaba, nasılsın?",
        "Python nedir?",
        "2+2 kaç eder?"
    ]
    
    print("LLM Test Sonuçları:")
    print("-" * 50)
    
    for prompt in test_prompts:
        print(f"\nSoru: {prompt}")
        response = llm.get_response(prompt)
        print(f"Yanıt: {response}")
        print("-" * 50)