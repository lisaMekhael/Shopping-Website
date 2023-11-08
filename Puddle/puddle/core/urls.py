from django.urls import path 
from .import views
from core.views import contact
from django.contrib.auth import views as auth_views
from .forms import LoginForm
#link between views (DB) and backend


app_name ='core'

urlpatterns=[
    path('', views.index , name='index'),
    path('contact/',contact ,name='contact'),
    path('signup/', views.signup , name='signup' ),  #add the hyperlink to the frontpage
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm) , name='login'),
]
