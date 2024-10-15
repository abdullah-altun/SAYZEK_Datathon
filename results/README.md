<h2>Sonuçlar</h2>

<p>
1. Model eğitimi ham veri seti kullanılarak YOLOv8x modeli ile gerçekleştirilmiştir.<br>
2. Görüntüler, ESRGAN ile 1024x1024 çözünürlüğe yükseltilmiş ve YOLOv8x modeli varsayılan ayarlarda eğitilmiştir.<br>
3. Görüntüler, bicubic interpolasyon yöntemi ile 1024x1024 çözünürlüğe yükseltilmiş ve YOLOv8x modeli varsayılan ayarlarda eğitilmiştir.<br>
4. ESGAN ile elde edilen görüntüler model girdisini 1024x1024 olarak ayarlanarak eğitlmişitr<br>
5. bicubic ile elde edilen görüntüler ile model giridinisin 1024x1024 olarak ayaralanarak eğitilmiştir.<br>
6. Ana veri setinden sadece Silo görüntüleriyle eğitilen model (train7) <br>
7. Silo verisinin 1400 görüntüsünün eklenmesi (train8)<br>
8. Silo v1 ile eğitilmesi (train9)<br>
9. Ham bina verisi (train10)<br>
10. Toplam bina verisi (train11)<br>

11. Ham futbol sahasi verisi (train12)
12. Toplam Futbol sahasi verisi (train13)
</p>

<h3>Eğitim Sonuçları:</h3>

<p>
<strong>Eğitim-1:</strong> mAP50: 0.58, mAP50-95: 0.35<br>
<strong>Eğitim-2:</strong> mAP50: 0.58, mAP50-95: 0.38<br>
<strong>Eğitim-3:</strong> mAP50: 0.64, mAP50-95: 0.42<br>
<strong>Eğitim-4:</strong> mAP50: 0.58, mAP50-95: 0.39<br>
<strong>Eğitim-5:</strong> mAP50: 0.64, mAP50-95: 0.43<br>
<strong>Eğitim-6:</strong> mAP50: 0.89, mAP50-95: 0.71<br>
<strong>Eğitim-7:</strong> mAP50: 0.90, mAP50-95: 0.69<br>
<strong>Eğitim-8:</strong> mAP50: 0.91, mAP50-95: 0.69<br>

<strong>Eğitim-9:</strong> mAP50: 0.76, mAP50-95: 0.51<br>
<strong>Eğitim-10:</strong> mAP50: 0.79, mAP50-95: 0.53<br>

<strong>Eğitim-11:</strong> mAP50: 0.273, mAP50-95: 0.111<br>
<strong>Eğitim-12:</strong> mAP50: 0.995, mAP50-95: 0.869<br>

<strong>Eğitim-13:</strong> mAP50: 0.39, mAP50-95: 0.13<br>
<strong>Eğitim-14:</strong> mAP50: 0.41, mAP50-95: 0.13<br>
</p>

<p>
Ham veri seti ile eğitilen model, ESRGAN ile çözünürlüğü artırılmış ve aynı parametreler ile (640x640) eğitilmiş olmasına rağmen, hata matrisinde küçük bir iyileşme gözlenmiştir. Özellikle, bicubic interpolasyon ile çözünürlük artırıldığında sonuçlar ESRGAN kıyasla daha iyi olmuştur. Model parametreleri 1024 olarak ayarlandığında, iyileşme çok daha belirgin hale gelmiştir.
</p>

<p>
Ham veri setinde sadece Silo görüntü
</p>
