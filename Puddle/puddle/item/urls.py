from django.urls import path
#import all of the views for the item

from .import views  # . -> from current package / directory
    
app_name ='item'  #so i dont incude item in every url


urlpatterns = [
                    #name of the view and name of def
    path('<int:pk>/' , views.detail , name='detail'),
    path('category=<int:pk>/' , views.category , name='category'),
    path('new/' , views.new , name='new'),
    path('<int:pk>/delete' , views.delete ,name='delete'),
    path('<int:pk>/edit' , views.edit ,name='edit'),
    path('items' , views.items , name='items')
]

#import these url files to the main urls file(one in puddle)