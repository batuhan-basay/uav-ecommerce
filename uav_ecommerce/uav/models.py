from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Uav(models.Model):
    model = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uavs")
    weight = models.IntegerField()
    Flight_time = models.IntegerField()
    Flight_distance = models.IntegerField()
    price = models.IntegerField()
    Battery = models.CharField(max_length=20)

    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f"{self.model}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model)
        super().save(*args, **kwargs)



