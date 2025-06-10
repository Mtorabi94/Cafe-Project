from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import json

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            try:
                # Send email
                subject = f'New Contact Form Submission from {name}'
                email_message = f'''
                Name: {name}
                Email: {email}
                Message: {message}
                '''
                
                send_mail(
                    subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['your-cafe-email@example.com'],
                    fail_silently=False,
                )
                
                messages.success(request, 'پیام شما با موفقیت ارسال شد!')
                return redirect('index')
                
            except Exception as e:
                messages.error(request, 'خطا در ارسال پیام. لطفاً دوباره تلاش کنید.')
        else:
            messages.error(request, 'لطفاً تمام فیلدها را پر کنید.')
    
    return render(request, 'website/index.html')