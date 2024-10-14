import time
from transformers import pipeline

# Modeli yükleyelim
pipe_model_2 = pipeline("text-classification", model="savasy/bert-base-turkish-sentiment-cased")

# Dosyalardan uzun, kısa ve 100 cümlelik metinleri okuyalım
with open("testSentences/10longSentences.txt", "r", encoding="utf-8") as file:
    long_sentences = [sentence.strip() for sentence in file.readlines()]

with open("testSentences/10shortSentences.txt", "r", encoding="utf-8") as file:
    short_sentences = [sentence.strip() for sentence in file.readlines()]

with open("testSentences/100mixSenteces.txt", "r", encoding="utf-8") as file:
    hundred_sentences = [sentence.strip() for sentence in file.readlines()]

# 1 uzun ve 1 kısa cümle için dosyadan okuma
with open("testSentences/1longSentence.txt", "r", encoding="utf-8") as file:
    one_long_sentence = file.readline().strip()

with open("testSentences/1shortSentence.txt", "r", encoding="utf-8") as file:
    one_short_sentence = file.readline().strip()

# Zaman ölçümü: 10 uzun cümle
start_time_long = time.time()
results_long = pipe_model_2(long_sentences)
end_time_long = time.time()

# Zaman ölçümü: 10 kısa cümle
start_time_short = time.time()
results_short = pipe_model_2(short_sentences)
end_time_short = time.time()

# Zaman ölçümü: 100 cümle
start_time_hundred = time.time()
results_hundred = pipe_model_2(hundred_sentences)
end_time_hundred = time.time()

# Zaman ölçümü: 1 uzun cümle
start_time_one_long = time.time()
result_one_long = pipe_model_2(one_long_sentence)
end_time_one_long = time.time()

# Zaman ölçümü: 1 kısa cümle
start_time_one_short = time.time()
result_one_short = pipe_model_2(one_short_sentence)
end_time_one_short = time.time()

# Toplam süreleri hesaplayalım
total_time_long = end_time_long - start_time_long
total_time_short = end_time_short - start_time_short
total_time_hundred = end_time_hundred - start_time_hundred
total_time_one_long = end_time_one_long - start_time_one_long
total_time_one_short = end_time_one_short - start_time_one_short

# 10 uzun cümlenin sonuçlarını yazdıralım
print("Results for 10 long sentences:")
for sentence, result in zip(long_sentences, results_long):
    print(f"Sentence: {sentence} -> Label: {result['label']}, Score: {result['score']:.4f}")

# 10 kısa cümlenin sonuçlarını yazdıralım
print("\nResults for 10 short sentences:")
for sentence, result in zip(short_sentences, results_short):
    print(f"Sentence: {sentence} -> Label: {result['label']}, Score: {result['score']:.4f}")

# 100 cümlenin sonuçlarını yazdıralım
print("\nResults for 100 sentences:")
for sentence, result in zip(hundred_sentences, results_hundred):
    print(f"Sentence: {sentence} -> Label: {result['label']}, Score: {result['score']:.4f}")

# 1 uzun cümlenin sonucunu yazdıralım
print("\nResult for 1 long sentence:")
print(f"Sentence: {one_long_sentence} -> Label: {result_one_long[0]['label']}, Score: {result_one_long[0]['score']:.4f}")

# 1 kısa cümlenin sonucunu yazdıralım
print("\nResult for 1 short sentence:")
print(f"Sentence: {one_short_sentence} -> Label: {result_one_short[0]['label']}, Score: {result_one_short[0]['score']:.4f}")

# Toplam süreleri yazdıralım
print(f"\nTotal time to label 10 long sentences: {total_time_long:.4f} seconds")
print(f"Total time to label 10 short sentences: {total_time_short:.4f} seconds")
print(f"Total time to label 100 sentences: {total_time_hundred:.4f} seconds")
print(f"Total time to label 1 long sentence: {total_time_one_long:.4f} seconds")
print(f"Total time to label 1 short sentence: {total_time_one_short:.4f} seconds")
