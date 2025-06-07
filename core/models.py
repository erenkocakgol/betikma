# core/models.py
from django.db import models

class AboutPageContent(models.Model):
    """
    Betikma'nın 'Hakkımızda' sayfasının dinamik içeriğini tutan model.
    Bu modeldeki alanlar, admin panelinden düzenlenebilir olacak.
    """
    # Genel Bilgiler
    page_title = models.CharField(
        max_length=200,
        default="Betikma Hakkında",
        verbose_name="Sayfa Başlığı"
    )
    page_description = models.TextField(
        default="Yapay zeka gücüyle metinlerinizi dönüştüren, yaratıcı ve verimli bir platform.",
        verbose_name="Sayfa Açıklaması"
    )

    # Misyon Bölümü
    mission_title = models.CharField(
        max_length=100,
        default="Misyonumuz",
        verbose_name="Misyon Başlığı"
    )
    mission_text = models.TextField(
        default="Betikma olarak misyonumuz, yapay zekanın gücünü herkesin erişebileceği bir araç haline getirmek. Kullanıcılarımızın, metinlerini kolayca yeniden yazmalarına, geliştirmelerine ve yaratıcı potansiyellerini tam anlamıyla ortaya çıkarmalarına yardımcı oluyoruz. Dilin karmaşıklığını basitleştirerek, iletişimi daha etkili ve keyifli hale getirmeyi hedefliyoruz. Herkesin daha iyi metinler yazabilmesi için yenilikçi çözümler sunmaya, kullanıcı deneyimini sürekli iyileştirmeye ve yapay zeka teknolojilerini etik ve sorumlu bir şekilde kullanmaya kararlıyız.",
        verbose_name="Misyon Metni"
    )

    # Vizyon Bölümü
    vision_title = models.CharField(
        max_length=100,
        default="Vizyonumuz",
        verbose_name="Vizyon Başlığı"
    )
    vision_text = models.TextField(
        default="Vizyonumuz, Betikma'yı küresel çapta lider bir AI metin editörü platformu haline getirmektir. İnsan ve yapay zeka iş birliğinin en iyi örneklerini sunarak, geleceğin iletişim standartlarını belirlemeyi amaçlıyoruz. Dil bariyerlerini ortadan kaldıran, yaratıcılığı teşvik eden ve her alanda metin üretimini kolaylaştıran bir dünya hayal ediyoruz. Sürekli öğrenen ve gelişen bir platform olarak, kullanıcılarımızın ihtiyaçlarına göre evrimleşmeyi ve onlara her zaman en güncel ve güçlü araçları sunmayı taahhüt ediyoruz.",
        verbose_name="Vizyon Metni"
    )

    # Değerler Bölümü (Her bir değer için ayrı alanlar)
    value1_icon = models.CharField(
        max_length=50,
        default="fas fa-brain",
        verbose_name="Değer 1 İkonu (Font Awesome)"
    )
    value1_title = models.CharField(
        max_length=100,
        default="Yenilikçilik",
        verbose_name="Değer 1 Başlığı"
    )
    value1_description = models.TextField(
        default="Sürekli gelişen yapay zeka teknolojilerini takip eder, en yeni çözümleri sunarız.",
        verbose_name="Değer 1 Açıklaması"
    )

    value2_icon = models.CharField(
        max_length=50,
        default="fas fa-hands-helping",
        verbose_name="Değer 2 İkonu (Font Awesome)"
    )
    value2_title = models.CharField(
        max_length=100,
        default="Erişilebilirlik",
        verbose_name="Değer 2 Başlığı"
    )
    value2_description = models.TextField(
        default="Yapay zekayı herkesin kolayca kullanabileceği bir araç haline getiririz.",
        verbose_name="Değer 2 Açıklaması"
    )

    value3_icon = models.CharField(
        max_length=50,
        default="fas fa-shield-alt",
        verbose_name="Değer 3 İkonu (Font Awesome)"
    )
    value3_title = models.CharField(
        max_length=100,
        default="Güvenilirlik",
        verbose_name="Değer 3 Başlığı"
    )
    value3_description = models.TextField(
        default="Kullanıcı verilerinin gizliliğine ve güvenliğine en üst düzeyde önem veririz.",
        verbose_name="Değer 3 Açıklaması"
    )

    class Meta:
        verbose_name = "Hakkımızda Sayfası İçeriği"
        verbose_name_plural = "Hakkımızda Sayfası İçerikleri"

    def __str__(self):
        return self.page_title

class TeamMember(models.Model):
    """
    'Hakkımızda' sayfasındaki ekip üyelerini tutan model.
    Her ekip üyesi için ayrı ayrı giriş yapılabilir.
    """
    name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    title = models.CharField(max_length=100, verbose_name="Unvan")
    description = models.TextField(verbose_name="Açıklama")
    # Profil resmi için ImageField kullanıyoruz. MEDIA_ROOT ayarlı olmalı.
    profile_picture = models.ImageField(
        upload_to='team_members/',
        blank=True,
        null=True,
        verbose_name="Profil Resmi"
    )
    # Varsayılan placeholder resim URL'si
    placeholder_image_url = models.URLField(
        default="https://placehold.co/120x120/E8DCFF/7C3AED?text=PP",
        verbose_name="Placeholder Resim URL'si"
    )

    class Meta:
        verbose_name = "Ekip Üyesi"
        verbose_name_plural = "Ekip Üyeleri"

    def __str__(self):
        return self.name

    def get_profile_image_url(self):
        """
        Eğer profil resmi varsa URL'sini döndürür, yoksa placeholder kullanır.
        """
        if self.profile_picture:
            return self.profile_picture.url
        return self.placeholder_image_url

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True) # Mesajın gönderildiği zamanı otomatik kaydeder

    def __str__(self):
        return f"Mesaj: {self.subject} - Kimden: {self.name}"

    class Meta:
        verbose_name = "İletişim Mesajı"
        verbose_name_plural = "İletişim Mesajları"
        ordering = ['-sent_at'] # En yeni mesajları en üstte göstermek için