from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from django.http import HttpResponse

def sayHello(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]