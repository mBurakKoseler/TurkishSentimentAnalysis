import string

# Text dosyasını okuma fonksiyonu
def process_text_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        # Dosyayı okuma
        text = file.read()

    # Tüm harfleri küçük harfe dönüştürme
    text = text.lower()

    # Noktalama işaretlerini kaldırma
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Yeni dosyaya yazma
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Örnek kullanım
input_file = 'CallCenterExampleSentences.txt'   # Girdi dosyanın adı
output_file = 'islenmisVeriSeti.txt'  # İşlenmiş çıktıyı kaydedeceğin dosyanın adı
process_text_file(input_file, output_file)
