#!/bin/bash

set -e

echo "Gunicorn süreçleri sonlandırılıyor..."
killall gunicorn || true

echo "Uygulama durduruldu."