from rest_framework import serializers
from .models import Card, Intro, Service, Slider

class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Card
    # fields = ['id', 'title', 'author']
    fields = '__all__'

class IntroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Intro
    # fields = ['id', 'title', 'author']
    fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    # fields = ['id', 'title', 'author']
    fields = '__all__'

class SliderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Slider
    # fields = ['id', 'title', 'author']
    fields = '__all__'

# class ArticleSerializer(serializers.Serializer):
#   title = serializers.CharField(max_length=100)
#   author = serializers.CharField(max_length=100)
#   email = serializers.EmailField(max_length=100)
#   date = serializers.DateTimeField()

#   def create(self, validated_data):
#     return Article.objects.create(validated_data)
#   def update(self, instance, validated_data):
#     instance.title = validated_data.get('title', instance.title)
#     instance.author = validated_data.get('author', instance.author)
#     instance.email = validated_data.get('email', instance.email)
#     instance.date = validated_data.get('date', instance.date)
#     instance.save()
#     return instance
