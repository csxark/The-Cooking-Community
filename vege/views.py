from django.shortcuts import render, redirect
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
            receipe_image=receipe_image
        )
        receipe.save() 
        return redirect('recipes')
    return render(request,'recipes.html')
   

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def view_receipes(request):
    recipes = Receipe.objects.all()
    return render(request,'view_receipes.html',{'recipes':recipes})


