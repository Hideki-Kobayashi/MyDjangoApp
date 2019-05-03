import django_filters
from rest_framework import viewsets, filters
from django.views.generic import TemplateView

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
class EntryViewSet(viewsets.ModelViewSet):
  queryset = Entry.objects.all()
  serializer_class = EntrySerializer
  
class SampleTemplateView(TemplateView):
    template_name = "index.html"