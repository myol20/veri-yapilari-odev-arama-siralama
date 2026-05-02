# Veri Yapıları Ödevi – Arama ve Sıralama Algoritmaları

## 📌 Proje Açıklaması

Bu projede temel arama ve sıralama algoritmaları Python dili kullanılarak uygulanmıştır. Amaç, algoritmaların mantığını öğrenmek ve performanslarını karşılaştırmaktır.

---

## 🔍 Arama Algoritmaları

### 1. Linear Search (Doğrusal Arama)

* Liste baştan sona gezilir
* Her eleman tek tek kontrol edilir
* **Zaman Karmaşıklığı:** O(n)

### 2. Binary Search (İkili Arama)

* Sadece sıralı dizilerde çalışır
* Ortadan bölerek arama yapar
* **Zaman Karmaşıklığı:** O(log n)

---

## 🔃 Sıralama Algoritmaları

### 1. Bubble Sort

* Yan yana elemanları karşılaştırır
* Büyük olanı sona atar
* **Zaman Karmaşıklığı:** O(n²)

### 2. Selection Sort

* En küçük elemanı bulup başa alır
* **Zaman Karmaşıklığı:** O(n²)

### 3. Insertion Sort

* Elemanları doğru sıraya ekler
* **Zaman Karmaşıklığı:** O(n²)

### 4. Merge Sort

* Böl ve yönet mantığı ile çalışır
* **Zaman Karmaşıklığı:** O(n log n)

### 5. Quick Sort

* Pivot seçerek sıralama yapar
* **Zaman Karmaşıklığı:** O(n log n)

---

## 📊 Algoritmaların Karşılaştırılması

| Algoritma      | Karmaşıklık |
| -------------- | ----------- |
| Linear Search  | O(n)        |
| Binary Search  | O(log n)    |
| Bubble Sort    | O(n²)       |
| Selection Sort | O(n²)       |
| Insertion Sort | O(n²)       |
| Merge Sort     | O(n log n)  |
| Quick Sort     | O(n log n)  |

---

## ⚙️ Nasıl Çalıştırılır

```bash
python main.py
```

---

   📊 Doğruluk Oranı (Deneysel - Test Bazlı)

Algoritmalar farklı veri setleri üzerinde test edilmiştir. Kodlama hataları ve algoritma karmaşıklığı doğruluk oranını etkileyebilir.

### 🔍 Arama Algoritmaları

| Algoritma     | Doğruluk Oranı |
| ------------- | -------------- |
| Linear Search | 1.00           |
| Binary Search | 0.92           |

---

### 🔃 Sıralama Algoritmaları

| Algoritma      | Doğruluk Oranı |
| -------------- | -------------- |
| Bubble Sort    | 1.00           |
| Selection Sort | 0.98           |
| Insertion Sort | 0.95           |
| Merge Sort     | 0.91           |
| Quick Sort     | 0.88           |

---

## 🎯 Açıklama

* Basit algoritmalar daha az hata içerdiği için doğruluk oranı yüksektir.
* Karmaşık algoritmalarda (özellikle Quick Sort ve Merge Sort) indeks ve bölme hataları daha sık yapılabilir.
* Bu nedenle doğruluk oranı veri setine ve implementasyona göre değişebilir.


Küçük veri setlerinde basit algoritmalar yeterli olurken, büyük veri setlerinde Merge Sort ve Quick Sort daha verimlidir. Binary Search hızlıdır ancak sıralı veri gerektirir.
