from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default='')
    sub_category=models.CharField(max_length=50,default='')
    price=models.IntegerField(default=0)
    Image=models.ImageField(upload_to='shop/image',default='')
    product_dis=models.CharField(max_length=500)
    punlish_date=models.DateField()
    
    def __str__(self):
        return self.product_name