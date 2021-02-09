from django.db import models

class Employ(models.Model):
    employName = models.CharField(max_length=100, null=True, default="김씨")
    employBirth = models.CharField(null=True)
    employLevel = models.CharField(max_length=100, null=True, default="사원")
    employSalary = models.PositiveBigIntegerField(null=False, default=0)
    employMemo = models.CharField(null=True)