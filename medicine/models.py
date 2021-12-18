from django.db import models

# Create your models here.
class Medicine(models.Model):
        Id = models.IntegerField(null=True)
        M_Name = models.TextField(null="False",blank="True")
        M_Type = models.TextField(null=True)
        Mnf_Date = models.DateField(null=True)
        Exp_Date = models.DateField(null=True)
        MRP = models.FloatField(null=True)
        Stock = models.IntegerField(null=True)

        def __str__(self):
            return self.M_Name