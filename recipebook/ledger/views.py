from .models import Recipe, RecipeImage
from .forms import RecipeForm, ImageForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class RecipeListView(ListView):
    model = Recipe
    template_name = 'list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = 'login.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_add.html'
    redirect_field_name = 'login.html'


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = ImageForm
    template_name = 'recipe_image.html'
    redirect_field_name = 'login.html'


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe.html'
    redirect_field_name = 'login.html'
