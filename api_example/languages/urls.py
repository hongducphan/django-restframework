from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('language', views.LanguageView)
router.register('paradigm', views.ParadigmView)
router.register('programmer', views.ProgrammerView)
# router.register('testapiresponse', views.test_api_response)

urlpatterns = [
    path('', include(router.urls)),
    path('testapiresponse', views.LanguageView.get)
]
