from django.urls import path
from .views import UpdateGenerateData

urlpatterns = [
    path("see-all-data", UpdateGenerateData.as_view())
]
