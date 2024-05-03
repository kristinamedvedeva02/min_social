from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from users.models import User
from rest_framework import viewsets, permissions, status
from .serializers import *
from django.http import JsonResponse
from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes

def main(request):
    users = User.objects.order_by('-id')
    return render(request, 'main/main.html', {'users': users})


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAdminUser]


class OfficeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows offices to be viewed or edited.
    """

    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAdminUser]


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAdminUser]



# class OfficeListView(APIView):      #Example of APIView methods
#     """
#     List all offices, or create a new office.
#     """

#     def get(self, request, format=None):
#         offices = Office.objects.all()
#         serializer = OfficeSerializer(offices, many=True)
#         return JsonResponse(serializer.data, safe = False)

#     def post(self, request, format=None):
#         serializer = OfficeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe = False)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class OfficeDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     permission_classes = [permissions.IsAdminUser]

#     def get_object(self, pk):
#         try:
#             return Office.objects.get(pk=pk)
#         except Office.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         office = self.get_object(pk)
#         serializer = OfficeSerializer(office)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         office = self.get_object(pk)
#         serializer = OfficeSerializer(office, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         office = self.get_object(pk)
#         office.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)