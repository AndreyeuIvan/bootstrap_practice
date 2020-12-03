from django.db import models

# Create your models here.

class Topping(models.Model):
    REGULAR = 1
    DOUBLE = 2
    TRIPLE = 3
    AMOUNT_CHOICES = (
        (REGULAR, 'Regular'),
        (DOUBLE, 'Double'),
        (TRIPLE, 'Triple'),
    )
    name = models.CharField(max_length=100)
    amount = models.IntegerField(choices=AMOUNT_CHOICES, default=REGULAR)

    def __str__(self):
        return self.name


class Size(models.Model):
    SIZE_CHOICES = (
        (6, 'Regular'),
        (12, 'Double'),
        (24, 'Triple'),
    )
    PRICE_CHOICES = (
        ('6$', 6),
        ('11$',12),
        ('15$', 24),
    )
    amount = models.IntegerField(choices=SIZE_CHOICES, default=SIZE_CHOICES[0][0])
    price = models.CharField(choices=PRICE_CHOICES, default=PRICE_CHOICES[0][0], max_length=10)


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
