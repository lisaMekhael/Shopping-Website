from django.urls import path
#import all of the views for the item

from .import views  # . -> from current package / directory
    
app_name ='conversation'  #so i dont incude item in every url


urlpatterns = [
                    #name of the view and name of def
    path('new/<int:item_pk>/' , views.convo , name='convo'),  
    path('', views.inbox , name='inbox'),     
    path('<int:pk>/', views.detail , name='detail'),         
]

#import these url files to the main urls file(one in puddle)