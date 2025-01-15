import requests
from typing import Optional, Dict, Tuple
from datetime import datetime
from llm_helper import LLMHelper
from config import TAVILY_API_KEY

class MetalPriceAnalyzer:
   def __init__(self):
       self.llm = LLMHelper()
       self.tavily_url = "https://api.tavily.com/search"
       
   def get_metal_price_data(self, metal: str, year: str) -> Optional[dict]:
        
        headers = {
            "Authorization": f"Bearer {TAVILY_API_KEY}",
            "Content-Type": "application/json"  # Content type eklendi
        }
        
        data = {
            "query": f"{metal} price performance {year}",
            "include_answer": True
        }
        
        try:            
            response = requests.post(
                self.tavily_url,
                headers=headers, 
                json=data
            )
                        
            return response.json()
            
        except Exception as e:
            print(f"HATA - {metal} verisi çekerken: {str(e)}")
            return None

   def get_both_metals_data(self, year: str) -> Tuple[Optional[dict], Optional[dict]]:
       print("\nİki metal için veri çekiliyor")
       
       gold_data = self.get_metal_price_data("gold", year)
       print(f"Altın verisi alındı: {bool(gold_data)}")
       
       silver_data = self.get_metal_price_data("silver", year)
       print(f"Gümüş verisi alındı: {bool(silver_data)}")
       
       return gold_data, silver_data

   def analyze(self, year: str = None) -> Optional[str]:
       if year is None:
           year = str(datetime.now().year)
                  
       gold_data, silver_data = self.get_both_metals_data(year)
       
       if not gold_data or not silver_data:
           print("Veri eksik, analiz yapılamıyor")
           return "Veri alınamadı."
                  
       prompt = f"""Aşağıdaki verilere bakarak {year} için altın ve gümüş fiyat analizini yap.

       Altın verileri:
       {gold_data['answer']}

       Gümüş verileri:
       {silver_data['answer']}
       
       Yanıtını Türkçe ver.
       """
       
       
       result = self.llm.get_response(prompt)
       print(f"\nLLM yanıtı: {result}")
       
       return result


if __name__ == "__main__":
   print("Program başlatılıyor...")
   
   analyzer = MetalPriceAnalyzer()
   test_years = ["2023", "2022"]
   
   print("\nMetal Performans Analizi Testi:")
   print("-" * 50)
   
   for year in test_years:
       print(f"\nYıl: {year} için test başlıyor")
       result = analyzer.analyze(year)
       print(f"Final Sonuç: {result}")
       print("-" * 50)