from django.shortcuts import render
from .models import Category , Page
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from .forms import CategoryForm , PageForm

def index(request):
    categories = Category.objects.all()
    page = request.GET.get('page' , 1)
    paginator = Paginator(categories , 3)

    #check the current page
    try:
        results = paginator.page(page)

    #If page is not an integer, return to first page
    except PageNotAnInteger:
        results  = paginator.page(page)
    
    #if next page is empty, return to the last page of the paginator
    except EmptyPage:
        results  = paginator.page(paginator.num_pages)

    homepage_title = "Welcome Here"
    return render(request , 'tango/index.html' , locals())

def show_category(request , category_slug):
    try:
        category = Category.objects.get(slug = category_slug)
        page = Page.objects.filter(category = category)
    except Category.DoesNotExist:
        category = "Does not Exist"
        page = None

    return render(request , 'tango/category.html' , locals())

def show_page(request , page_slug):
    try:
        page = Page.objects.get(slug = page_slug)
    except Page.DoesNotExist:
        page = "Page does Not Exist"
    
    return render(request , 'tango/page_view.html' , locals())

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save(commit = True)
            return index(request)

    else:
        print(form.errors)
    
    return render(request , 'tango/add_category.html' , locals())

def add_page(request, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)
    except Category.DoesNotExist:
        category = None
   
    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit = False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request , category_slug)
        else:
            print(form.errors)

    return render(request , 'tango/add_page.html' , locals())