# editor/views.py

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import io
from docx import Document
import google.generativeai as genai
import os
import dotenv

dotenv.load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
model = None

if not GEMINI_API_KEY:
    print("UYARI: GEMINI_API_KEY ortam değişkeni ayarlanmamış. AI özellikleri çalışmayacaktır.")
else:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemma-3-12b-it')
        print("Gemini modeli başarıyla yüklendi.")
    except Exception as e:
        print(f"HATA: Gemini modeli başlatılamadı: {e}")
        model = None

def editor_view(request):
    return render(request, 'editor/editor.html', {})

@csrf_exempt
def api_process_text(request):
    if not model:
        return JsonResponse({'error': 'AI modeli yapılandırılmamış veya yüklenememiş. Lütfen API anahtarını kontrol edin veya sunucu loglarına bakın.'}, status=500)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            action = data.get('action')
            text = data.get('text')

            if not text or not text.strip():
                return JsonResponse({'error': 'İşlemek için metin boş olamaz.'}, status=400)

            processed_text = ""
            prompt = ""

            try:
                if action == 'summarize':
                    prompt = f"Aşağıdaki metni Türkçe olarak kısa ve öz bir şekilde özetle, çıktıda sadece metni yaz:\n\n{text}"
                elif action == 'rewrite':
                    prompt = f"Aşağıdaki metni Türkçe olarak yeniden yaz. Anlamını koruyarak farklı kelimeler ve cümle yapıları kullan, çıktıda sadece metni yaz:\n\n{text}"
                elif action == 'expand':
                    prompt = f"Aşağıdaki metni Türkçe olarak detaylandırarak ve ek bilgilerle genişlet, çıktıda sadece metni yaz:\n\n{text}"
                elif action == 'grammar':
                    prompt = f"Aşağıdaki Türkçe metindeki dilbilgisi, yazım ve noktalama hatalarını düzelt. Sadece düzeltilmiş metni geri döndür:\n\n{text}"
                elif action == 'tone':
                    selected_tone = data.get('tone', 'resmi') # Varsayılan olarak resmi
                    # Ton seçeneklerine göre prompt'u dinamik olarak oluştur
                    if selected_tone == 'resmi':
                        prompt = f"Aşağıdaki Türkçe metnin tonunu resmi yap. Sadece dönüştürülmüş metni geri döndür:\n\n{text}"
                    elif selected_tone == 'samimi':
                        prompt = f"Aşağıdaki Türkçe metnin tonunu samimi ve arkadaşça yap. Sadece dönüştürülmüş metni geri döndür:\n\n{text}"
                    elif selected_tone == 'iknaedici':
                        prompt = f"Aşağıdaki Türkçe metnin tonunu ikna edici ve etkileyici yap. Sadece dönüştürülmüş metni geri döndür:\n\n{text}"
                    elif selected_tone == 'akademik':
                        prompt = f"Aşağıdaki Türkçe metnin tonunu akademik ve bilimsel yap. Sadece dönüştürülmüş metni geri döndür:\n\n{text}"
                    elif selected_tone == 'eğlenceli':
                        prompt = f"Aşağıdaki Türkçe metnin tonunu eğlenceli ve mizahi yap. Sadece dönüştürülmüş metni geri döndür:\n\n{text}"
                    else: # Varsayılan veya bilinmeyen ton için genel prompt
                        prompt = f"Aşağıdaki Türkçe metnin tonunu '{selected_tone}' yap. Sadece dönüştürülmüş metni geri döndür:\n\n{text}"
                elif action == 'continue_writing':
                    prompt = f"Aşağıdaki Türkçe metnin devamını yaz. Sadece devamını yaz, orijinal metni tekrarlama, çıktıda sadece metni yaz:\n\n{text}"
                else:
                    return JsonResponse({'error': 'Geçersiz AI işlemi.'}, status=400)

                response = model.generate_content(prompt)
                processed_text = response.text
                
                processed_text = processed_text.replace('**', '').replace('*', '').strip()

            except Exception as ai_error:
                print(f"Gemini API Hatası: {ai_error}")
                error_message = f'AI hizmeti hatası oluştu. Lütfen daha sonra tekrar deneyin.'
                if "API key not valid" in str(ai_error) or "permission" in str(ai_error).lower():
                     error_message = 'AI API anahtarı geçersiz veya yetkilendirme sorunu var. Lütfen yönetici ile iletişime geçin.'
                return JsonResponse({'error': error_message}, status=500)

            return JsonResponse({'processed_text': processed_text})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
    return JsonResponse({'error': 'Sadece POST istekleri kabul edilir.'}, status=405)


@csrf_exempt
def download_docx(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text_content = data.get('text', '')

            if not text_content.strip():
                return JsonResponse({'error': 'İndirmek için metin boş olamaz.'}, status=400)

            document = Document()
            for paragraph_text in text_content.split('\n'):
                document.add_paragraph(paragraph_text)

            buffer = io.BytesIO()
            document.save(buffer)
            buffer.seek(0)

            response = HttpResponse(
                buffer.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
            response['Content-Disposition'] = 'attachment; filename="metin_betikma.docx"'
            return response
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
        except Exception as e:
            print(f"DOCX oluşturma hatası: {str(e)}")
            return JsonResponse({'error': f'DOCX dosyası oluşturulurken bir hata oluştu: {str(e)}'}, status=500)
    return JsonResponse({'error': 'Sadece POST istekleri kabul edilir.'}, status=405)