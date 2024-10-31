from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Testmonials(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(default='mamnoti.jpg')

    def __str__(self) -> str:
        return self.user.first_name and self.content

class Fqa(models.Model):
    title = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.title

class service(models.Model):
    title = models.TextField()
    desc = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class service_two(models.Model):
    title = models.TextField()
    desc = models.TextField()
    status = models.BooleanField(default=False)

class Pros(models.Model):
    title = models.TextField()
    status = models.BooleanField(default=False)

class Prices(models.Model):
    titel = models.TextField()
    price = models.IntegerField(default=0)
    pros = models.ManyToManyField(Pros)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.titel



