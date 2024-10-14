<h2>Sonuçlar</h2>

<p>
1. Model eğitimi ham veri seti kullanılarak YOLOv8x modeli ile gerçekleştirilmiştir.<br>
2. Görüntüler, ESRGAN ile 1024x1024 çözünürlüğe yükseltilmiş ve YOLOv8x modeli varsayılan ayarlarda eğitilmiştir.<br>
3. Görüntüler, bicubic interpolasyon yöntemi ile 1024x1024 çözünürlüğe yükseltilmiş ve YOLOv8x modeli varsayılan ayarlarda eğitilmiştir.<br>
4. ESGAN ile elde edilen görüntüler model girdisini 1024x1024 olarak ayarlanarak eğitlmişitr<br>
5. bicubic ile elde edilen görüntüler ile model giridinisin 1024x1024 olarak ayaralanarak eğitilmiştir.
</p>

<h3>Eğitim Sonuçları:</h3>

<p>
<strong>Eğitim-1:</strong> mAP50: 0.58, mAP50-95: 0.35<br>
<strong>Eğitim-2:</strong> mAP50: 0.58, mAP50-95: 0.38<br>
<strong>Eğitim-3:</strong> mAP50: 0.64, mAP50-95: 0.42<br>
<strong>Eğitim-4:</strong> mAP50: 0.58, mAP50-95: 0.39<br>
<strong>Eğitim-5:</strong> mAP50: 0.64, mAP50-95: 0.43<br>
</p>

<p>
Ham veri seti ile eğitilen model, ESRGAN ile çözünürlüğü artırılmış ve aynı parametreler ile (640x640) eğitilmiş olmasına rağmen, hata matrisinde küçük bir iyileşme gözlenmiştir. Özellikle, bicubic interpolasyon ile çözünürlük artırıldığında sonuçlar ESRGAN kıyasla daha iyi olmuştur. Model parametreleri 1024 olarak ayarlandığında, iyileşme çok daha belirgin hale gelmiştir.
</p>
