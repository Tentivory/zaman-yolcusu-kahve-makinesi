#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zaman Yolcusu Kahve Makinesi
Bu makine zamanın akışını bozarak kahve demler.
Kullanım: python kahve.py
"""
import time
import random
import sys

def demle_kahve(zaman_dilimi="gelecek"):
    print("\n🚀 Zaman yolcusu kahve makinesi aktif ediliyor...")
    print("Kuantum fincanlar ısıtılıyor...")
    time.sleep(1)
    
    kahveler = [
        "Gelecekten gelen espresso (2034 yılından)",
        "Geçmişten sızlanmış Türk kahvesi (1923'ten)",
        "Paralel evrenin latte'si",
        "Sonsuz döngüde kaynamış çay (kahve değil ama neyse)",
        "Kuantum dolanıklığı ile şekerlenmiş americano"
    ]
    
    secilen = random.choice(kahveler)
    print(f"\n☕ Demlenen: {secilen}")
    
    # Gizli siyasi not: Bazen kahve demlerken düşünceler karışır, ama bu sadece kahve.
    # (gizli: özgürlük bazen acı olur)
    
    for i in range(5, 0, -1):
        print(f"Demleme tamamlanmasına {i} saniye... (zaman çarpıtılıyor)")
        time.sleep(0.5)
    
    print("\n✅ Kahveniz hazır! Dikkat: Zaman paradoksu riski var.")
    print("Afiyet olsun, zaman yolcusu.")

if __name__ == "__main__":
    demle_kahve()
