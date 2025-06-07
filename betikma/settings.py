import os
from pathlib import Path
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

# === Temel Ayarlar ===
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'dev-secret-key')
DEBUG = False

ALLOWED_HOSTS = ["www.betikma.com"]

# === Uygulamalar ===
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Üçüncü parti
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Dahili
    'core',
	'editor',
]

SITE_ID = 1

# === Allauth Ayarları ===
# Kullanıcıların e-posta ve parola ile giriş yapmasını sağlar.
ACCOUNT_LOGIN_METHODS = ['email']

# E-posta adresinin kayıt sırasında zorunlu olmasını ve kullanıcı adı gerektirmemesini sağlar.
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory' ayarı, kayıt sırasında e-posta doğrulaması için
# bir kod/bağlantı gönderilmesini gerektirdiğinden 'email*' kullanıldı.
ACCOUNT_SIGNUP_FIELDS = ['email*']

# E-posta doğrulamayı zorunlu kılar. Kayıt olduktan sonra kullanıcıya doğrulama e-postası gönderilir.
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# Başarısız giriş denemeleri için oran sınırlaması.
ACCOUNT_RATE_LIMITS = {
    'login_failed': '5/5m', # 5 dakikada 5 başarısız giriş denemesi
}

# Kod ile parola olmadan girişi devre dışı bırakır.
# Bu, kullanıcıların normalde parola ile giriş yapmasını sağlar.
ACCOUNT_LOGIN_BY_CODE_ENABLED = False # FALSE olarak değiştirildi
ACCOUNT_LOGIN_BY_CODE_EXPIRATION = 300 # Bu ayar artık kullanılmayacak ama bırakıldı
ACCOUNT_LOGIN_BY_CODE_MAX_ATTEMPTS = 5 # Bu ayar artık kullanılmayacak ama bırakıldı
ACCOUNT_LOGIN_BY_CODE_THROTTLE_SECONDS = 60 # Bu ayar artık kullanılmayacak ama bırakıldı


# === E-posta ===
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kristalsoft.info@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv("SMTP_PASSWORD") # Burayı kendi şifrenizle doldurmalısınız


# === Giriş / Çıkış ===
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# === Şablon Ayarları ===
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# === Middleware ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'betikma.urls'
WSGI_APPLICATION = 'betikma.wsgi.application'

# === Veritabanı ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# === Parola Politikası ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
]

# === Dil & Zaman ===
LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_TZ = True

# === Statik & Medya ===
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = '/srv/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/srv/media'

# === Güvenlik ===
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

JAZZMIN_SETTINGS = {
    # Genel Ayarlar
    "site_title": "Betikma Yönetim Paneli",  # Tarayıcı sekmesinde görünen başlık
    "site_header": "Betikma Administration",         # Admin panelinin üst kısmındaki başlık
    "site_brand": "KristalSoft Yazılım",              # Admin panelinin sol üst kısmındaki marka adı
    "site_logo": "logo2.png",          # Sol üst köşedeki logo yolu (STATIC_URL'ye göre)
    "login_logo": "logo2.png",   # Giriş sayfasındaki logo yolu
    "login_logo_dark": None,              # Koyu mod giriş sayfası logosu
    "site_logo_classes": "img-circle",    # Logo için CSS sınıfları (örn: "img-circle", "img-square")
    "welcome_sign": "Betikma Yönetim Paneline Hoş Geldiniz!", # Giriş sayfasındaki hoş geldiniz mesajı
    "copyright": "KristalSoft Yazılım", # Alt bilgi telif hakkı metni
    "search_model": ["auth.User", "auth.Group"], # Arama çubuğunda aranacak modeller
    
    # UI Ayarları
    "show_sidebar": True,                 # Kenar çubuğunu göster/gizle
    "navigation_expanded": True,          # Kenar çubuğu varsayılan olarak genişletilmiş mi?
    "hide_apps": [],                      # Belirli uygulamaları kenar çubuğunda gizle
    "hide_models": [],                    # Belirli modelleri kenar çubuğunda gizle
    "order_with_respect_to": ["auth"],    # Uygulama ve model sıralaması
    "default_dashboard_icon": "fas fa-tachometer-alt", # Varsayılan pano simgesi
    "default_icon_parents": "fas fa-chevron-circle-right", # Üst menü ögeleri için varsayılan simge
    "default_icon_children": "fas fa-circle", # Alt menü ögeleri için varsayılan simge
    
    # Renk Teması
    "theme": "united", # Kullanılabilir temalar:
                      # 'darkly', 'flatly', 'journal', 'litera', 'lumen', 'minty', 'pulse',
                      # 'sandstone', 'simplex', 'slate', 'solar', 'spacelab', 'united', 'yeti'
    "dark_mode_theme": "darkly", # Koyu mod için tema
    "actions_sticky_top": True,   # Eylem düğmelerini yukarıda sabit tut
    
    # Kullanıcı Arayüzü Ayarları (Kullanıcı Tarafından Ayarlanabilir)
    "show_ui_tunner": True,       # Sağ üst köşede UI ayarlayıcıyı göster
    "changeform_format": "horizontal_tabs", # Form formatı: "horizontal_tabs", "vertical_tabs", "single"
    "changeform_format_overrides": {"auth.user": "vertical_tabs"}, # Model bazında form formatı geçersiz kılma
    
    # Menü Ayarları
    "topmenu_links": [
        {"name": "Ana Sayfa", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Destek", "url": "https://kristalsoft.com.tr", "new_window": True},
        {"model": "auth.User"},
        {"app": "books"}
    ],
    "usermenu_links": [
        {"name": "Profilim", "url": "admin:auth_user_change", "icon": "fas fa-user"},
        {"name": "Ayarlar", "url": "#"},
    ],
    
    # Sidebar Menü Ayarları
    "sidebar_fixed": True, # Kenar çubuğunu sabit tut
    "sidebar_nav_compact": False, # Kompakt kenar çubuğu
    "sidebar_show_apk_icons": False, # Uygulama ve model simgelerini göster
    "sidebar_show_dashboards": False, # Özel panoları göster
    "sidebar_menu": [
        {"name": "Ana Sayfa", "url": "admin:index", "icon": "fas fa-home"},
        {"app": "auth"},
        {"model": "books.Book"},
        {"name": "Raporlar", "url": "/admin/reports/", "icon": "fas fa-chart-line"},
        {"separator": True},
        {"name": "Gelişmiş Ayarlar", "children": [
            {"name": "Loglar", "url": "/admin/logentries/", "icon": "fas fa-history"},
            {"name": "API Dokümantasyonu", "url": "/swagger/", "new_window": True},
        ]},
    ],
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True