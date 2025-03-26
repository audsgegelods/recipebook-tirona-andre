from django.urls import path
from .views import (RecipeListView,
                    RecipeDetailView,
                    RecipeCreateView,
                    RecipeUpdateView,
                    ImageCreateView,)

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeUpdateView.as_view(), name='recipe-detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/add_image', ImageCreateView.as_view(), name='image-add')
]

app_name = 'ledger'
