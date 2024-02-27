from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

from django.urls import reverse

from django.utils.text import slugify

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    mainactor = models.CharField(max_length=50, null=True)
    is_boxofficehit = models.BooleanField(default=False)

    # Adding a slug field in the model
    slug = models.SlugField(default="")
    
    def __str__(self):
        return f"(Title: { self.title } Rating: { self.rating })"
    
    # def get_absolute_url(self):
    #     return reverse("movie-detail", args=[self.id])

    # Changing the method get_absolute_url to generate
    # url based on slug and not id

    def get_absolute_url(self):
        return reverse("movie-detail", args=[self.slug])


    # Overriding the default save method to add a 
    # proper slug value to the slug field of the 
    # model instance

    # Import a helper function called 'slugify'
    # for generating proper slugs

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)