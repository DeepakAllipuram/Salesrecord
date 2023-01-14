from django.db import models

# Create your models here.

class SalesRecord(models.Model):
    Region = models.TextField()
    Country = models.TextField()
    Item_Type = models.TextField()
    Sales_Channel = models.TextField()
    Order_Priority = models.TextField()
    Order_Date = models.TextField()
    Order_ID = models.IntegerField(null=True)
    Ship_Date = models.TextField()
    Units_Sold = models.IntegerField(null=True)
    Unit_Price = models.DecimalField(max_digits=20, decimal_places=2)
    Unit_Cost = models.DecimalField(max_digits=20, decimal_places=2)
    Total_Revenue = models.DecimalField(max_digits=20, decimal_places=2)
    Total_Cost = models.DecimalField(max_digits=20, decimal_places=2)
    Total_Profit = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = 'sales_records'
