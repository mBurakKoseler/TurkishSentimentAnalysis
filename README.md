**Bu proje ilk aşamada Türkçe duygu analizi alanında iki farklı modelin performansını değerlendirmeyi ve bu modellerin çağrı merkezi gibi birimlerde kullanım uygunluğunu belirlemeyi hedeflemektedir.**

İncelenen duygu analizi modelleri arasında, bu amaca uygun ve başarılı olarak seçilen modeller şunlardır:

savasy/bert-base-turkish-sentiment-cased (https://huggingface.co/savasy/bert-base-turkish-sentiment-cased)
saribasmetehan/bert-base-turkish-sentiment-analysis (https://huggingface.co/saribasmetehan/bert-base-turkish-sentiment-analysis)

Yukarıda belirtilen modeller, duygu analizi çalışmalarında kullanılmak üzere seçilmiştir. Çalışmaları için bu iki yazılımcıya teşekkür ederiz.

**Modellerden biri yalnızca olumlu ve olumsuz etiketlendirme yaparken, diğeri olumlu, olumsuz ve nötr etiketlendirme gerçekleştirmektedir.** Hangi modelin çağrı merkezleri için daha uygun olduğunu belirlemek amacıyla, **model başarıları 100 cümlelik bir veri seti ile test edilmiştir.** Bu test cümleleri, çağrı merkezleriyle yapılan konuşmalarda kullanılabilecek olumlu, olumsuz ve nötr cümlelerden seçilmiş ve sonuçları karşılaştırılabilir hale getirmek için  tablolaştırılmıştır.

Sonrasında, modellerin etiketlendirme sürelerinin ölçülmesi amacıyla farklı boyutlarda cümleler içeren setler ile testler gerçekleştirilmiştir. Bu kapsamda **10 uzun/kısa cümle, 100 karışık cümle ve 1 uzun/kısa cümle üzerinden hız karşılaştırmaları yapılmış** ve sonuçlar zaman etiketleri ile tespit edilmiştir. Elde edilen sonuçlar ve ilgili kodlar projeye eklenmiştir.


![timeComprasion](https://github.com/user-attachments/assets/f8b84847-d3cf-4d47-9c16-90c00f8da770)
