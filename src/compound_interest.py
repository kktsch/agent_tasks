from typing import Optional
from calculator import Calculator
from llm_helper import LLMHelper

class CompoundInterestAgent:
    """
    Bileşik faiz hesaplamalarını LLM ile yapan sınıf
    """
    
    def __init__(self):
        self.llm = LLMHelper()
        self.calculator = Calculator()
        
    def calculate(self, user_question: str) -> Optional[str]:
        """
        Doğal dil sorusunu anlayıp bileşik faiz hesaplar

        Args:
            user_question: Örn: "aylık %3 faizle 9 ayda ne kadar getiri olur?"
        """
        system_prompt = """Bir finansal hesaplama asistanısın. Verilen girdiler için hesap makinesi kullanman gerekiyor.

        Kullanacağın hesap makinesi fonksiyonunun docstringi:
        ---
       Matematik ifadesini güvenli şekilde hesapla.
       
       Parametreler:
           ifade (str): Hesaplanacak matematik ifadesi (+, -, *, /, ^, parantez destekler)
           
       Dönüş:
           Optional[Decimal]: Hesaplama sonucu veya hata durumunda None
           
       Örnekler:
           >>> hm = HesapMakinesi()
           >>> hm.hesapla("2 + 2")     # Basit toplama
           >>> hm.hesapla("2 ^ 3")     # Üs alma
           >>> hm.hesapla("(4 + 5)/3") # Parantez ve bölme
       ---
        
        
        1. SADECE "Hesaplıyorum:" yaz
        2. Yeni satırda "HESAP:" yazıp formülü yukarıdaki kurallara uygun yaz
        3. Başka bilgi verme
        """
        
        try:
            response = self.llm.get_response(f"{system_prompt}\n\nİnsan: {user_question}\nAsistan:")
            print(response)
            
            if response:
                for line in response.split('\n'):
                    if line.strip().startswith('HESAP:'):
                        expression = line.replace('HESAP:', '').strip()
                        result = self.calculator.evaluate(expression)
                        if result:
                            return f"Sonuç: %{result}"
            
            return "Hesaplama yapılamadı."
            
        except Exception as e:
            print(f"Hesaplama hatası: {str(e)}")
            return None


if __name__ == "__main__":
    # Test kullanımı
    agent = CompoundInterestAgent()
    
    test_questions = [
        "aylık %3 faizle 9 ayda ne kadar getiri olur?",
        "yıllık %12 faiz 6 ayda ne getirir?",
        "aylık %2.5 faizle 1 yılda ne kazanırım?"
    ]
    
    print("Bileşik Faiz Hesaplama Testi:")
    print("-" * 50)
    
    for question in test_questions:
        print(f"\nSoru: {question}")
        result = agent.calculate(question)
        print(result)
        print("-" * 50)