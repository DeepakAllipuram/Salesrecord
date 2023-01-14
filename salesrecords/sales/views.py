from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from sales.models import SalesRecord
from rest_framework import status
from rest_framework.decorators import api_view
from sales.serializers import SalesRecordSerializer
import csv


@api_view(['GET', 'POST'])
def sales_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        salesrecord = SalesRecord.objects.all()
        serializer = SalesRecordSerializer(salesrecord, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SalesRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def sales_view(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        salesrecord = SalesRecord.objects.get(ID=pk)
    except SalesRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SalesRecordSerializer(salesrecord)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SalesRecordSerializer(salesrecord, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def download_sales(request):
	output = []
	response = HttpResponse (content_type='text/csv')
	writer = csv.writer(response)
	query_set = SalesRecord.objects.all()
	#Header
	writer.writerow(['ID','Region', 'Country', 'Item_Type', 'Sales_Channel', 'Order_Priority', 'Order_Date','Order_ID','Ship_Date','Units_Sold','Unit_Price',
        'Unit_Cost','Total_Revenue','Total_Cost','Total_Profit'])
	for sales in query_set:
	    output.append([sales.ID, sales.Region, sales.Country, sales.Item_Type, sales.Sales_Channel, sales.Order_Priority, sales.Order_Date,
	    	sales.Order_ID, sales.Ship_Date, sales.Units_Sold,sales.Unit_Price,sales.Unit_Cost,sales.Total_Revenue,sales.Total_Cost,
	    	sales.Total_Profit])
	#CSV Data
	writer.writerows(output)
	return response