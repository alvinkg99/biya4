from django.db import models
from datetime import datetime

#user registration

class registration(models.Model):
    Name=models.CharField(max_length=100)
    Number=models.IntegerField()
    Email=models.EmailField()
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'''
                    {self.Name}
        '''
    
#product details

class product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    wood=models.CharField(max_length=50)
    colour=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return f'''
                {self.name}'''

# cart details 

class cart(models.Model):
    product_id=models.IntegerField()
    user=models.CharField(max_length=50)
    quantity=models.IntegerField()

    def __str__(self) -> str:
        return f'''
                {self.user}'''
    
#mycart details(delivered or pending)

class mycart(models.Model):
    products= models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(registration,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    delivered=models.BooleanField(default=False)

    def __str__(self) -> str:
         return f'''
                {self.user}'''
    

class wish(models.Model):
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(registration,on_delete=models.CASCADE)

    def __str__(self) -> str:
         return f'''
                {self.user}'''
    
    
class complaints(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    complaint=models.TextField(
        
    )
 

class order(models.Model):
    user = models.ForeignKey(registration, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    district = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    state = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=150, null=True)
    orderstatus = (
        ('pending','pending'),
        ('Out for shipping','Out for shipping'),
        ('Completed','Completed')
    )
    status = models.CharField(max_length=150,choices=orderstatus, default='pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def _str_(self) -> str:
        return f'{self.user},{self.tracking_no}'
    
class orderitem(models.Model):
    orderdet = models.ForeignKey(order,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def _str_(self) -> str:
        return f'{self.orderdet}'


class profile(models.Model):
    user = models.OneToOneField(registration,on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    district = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    state = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self) -> str:
        return f'{self.user.Username}'
    

class profilepic(models.Model):
    user = models.OneToOneField(registration,on_delete=models.CASCADE)
    propic = models.ImageField(upload_to='images/profilepic')

    def _str_(self) -> str:
        return f'{self.user.Username}'
# Create your models here.
