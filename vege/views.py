from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Receipe  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required (login_url='login') 
def recipes(request):
    if request.method == 'POST':

        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_ingredients = request.POST.get('receipe_ingredients')
        receipe_category = request.POST.get('receipe_category') 
        receipe_instructions = request.POST.get('receipe_instructions') 
        cooking_time = request.POST.get('cooking_time')
        receipe_author = request.POST.get('receipe_author')
        difficulty = request.POST.get('difficulty') 
        receipe_image = request.FILES.get('receipe_image')

        print(receipe_name)
        print(receipe_description) 
        print(receipe_ingredients)
        print(receipe_category)
        print(receipe_instructions)
        print(cooking_time)
        print(receipe_author)
        print(difficulty)
        print(receipe_image)
        

        receipe = Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_ingredients=receipe_ingredients,
            receipe_category=receipe_category,
            receipe_instructions=receipe_instructions,
            cooking_time=cooking_time,
            receipe_author=receipe_author,
            difficulty=difficulty,
            receipe_image=receipe_image,
        )
        receipe.save() 
        return redirect('recipes')
    return render(request,'recipes.html')
   
@login_required (login_url='login') 
def edit_receipe(request, recipe_id):
    receipe = get_object_or_404(Receipe, id=recipe_id)
    if request.method == 'POST': 
        receipe.receipe_name = request.POST.get('receipe_name')
        receipe.receipe_description = request.POST.get('receipe_description')
        receipe.receipe_ingredients = request.POST.get('receipe_ingredients')
        receipe.receipe_category = request.POST.get('receipe_category')
        receipe.receipe_instructions = request.POST.get('receipe_instructions')
        receipe.cooking_time = request.POST.get('cooking_time')
        receipe.receipe_author = request.POST.get('receipe_author')
        receipe.difficulty = request.POST.get('difficulty')
        receipe.receipe_image = request.FILES.get('receipe_image')
        receipe.save()
        return redirect('view_receipes')
    return render(request, 'edit_receipe.html', {'recipe': receipe}) 

@login_required (login_url='login') 
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('recipes')  
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('login') 

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name') 
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already exists')
            return render(request,'register.html')
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email) 
        user.set_password(password) 
        if password == confirm_password:
            user.save()
            messages.info(request,'User created successfully') 
            return redirect('login')
        else:
            messages.info(request,'Passwords do not match')
            return render(request,'register.html')
    return render(request,'register.html')

