from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Receipe  

# Create your views here.
def recipes(request):
    if request.method == 'POST':
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_instructions = request.POST.get('receipe_instructions')
        receipe_image = request.FILES.get('receipe_image')

        print(receipe_name)
        print(receipe_description)
        print(receipe_instructions)
        print(receipe_image)
        

        receipe = Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_instructions=receipe_instructions,
            receipe_image=receipe_image,
        )
        receipe.save() 
        return redirect('recipes')
    return render(request,'recipes.html')
   

def edit_receipe(request, recipe_id):
    receipe = get_object_or_404(Receipe, id=recipe_id)
    if request.method == 'POST': 
        receipe.receipe_name = request.POST.get('receipe_name')
        receipe.receipe_description = request.POST.get('receipe_description')
        receipe.receipe_instructions = request.POST.get('receipe_instructions') 
        receipe.receipe_image = request.FILES.get('receipe_image')
        receipe.save()
        return redirect('view_receipes')
    return render(request, 'edit_receipe.html', {'recipe': receipe}) 

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Receipe, id=recipe_id)
    recipe.delete()
    return redirect('view_receipes')

def view_blog(request, recipe_id):
    recipe = get_object_or_404(Receipe, id=recipe_id)
    return render(request, 'view_blog.html', {'recipe': recipe})

def search(request):
    query = request.GET.get('query')
    recipes = Receipe.objects.filter(receipe_name__icontains=query)
    return render(request, 'search.html', {'recipes': recipes})

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def view_receipes(request):
    recipes = Receipe.objects.all()
    return render(request, 'view_receipes.html', {'recipes': recipes})


