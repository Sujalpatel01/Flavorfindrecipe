import urllib.request
import json
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import ContactMessage

def fetch_api(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"API Error fetching {url}: {e}")
        return None

SIDEBAR_CATEGORIES = {
    'Dish Type': [
        ('Pizza', 'Pizza'), ('Pasta', 'Pasta Recipes'), ('Salad', 'Salads'), 
        ('Soup', 'Soups'), ('Sandwich', 'Sandwiches'), ('Cookies', 'Cookies & Biscuits'), 
        ('Baking', 'Baking'), ('Salsa', 'Salsa & Dips'),
    ],
    'Meal Type': [
        ('Breakfast', 'Breakfast & Brunch'), ('Lunch', 'Lunch'), 
        ('Dinner', 'Dinner'), ('Dessert', 'Dessert'),
    ],
    'Diet and Health': [
        ('Vegetarian', 'Vegetarian'), ('Quick', 'Quick & Easy'),
    ],
    'World Cuisine': [
        ('Italian', 'Italian'), ('Indian', 'Indian'), ('Pakistani', 'Pakistani'), 
        ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Greek', 'Greek'), 
        ('Turkish', 'Turkish'), ('Mexican', 'Mexican'), ('Spanish', 'Spanish'), 
        ('Vietnamese', 'Vietnamese'), ('Lebanese', 'Lebanese'), 
        ('Brazilian', 'Brazilian'), ('Cuban', 'Cuban'), ('Moroccan', 'Moroccan'),
    ]
}

def get_recipes_page(request, url):
    sort_by = request.GET.get('sort', 'Latest')
    api_data = fetch_api(url)
    recipes = api_data.get('recipes', []) if api_data else []
    
    if sort_by == 'Top Rated':
        recipes.sort(key=lambda r: r.get('rating', 0), reverse=True)
    elif sort_by == 'Trending':
        recipes.sort(key=lambda r: r.get('reviewCount', 0), reverse=True)
    elif sort_by == 'Latest':
        recipes.sort(key=lambda r: r.get('id', 0), reverse=True)
        
    paginator = Paginator(recipes, 9)
    return paginator.get_page(request.GET.get('page', 1)), sort_by

def index(request):
    page_obj, sort_by = get_recipes_page(request, 'https://dummyjson.com/recipes?limit=0')
    return render(request, 'index.html', {
        'page_obj': page_obj,
        'sidebar_categories': SIDEBAR_CATEGORIES,
        'selected_sort': sort_by,
    })

def search_recipes(request):
    q = request.GET.get('q', '')
    tag = request.GET.get('tag', '')
    
    if tag:
        url = f'https://dummyjson.com/recipes/tag/{tag}?limit=0'
    elif q:
        url = f'https://dummyjson.com/recipes/search?q={q}&limit=0'
    else:
        return redirect('index')
        
    page_obj, sort_by = get_recipes_page(request, url)
    return render(request, 'search.html', {
        'page_obj': page_obj,
        'q': q,
        'tag': tag,
        'selected_sort': sort_by,
        'sidebar_categories': SIDEBAR_CATEGORIES,
    })

def recipe_detail(request, recipe_id):
    recipe = fetch_api(f'https://dummyjson.com/recipes/{recipe_id}')
    if not recipe:
        return render(request, '404.html', status=404)
        
    recs_data = fetch_api('https://dummyjson.com/recipes?limit=4')
    return render(request, 'recipe.html', {
        'recipe': recipe,
        'recommendations': recs_data.get('recipes', []) if recs_data else [],
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('_replyto', '')
        message = request.POST.get('message', '')
        
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        messages.error(request, "Please fill out all fields.")
            
    return render(request, 'contact.html')

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {u}!")
            return redirect('index')
        messages.error(request, "Invalid username or password.")
        
    return render(request, 'sign-in.html')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        u = request.POST.get('username', '').strip()
        e = request.POST.get('email', '').strip()
        p = request.POST.get('password', '')
        cp = request.POST.get('confirm_password', '')
        
        if not u or not e or not p:
            messages.error(request, "Please fill out all required fields.")
        elif p != cp:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=u).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=e).exists():
            messages.error(request, "An account with this email already exists.")
        else:
            user = User.objects.create_user(username=u, email=e, password=p)
            login(request, user)
            messages.success(request, "Account created successfully! Welcome to Kocina.")
            return redirect('index')
            
    return render(request, 'sign-up.html')

def sign_out(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')
