from django.db import models
from loginsystem.models import newuser

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 300)
    publish_date = models.DateField()
    category = models.CharField(max_length = 200, default = " ")
    sub_category = models.CharField(max_length = 200, default = " ")
    price = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = "shopme/images", default = " ")

    def __str__(self):
        return self.product_name 

class furt(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)

class purchaseperuser(models.Model):
    userInstance = models.OneToOneField(newuser, on_delete=models.CASCADE)
    productuser = models.ForeignKey(product, on_delete=models.CASCADE)
