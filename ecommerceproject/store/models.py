from django.db import models

# Create your models here.
class Order(models.Model):
    status = models.IntegerField()
    status_legend = {1: 'in cart', 2: 'ordered'}
    username = models.CharField(max_length = 128)

    def get_status(self):
        return self.status_legend[self.status]

class Product(models.Model):
    name = models.CharField(max_length = 128)
    price = models.IntegerField()
    image = models.TextField()
    description = models.TextField()
    product_type = models.TextField()
    quantity = models.IntegerField() 
    orderproducts = models.ManyToManyField(Order, through = "OrderProduct")

    def dollars(self):
        if self.price <= 99999:
            return "%.2f" % (self.price / 100.0)
        else:
            return '{:,.2f}'.format(self.price / 100.0)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()


# from store.models  import aaaa

def make_product():
    print 1111
    products=["bottle","mouse","keyboard","pen","notebook"]
    types=["bottle","tech","tech","office supply","office supply"]
    for i in range(len(products)):
        print 333
        p = Product()
        p.name=products[i]
        p.price=5000+i*2500 
        p.image="image"
        p.description="This is product "+products[i]
        p.product_type=types[i]
        p.quantity=0+i*20
        p.save()

    print 2222