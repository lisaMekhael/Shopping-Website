from django.shortcuts import redirect, render
from item.models import Category , Item
from .forms import SignupForm
# Create your views here.

#CONNECTION BETWEEN DATABASE AND FRONTEND
#show my items and categories on the front page

def index(request):#all def return HTML pages 
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    #list of items
    return render(request , 'core/index.html' , {
        'categories' : categories ,  #as in def index
        'items' : items , 
    })

def contact(request):
    return render(request , 'core/contanct.html')

def signup(request):
    if request.method =='POST':
        form= SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm 

    return render( request ,'core/signup.html' ,{
    'form' : form
    })
    
