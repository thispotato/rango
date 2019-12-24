from django.db import models
from django.template.defaultfilters import slugify 
from .utils import num_generator

class Category(models.Model):
    title = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    slug  = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title) + num_generator()
        super(Category , self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Page(models.Model):
    category  = models.ForeignKey(Category , on_delete = models.CASCADE)
    title     = models.CharField(max_length=255)
    slug      = models.SlugField(blank= True)
    views     = models.IntegerField(default=0)
    content   = models.TextField(blank = True , null = True)

    def __str__(self):
        return self.title
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title) + num_generator()
        super(Page , self).save(*args, **kwargs)

