from django.db import models

# Create your models here.
class customer(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    email=models.CharField(max_length=50,default="")
    mobile=models.IntegerField(default="0")
    def __str__(self):
        return self.user_name
class client(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    email=models.CharField(max_length=50,default="")
    mobile=models.IntegerField(default="0")
    def __str__(self):
        return self.user_name
class product(models.Model):
    product_id = models.AutoField
    client_name=models.CharField(max_length=50,default="")
    product_name= models.CharField(max_length=50,default="")
    category=models.CharField(max_length=50,default="")
    subcategoru=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300,default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to="page1/images",default="")
    def __str__(self):
        return self.product_name
class contact(models.Model):
    msg_id = models.AutoField
    user_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    mobile=models.IntegerField(default=0)
    desc=models.CharField(max_length=300,default="")
    def __str__(self):
        return self.user_name
class cart(models.Model):
    product_number=models.AutoField
    customer_name=models.CharField(max_length=50,default="")
    product_id=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)



