from django.urls import path
from Hello import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup_user,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_password/',views.change_password,name='change_password'),
]