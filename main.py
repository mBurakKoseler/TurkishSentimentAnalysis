import pandas as pd
from transformers import pipeline

# İlk model
pipe_model_1 = pipeline("text-classification", model="saribasmetehan/bert-base-turkish-sentiment-analysis")
# İkinci model
pipe_model_2 = pipeline("text-classification", model="savasy/bert-base-turkish-sentiment-cased")

# Cümleleri bir dosyadan oku
with open('islenmisVeriSeti.txt', 'r', encoding='utf-8') as file:
    test_sentences = [line.strip() for line in file if line.strip()]

# Sonuçları saklamak için bir liste
results = []

# Her cümleyi test et
for sentence in test_sentences:
    # Birinci modelin tahmini
    prediction_1 = pipe_model_1(sentence)[0]
    label_1 = prediction_1['label']
    score_1 = round(prediction_1['score'], 2)  # Skoru iki ondalık basamağa yuvarla

    # İkinci modelin tahmini
    prediction_2 = pipe_model_2(sentence)[0]
    label_2 = prediction_2['label']
    score_2 = round(prediction_2['score'], 2)  # Skoru iki ondalık basamağa yuvarla

    # model1 etiketlerini daha rahta yorumlamak için dönüştürme
    if label_1 == "LABEL_1":
        label_1 = "Positive"
    elif label_1 == "LABEL_2":
        label_1 = "Negative"
    elif label_1 == "LABEL_0":
        label_1 = "Notr"

    # Sonuçları listeye ekle
    results.append([sentence, label_1, score_1, label_2, score_2])

# Sonuçları pandas DataFrame'e dönüştür
df = pd.DataFrame(results, columns=["Sentence", "Model 1 Label", "Model 1 Score", "Model 2 Label", "Model 2 Score"])
# DataFrame'i noktalı virgül ayırıcı ile CSV dosyasına kaydet
df.to_csv('cleaned_model_comparison_results.csv', index=False, sep=';', encoding='utf-8-sig')
