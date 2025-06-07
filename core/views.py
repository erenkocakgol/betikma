# core/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from core.forms import ContactForm
from core.models import AboutPageContent, TeamMember
from betikma import settings

def home_view(request):
    # Check if the user is authenticated (logged in)
    if not request.user.is_authenticated:
        # If not logged in, clear the session
        request.session.flush() # This will delete all data in the current session
    
    context = {
        'welcome_message': 'Betikma\'ya Hoş Geldiniz!',
        'description': 'Yapay zeka destekli metin oluşturma ve düzenleme aracınız.',
    }
    return render(request, 'home.html', context)

def about_view(request):
    about_data = AboutPageContent.objects.first()
    team = TeamMember.objects.all()
    about_content = {
        'about_content': about_data,
        'team_members': team,
    }
    return render(request, 'about.html', about_content)

def services_view(request):
    return render(request, 'services.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # 2. E-posta Gönder (Önerilen)
            try:
                send_mail(
                    subject=f'İletişim Formu: {subject} (Gönderen: {name})',
                    message=f'Gönderen: {name}\nE-posta: {email}\n\nMesaj:\n{message}',
                    from_email=settings.EMAIL_HOST_USER, # settings.py dosyanızda tanımlanmalı
                    recipient_list=['kristalsoft.info@gmail.com'], # Mesajı alacak e-posta adresi
                    fail_silently=False,
                )
                # Başarılı olduğunda bir "başarı" mesajı gösterebilirsiniz
                # from django.contrib import messages
                # messages.success(request, "Mesajınız başarıyla gönderildi!")
                return redirect('contact') # Başarılı bir sayfaya yönlendirme
            except Exception as e:
                # Hata durumunda bir "hata" mesajı gösterebilirsiniz
                # messages.error(request, f"Mesajınız gönderilirken bir hata oluştu: {e}")
                pass # Hata yönetimi burada yapılabilir

    else:
        form = ContactForm() # GET isteği ise boş bir form oluştur

    return render(request, 'contact.html', {'form': form})

# Opsiyonel: Mesaj gönderimi başarılı olduğunda yönlendirilecek sayfa
def contact_success_view(request):
    return render(request, 'contact_success.html') # contact_success.html adında bir şablon oluşturmanız gerekir

def support_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) # ContactForm'u burada kullanıyorsunuz
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=f'Destek Formu: {subject} (Gönderen: {name})',
                    message=f'Gönderen: {name}\nE-posta: {email}\n\nMesaj:\n{message}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['kristalsoft.info@gmail.com'], # Bu adres destek mesajları için uygun olmalı
                    fail_silently=False,
                )
                return redirect('support_success') # Burayı 'support_success' olarak değiştirin
            except Exception as e:
                # Hata yönetimi
                pass
    else:
        form = ContactForm()
    return render(request, 'support.html', {'form': form})

def support_success_view(request):
    return render(request, 'support_success.html') # Bu şablonu oluşturmanız gerekiyor

def privacy_policy_view(request):
    return render(request, 'privacy_policy.html')

def terms_of_service_view(request):
    return render(request, 'terms_of_service.html')