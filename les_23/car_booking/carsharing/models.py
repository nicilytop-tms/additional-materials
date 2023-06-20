from django.db import models


class User(models.Model):
    phone = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, default=None)


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)


class AutoModel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)


class Auto(models.Model):
    STATUSES = (
        ('1', 'FREE'),
        ('2', 'BOOKED'),
        ('3', 'TAKEN'),
    )
    vin_code = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=5, choices=STATUSES, default='1')

    auto_model = models.ForeignKey('AutoModel', on_delete=models.CASCADE)

    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, default=None)
