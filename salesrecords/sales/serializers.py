from rest_framework import serializers
from .models import SalesRecord


class SalesRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesRecord
        fields = ['ID','Region', 'Country', 'Item_Type', 'Sales_Channel', 'Order_Priority', 'Order_Date','Order_ID','Ship_Date','Units_Sold','Unit_Price',
        'Unit_Cost','Total_Revenue','Total_Cost','Total_Profit']

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance