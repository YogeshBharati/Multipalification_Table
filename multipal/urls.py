from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='homepage'),
    path('<int:number>',views.multiply,name='multi'),

]