from django.db import models


class Brand(models.Model):
  id = models.AutoField
  
class Car(models.Model):
  id = models.AutoField(primary_key=True)
  model = models.CharField(max_length=200)
  brand = models.CharField(max_length=200)
  factory_year = models.IntegerField(blank=True, null=True)
  model_year = models.BigIntegerField(blank=True, null=True)
  value = models.FloatField(blank=True, null=True)

  def __str__(self):
    return self.model
  
