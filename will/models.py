from django.db import models


class User(models.Model):
    name = models.CharField(max_length=256, blank=True)
    gender_list = (('F','Female'),('M','Male'))
    gender = models.CharField(
        max_length = 1,
        choices = gender_list,
        blank=True
    )
    address = models.CharField(max_length=256, blank=True)
    NRIC = models.CharField(max_length = 9)
    date_of_birth = models.DateField(auto_now=True)

class Main(User):
    bankAcc = models.CharField(max_length=12)

class Asset(models.Model):
    TYPES_OF_ASSET = (('ch', 'Cash'), ('psb','Private Equity, Stock and Bonds'),
                        ('re','Real Estate'), ('cm', 'Commodity'),
                        ('pt','Patents'), ('fa','Furniture and Appliances'))
    asset_type = models.CharField(
        max_length = 2,
        choices = TYPES_OF_ASSET,
        blank=True
    )


