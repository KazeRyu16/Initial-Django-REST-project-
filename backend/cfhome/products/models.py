from django.db import models
from django.conf import settings
from django.db.models import Q

user = settings.AUTH_USER_MODEL

class productQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self,query,user = None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query) 
        qs = self.is_public().filter(lookup)
        return qs
    

class productmanager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return productQuerySet(self.model,using=self.db)

    def search(self , query , user=None):
        return self.get_queryset().search(query,user=user)

# Create your models here.
class product(models.Model):
    user = models.ForeignKey(user, default=1, null=True , on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
    public = models.BooleanField(default=True)

    objects = productmanager()

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)


    def get_discount(self):
        return "%.2f" %(float(self.price) * 0.4)
