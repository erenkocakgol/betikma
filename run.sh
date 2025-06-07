#!/bin/bash

# Hata durumunda script'in durmasını sağlar
set -e

echo "Sanal ortam etkinleştiriliyor..."
source .venv/bin/activate

echo "Nginx yeniden başlatılıyor..."
sudo systemctl restart nginx

echo "Mevcut Gunicorn süreçleri sonlandırılıyor..."
killall gunicorn || true

echo "Gunicorn arka planda başlatılıyor..."
# nohup: Terminal kapatılsa bile sürecin çalışmaya devam etmesini sağlar.
# > gunicorn.log 2>&1: Gunicorn'ın tüm çıktılarını (hem standart hem de hata) gunicorn.log dosyasına yönlendirir.
# &: Komutu arka planda çalıştırır, böylece script hemen tamamlanır ve terminal serbest kalır.
nohup gunicorn -c gconfig.py > gunicorn.log 2>&1 &

echo "Gunicorn başlatıldı ve arka planda çalışıyor. Terminali kapatabilirsiniz."
echo "Çıktılar gunicorn.log dosyasında bulunabilir."