from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, 
                            unique=True)
    slug = models.SlugField(max_length=100, 
                            unique=True, 
                            blank=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('planet_list_by_cat',{'category_slug': self.slug})


class Planet(models.Model):
    category = models.ForeignKey(Category, 
                                 on_delete=models.PROTECT, 
                                 related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100,
                            unique=True)
    image = models.ImageField(upload_to="planets/%Y/%m/%d/", 
                              blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.DecimalField(default=0, 
                                   max_digits=4,
                                   decimal_places=2)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("main_planet_detail", 
                       kwargs={"planet_slug": self.slug})
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.discount / 100 * self.price, 2)
        return self.price

