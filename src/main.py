from compound_interest import CompoundInterestAgent
from metal_analyzer import MetalPriceAnalyzer

def show_menu():
   print("\n=== Finansal Analiz Araçları ===")
   print("1. Bileşik Faiz Hesaplayıcı")
   print("2. Metal Fiyat Performans Analizi")
   print("3. Çıkış")
   print("=" * 30)

def run_compound_interest():
   
   agent = CompoundInterestAgent()
   print("\n=== Bileşik Faiz Hesaplayıcı ===")
   print("Örnek soru: 'aylık %3 faizle 9 ayda ne kadar getiri olur?'")
   print("Çıkış için 'q' yazın")
   print("-" * 30)
   
   while True:
       question = input("\nSorunuz: ")
       if question.lower() == 'q':
           break
           
       result = agent.calculate(question)
       print(result)

def run_metal_analyzer():
   
   analyzer = MetalPriceAnalyzer()
   print("\n=== Metal Fiyat Performans Analizi ===")
   print("Hangi yılın analizi yapılsın?")
   print("Çıkış için 'q' yazın")
   print("-" * 30)
   
   while True:
       year = input("\nYıl: ")
       if year.lower() == 'q':
           break
           
       result = analyzer.analyze(year)
       print(f"\nSonuç: {result}")

def main():
   print("Finansal Analiz Araçları'na Hoş Geldiniz!")
   print("Bu program, yapay zeka destekli iki farklı finansal analiz aracı sunmaktadır.")
   
   while True:
       show_menu()
       choice = input("Seçiminiz (1-3): ")
       
       if choice == '1':
           run_compound_interest()
       elif choice == '2':
           run_metal_analyzer()
       elif choice == '3':
           print("\nProgram sonlandırılıyor... İyi günler!")
           break
       else:
           print("\nGeçersiz seçim! Lütfen tekrar deneyin.")

if __name__ == "__main__":
   try:
       main()
   except KeyboardInterrupt:
       print("\n\nProgram kullanıcı tarafından sonlandırıldı.")
   except Exception as e:
       print(f"\nBeklenmeyen bir hata oluştu: {str(e)}")