from django.db import models

# Create your models here.
class Book(models.Model):
    #  定义完模型，序列化转换
    b_name = models.CharField(max_length=32)
    b_price = models.FloatField(default=2)