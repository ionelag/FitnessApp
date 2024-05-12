from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#def getcurrentusername(instance,filename):
#    return f"profile_images/{instance.user.username}/{filename}"
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    subscription = models.DateTimeField()
    total_visits = models.IntegerField(default=0)
    #picture = models.ImageField(upload_to=getcurrentusername, blank=True)
    #fitness_goals = models.TextField(blank=True)
    #medical_conditions = models.TextField(blank=True)

    @property
    def level(self):
        if self.total_visits >= 20:
            return 'Advanced'
        elif self.total_visits >= 10:
            return 'Intermediate'
        else:
            return 'Beginner'


    def has_subscription_available(self):
        return self.subscription > timezone.now()

    def __str__(self):
        return self.name
