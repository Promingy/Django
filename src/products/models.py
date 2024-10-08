from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length = required 
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=True) #null=True, default=True

    def get_absolute_url(self):
        return  reverse("products:product-detail", kwargs={"id": self.id}) # f"products/{self.id} / "products:" is based of of app_name in urls.py

    def to_dict(self):
        dictionary = {
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "summary": self.summary,
            "featured": self.featured
        }

        return dictionary