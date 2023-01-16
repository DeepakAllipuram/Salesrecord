from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from sales.models import SalesRecord
from rest_framework import status
from rest_framework.decorators import api_view
from sales.serializers import SalesRecordSerializer
import csv
from rest_framework import generics
from django.template import loader
import pdb
from django.views.decorators.csrf import csrf_exempt



def sales_list_html(request):
    template = loader.get_template('sales/sales_list.html')
    context = {}
 
    return HttpResponse(template.render(context, request))

def sales_create_html(request):
    template = loader.get_template('sales/sales_create.html')
    context = {    }
 
    return HttpResponse(template.render(context, request))

def sales_edit_html(request, pk):
    template = loader.get_template('sales/sales_edit.html')
    context = {
        'sales_id': pk
    }
 
    return HttpResponse(template.render(context, request))


class SalesList(generics.ListCreateAPIView):
    queryset = SalesRecord.objects.all()
    serializer_class = SalesRecordSerializer


@api_view(['POST'])
@csrf_exempt
def sales_add(request):
    pdb.set_trace()
    if request.method == 'POST':
        print(request.method)
        # data = request.data["data"]
        # print(data)
        # try:
        #     serializer = SalesRecord.objects.create(Region=data[region])
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        # except Exception as e:
        #     print(e)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
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