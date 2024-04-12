from django.urls import path
from .views import show_bank

urlpatterns = [
    path('<int:bank_id>', show_bank, name='show_bank'),
]
