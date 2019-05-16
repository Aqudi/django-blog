from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.title