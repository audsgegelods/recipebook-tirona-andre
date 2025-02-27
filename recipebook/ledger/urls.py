from django.urls import path
from .views import RecipeListView, RecipeDetailView, recipelist, recipe1, recipe2

urlpatterns = [
    #path('recipes/list', recipelist, name='recipe-list'),
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    #path('recipe/1', recipe1, name='recipe-1'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-1'),
    #path('recipe/2', recipe2, name='recipe-2'),
]

app_name = 'ledger'