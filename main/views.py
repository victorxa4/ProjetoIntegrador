from .permissions import *
from .serializers import *
from .models import *
from rest_framework import generics
from django_filters import rest_framework as filters

class Account_View(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = Account_Serializer
    permission_classes = [Attendant_FullAccess|Support_FullAccess|IsOwnAccount]
class Account_RetrieveUpdateDestroy_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    permission_classes = [Attendant_FullAccess|Support_FullAccess|IsOwnAccount]
    serializer_class = Account_Serializer

class Luggage_View(generics.ListCreateAPIView):
    queryset = Luggage.objects.all()
    serializer_class = Luggage_Serializer
    permission_classes = [Attendant_FullAccess|Support_FullAccess|Consumer_ReadOnly|Manager_ReadOnly]
class Luggage_RetrieveUpdateDestroy_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Luggage.objects.all()
    permission_classes = [Attendant_FullAccess|Support_FullAccess|Consumer_ReadOnly|Manager_ReadOnly]
    serializer_class = Luggage_Serializer

class Luggage_Stage_View(generics.ListCreateAPIView):
    queryset = Luggage_Stage.objects.all()
    serializer_class = Luggage_Stage_Serializer
    permission_classes = [Support_FullAccess|Consumer_ReadOnly|Manager_FullAccess]
    filterset_fields = ['luggage_stage_id', 'luggage_stage', 'luggage_stage_luggage']
class Luggage_Stage_RetrieveUpdateDestroy_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Luggage_Stage.objects.all()
    permission_classes = [Support_FullAccess|Consumer_ReadOnly|Manager_FullAccess]
    serializer_class = Luggage_Stage_Serializer