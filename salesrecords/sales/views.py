from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from sales.models import SalesRecord
from rest_framework import status
from rest_framework.decorators import api_view
from sales.serializers import SalesRecordSerializer


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


