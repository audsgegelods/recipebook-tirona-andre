from django.urls import path
from .views import recipelist, recipe1, recipe2

urlpatterns = [
    path('list', recipelist, name='recipe-list'),
    path('1', recipe1, name='recipe-1'),
    path('2', recipe2, name='recipe-2'),
]

app_name = 'ledger'