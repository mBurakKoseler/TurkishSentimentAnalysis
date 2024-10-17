import json
from transformers import pipeline

# Duygu analizi modeli
pipe_model = pipeline("text-classification", model="saribasmetehan/bert-base-turkish-sentiment-analysis")

# JSON dosyasını oku
with open('dialog10.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Müşteri cümlelerini ve diğer bilgileri güncelle
for entry in data['dialog']:
    if entry['speaker'] == "Müşteri":
        # Duygu analizi yap
        prediction = pipe_model(entry['sentence'])[0]
        label = prediction['label']
        score = round(prediction['score'], 2)  # Skoru iki ondalık basamağa yuvarla

        # Model etiketlerini daha rahat yorumlamak için dönüştürme
        if label == "LABEL_1":
            detected_emotion = "Olumlu"
        elif label == "LABEL_2":
            detected_emotion = "Olumsuz"
        elif label == "LABEL_0":
            detected_emotion = "Nötr"

        # Yeni alanları ekle
        entry['detectedEmotion'] = detected_emotion
        entry['score'] = score

# Yeni JSON dosyasını kaydet
with open('dialog10_duyguAnalizi.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Duygu analizi sonuçları yeni JSON dosyasına eklendi.")
