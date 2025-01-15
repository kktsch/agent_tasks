# Finansal Analiz Araçları

Bu repo, finansal hesaplamalar ve analizler için iki ayrı araç içerir:

## Görev 1: LLM Destekli Bileşik Faiz Hesaplayıcı

LLaMA modelini kullanarak doğal dil ile sorulan bileşik faiz sorularını anlayan ve hesaplayan bir sistem:
- Bileşik faiz ile ilgili doğal dil sorularını anlar
- Güvenli hesaplama altyapısı kullanır
- Hassas sonuçlar verir

Örnek:
```python
"Aylık %3 faizle 9 ayda ne kadar getiri olur?"
```

## Görev 2: Metal Fiyat Performans Analizi

Belirli bir yıl için altın ve gümüş fiyatlarının performansını karşılaştıran bir araç:

- Tavily AI ile gerçek piyasa verilerini arar
- LLaMA modeli ile bilgiyi işler
- Net karşılaştırma sonuçları sunar

Örnek:
```python
"2023'te altın mı gümüş mü daha çok kazandırdı?"
```

## Kurulum

1. Repo'yu klonlayın
2. Sanal ortam oluşturun:

```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
```

3. Bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

4. Çalıştırın
```bash
python src/main.py
```