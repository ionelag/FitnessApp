from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.models import User
from FitnessApp.models import UserProfile

def send_subscription_expiry_email():
    expiring_users = UserProfile.objects.filter(subscription__lte=timezone.now() + timezone.timedelta(days=3))
    for user_profile in expiring_users:
        send_mail(
            'Subscription Expiry Notification',
            f'Hello {user_profile.user.username}, your subscription is about to expire. Please renew your subscription.',
            'fromnoreply@fitness.com',
            [user_profile.user.email],
            fail_silently=False,
        )


