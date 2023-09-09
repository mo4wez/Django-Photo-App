from django.db import models

from django.urls import reverse

class Photo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("photo_detail", kwargs={"pk": self.pk})

    