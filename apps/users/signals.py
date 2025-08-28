from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=CustomUser)
def greed_registered_users(sender,instance ,created, **kwargs):
    if created:
        
        subject = 'Hello {instance.full_name}!'
        message = 'We`re happy to see you. Enjoy habit-tracker. Set habits - be happy'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.email],
            fail_silently=True
        )
        
        

