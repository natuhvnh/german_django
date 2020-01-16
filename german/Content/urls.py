from django.urls import path, include
from .views import GenericCardAPI, GenericIntroAPI, GenericServiceAPI, GenericSliderAPI

urlpatterns = [
  path('card', GenericCardAPI.as_view()),
  path('card/<int:id>', GenericCardAPI.as_view()),
  path('intro', GenericIntroAPI.as_view()),
  path('intro/<int:id>', GenericIntroAPI.as_view()),
  path('service', GenericServiceAPI.as_view()),
  path('service/<int:id>', GenericServiceAPI.as_view()),
  path('slider', GenericSliderAPI.as_view()),
  path('slider/<int:id>', GenericSliderAPI.as_view()),
]