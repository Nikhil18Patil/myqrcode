from django.urls import path
from .views import qrview
urlpatterns = [
    path('qrview/',qrview , name="qrview" )
]
