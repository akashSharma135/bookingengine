from rest_framework.urls import path
from .views import RoomsAvailableView

urlpatterns = [
    path('units/', RoomsAvailableView.as_view())
]