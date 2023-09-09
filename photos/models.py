from django.db import models

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Photo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("photo_detail", kwargs={"pk": self.pk})

    