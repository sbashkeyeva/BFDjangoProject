from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100)
    # image = models.ImageField(blank=True, null=True)
    phone = models.IntegerField()
    description = models.CharField(max_length=1000)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    #image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class ShopFlower(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    flower_id = models.ForeignKey(Flower, on_delete=models.CASCADE)
    price = models.IntegerField()


class Order(models.Model):
    customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    shop_id=models.ForeignKey(Shop, on_delete=models.CASCADE)
    sum=models.IntegerField()


class OrderFlower(models.Model):
    flower_id=models.ForeignKey(Flower, on_delete=models.CASCADE)
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE)
    count=models.IntegerField()