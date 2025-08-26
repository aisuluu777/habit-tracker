import signals
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=CustomUser)
def greed_registered_users(self, sender, created, **kwargs):
    if created:
        try:
            user = CustomUser.objects.filter(self.instance)
        except CustomUser.DoesNotExist:
            raise ValueError()
        

        subject = 'Hello {user.full_name}!'
        message = 'We`re happy to see you. Enjoy habit-tracker. Set habits - be happy'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.USER_HOST_EMAIL,
            recipient_list=user,
            fail_silently=True
        )
        
        

