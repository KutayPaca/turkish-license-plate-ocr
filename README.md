# Turkish License Plate OCR

Türk plaka görselleri üzerinde PaddleOCR tanıma modelini fine-tune etmek için
kullanılan veri hazırlama betiği ve model yapılandırmasıdır.

## Kurulum

1. PaddleOCR deposunu ayrı olarak klonlayın:

   ```powershell
   git clone https://github.com/PaddlePaddle/PaddleOCR.git
   ```

2. Bu depodaki `plate_dict.txt` ve `plate_rec.yml` dosyalarını PaddleOCR
   klasörüne kopyalayın.
3. Görselleri yerel olarak `dataset/plakalar/license-plates/` klasörüne koyun.
   Dataset dosyaları boyutları ve lisansları nedeniyle bu depoya dahil değildir.
4. PaddleOCR klasöründen veri listelerini oluşturun:

   ```powershell
   python prepare_data.py --image-dir ..\dataset\plakalar\license-plates
   ```

   Bu komut `train_list.txt` ve `val_list.txt` dosyalarını oluşturur. Bu
   dosyalar `.gitignore` tarafından dışlanır.

5. PaddleOCR'un resmi kurulum ve eğitim talimatlarını izleyerek
   `plate_rec.yml` yapılandırmasıyla eğitimi başlatın.

## Depoya dahil edilmeyenler

Yerel Python ortamı, dataset görselleri, indirilen ön-eğitimli modeller,
eğitim çıktıları ve üretilen label listeleri depoya gönderilmez.
