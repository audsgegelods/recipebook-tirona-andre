from django.shortcuts import render

# Create your views here.

def recipelist(request):
    ctx = [

    ]
    return render(request, 'recipe_list.html', ctx)

def recipe1(request):
    ctx = [

    ]
    return render(request, 'recipe_list.html', ctx)

def recipe2(request):
    ctx = [

    ]
    return render(request, 'recipe_list.html', ctx)