from django.core.cache import cache
import secrets
from django.core.mail import send_mail
from django.conf import settings


def generate_otp():
    numbers = '123456789'
    return ''.join(secrets.choice(numbers) for i in range(6))


def send_otp_code(email, code):
    subject = 'Your otp code'
    message = f'here is your otp code {code}'
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False
    )

def get_email_from_cache(code):
    return cache.get(code)
