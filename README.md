# 🇹🇷 Turkish Sentiment Analysis with BERT

Bu proje, **Türkçe duygu analizi** alanında iki farklı BERT tabanlı modelin performansını değerlendirmeyi ve bu modellerin çağrı merkezi gibi uygulama alanlarında ne kadar uygun olduğunu araştırmayı amaçlamaktadır.

## 🎯 Proje Amacı

- Türkçe diline özel duygu analizi modellerini test etmek
- Olumlu, olumsuz ve nötr cümleleri doğru sınıflandırma performanslarını ölçmek
- Çağrı merkezlerinde kullanılabilecek en uygun modeli belirlemek
- Modellerin hız ve etiketlendirme süresi karşılaştırmasını yapmak

## 🤖 Kullanılan Modeller

| Model | Açıklama | Etiketler |
|-------|----------|-----------|
| [`savasy/bert-base-turkish-sentiment-cased`](https://huggingface.co/savasy/bert-base-turkish-sentiment-cased) | Türkçe metinler için eğitilmiş BERT tabanlı model | Olumlu, Olumsuz |
| [`saribasmetehan/bert-base-turkish-sentiment-analysis`](https://huggingface.co/saribasmetehan/bert-base-turkish-sentiment-analysis) | Çok sınıflı duygu analizi modeli | Olumlu, Olumsuz, Nötr |

> Bu modelleri paylaşan geliştiricilere teşekkür ederiz 🙏

## 🧪 Test Süreci

Modeller, aşağıdaki şekilde test edilmiştir:

- 📋 **100 cümlelik test seti**: Gerçek çağrı merkezi konuşmalarını yansıtan olumlu, olumsuz ve nötr cümlelerden oluşur,
- 🕒 **Performans ölçümü**:
  - 10 kısa/uzun cümle
  - 100 karışık cümle
  - 1 uzun cümle / 1 kısa cümle
- Sonuçlar hem **doğruluk** hem de **etiketlendirme süresi (inference time)** açısından karşılaştırılmıştır.

## 📈 Sonuçlardan Örnek

```text
Model A - 100 cümlelik test süresi: 2.13 saniye
Model B - 100 cümlelik test süresi: 1.85 saniye

Doğruluk Oranı:
Model A: %86
Model B: %91
