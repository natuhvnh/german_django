from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins
from .models import Card, Intro, Service, Slider
from .serializers import CardSerializer, IntroSerializer, ServiceSerializer, SliderSerializer

# Create your views here.
class GenericCardAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
  serializer_class = CardSerializer
  queryset = Card.objects.all()
  lookup_field = 'id'
  authentication_classes = [BasicAuthentication, TokenAuthentication]
  permission_classes = [IsAuthenticated]
  def get(self, request, id=None):
    if id:
      return self.retrieve(request)
    else:
      return self.list(request)
  def post(self, request):
    return self.create(request)
  def put(self, request, id=None):
    return self.update(request, id)
  def delete(self, request, id):
    return self.destroy((request, id))

class GenericIntroAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
  serializer_class = IntroSerializer
  queryset = Intro.objects.all()
  lookup_field = 'id'
  authentication_classes = [BasicAuthentication, TokenAuthentication]
  permission_classes = [IsAuthenticated]
  def get(self, request, id=None):
    if id:
      return self.retrieve(request)
    else:
      return self.list(request)
  def post(self, request):
    return self.create(request)
  def put(self, request, id=None):
    return self.update(request, id)
  def delete(self, request, id):
    return self.destroy((request, id))

class GenericServiceAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
  serializer_class = ServiceSerializer
  queryset = Service.objects.all()
  lookup_field = 'id'
  authentication_classes = [BasicAuthentication, TokenAuthentication]
  permission_classes = [IsAuthenticated]
  def get(self, request, id=None):
    if id:
      return self.retrieve(request)
    else:
      return self.list(request)
  def post(self, request):
    return self.create(request)
  def put(self, request, id=None):
    return self.update(request, id)
  def delete(self, request, id):
    return self.destroy((request, id))

class GenericSliderAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
  serializer_class = SliderSerializer
  queryset = Slider.objects.all()
  lookup_field = 'id'
  authentication_classes = [BasicAuthentication, TokenAuthentication]
  permission_classes = [IsAuthenticated]
  def get(self, request, id=None):
    if id:
      return self.retrieve(request)
    else:
      return self.list(request)
  def post(self, request):
    return self.create(request)
  def put(self, request, id=None):
    return self.update(request, id)
  def delete(self, request, id):
    return self.destroy((request, id))