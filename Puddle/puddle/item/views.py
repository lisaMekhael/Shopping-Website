from django.shortcuts import render,get_object_or_404 , redirect
from .models import Item , Category
from .forms import NewItemForm , EditItemForm
from django.contrib.auth.decorators import login_required

from django.db.models import Q
# Create your views here.

#user cannot see details of the page
#call objects from db(choose which ones we want)
#connect the DB to the HTML?!

# def items(request , pk):
#     query = request.GET.get('query' , '')
#     items = Item.objects.filter(is_sold = False)
#     categories = Category.objects.all()
#     get_cat = get_object_or_404(Category , pk=pk)

#     related_cat = Item.objects.filter(category = get_cat.name , is_sold = False )

#     if query:
#         items = items.filter(Q(name__icontains = query) | Q(descrip_iconatins= query))

#     return render(request , 'item/items.html' , {
#         'items' : items,
#         'query' : query,
#         'categories' : categories,
#         'related_cat' : related_cat
#     })

def items(request):
    query = request.GET.get('query' , '')
    items = Item.objects.filter(is_sold = False)
    categories = Category.objects.all()

    if query:
        items = items.filter(Q(name__icontains = query) | Q(descrip__icontains= query))

    return render(request , 'item/items.html' , {
        'items' : items,
        'categories' : categories,
        'query' : query,
        })

def category(request , pk):
    category = get_object_or_404(Category , pk=pk)
    items = Item.objects.filter(category = category , is_sold = False )

    return render(request , 'item/category.html',{
        'category' : category,
        'items' : items,
    })


def detail(request,pk ):
    item = get_object_or_404(Item , pk=pk)
    related_items = Item.objects.filter(category =item.category , is_sold = False ).exclude(pk=pk)[0:3]

# render is used to render an HTML template and return it as an HTTP response. 
# It is typically used when you want to generate an HTML page that includes data from your Django views and templates.

    return render(request , 'item/detail.html',{ #append
        'item' : item,
        'related_items' : related_items  #send to the html 
    })

@login_required
def new(request):
    if request.method== 'POST':
        form = NewItemForm(request.POST , request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    return render(request , 'item/form.html',{
        'form' : form,
        'tile' : 'New Item'
    })

@login_required
def delete(request , pk):
    item = get_object_or_404(Item , pk=pk , created_by = request.user) 
    item.delete()
    
    return redirect('dashbaord:index')

@login_required
def edit(request , pk):
    item = get_object_or_404(Item , pk=pk , created_by = request.user) 
 
    if request.method== 'POST':
        form = EditItemForm(request.POST , request.FILES , instance=item)

        if form.is_valid():
           form.save()
           return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request , 'item/form.html',{
        'form' : form,
        'tile' : 'Edit Item'
    })