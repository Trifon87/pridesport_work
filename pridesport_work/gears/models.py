from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

from pridesport_work.pridesport_auth.models import UserProfile


class Gear(models.Model):
    FIGHT = 'fight'
    FITNESS = 'fitness'
    CLOTHING = 'clothing'
    UN = 'unknown'
    SPORT_TYPES = (
        (FIGHT, "fight"),
        (FITNESS, "fitness"),
        (CLOTHING, 'clothing'),
        (UN, 'Unknown')
    )
    type = models.CharField(max_length=35, choices=SPORT_TYPES, default=UN)
    name = models.CharField(max_length= 35, blank=False)
    price = models.FloatField(blank=False)
    description = models.TextField(blank=True)
    image_url = models.ImageField(
        upload_to='gear',
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # likes = models.IntegerField(blank=True)
    def __str__(self):
        return f"{self.id} {self.name} {self.price}"


class Like(models.Model):
    gear = models.ForeignKey(Gear, on_delete= models.CASCADE)
    test = models.CharField(max_length=2, default="OK")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
