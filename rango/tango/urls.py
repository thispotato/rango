from django.urls import path
from . import views

app_name = 'tango'

urlpatterns = [
    path('' , views.index , name='index'), 
    path('add_category/' , views.add_category , name = 'add_category'),
    path('add_page/<slug:category_slug>/' , views.add_page , name = 'add_page'), 
    path('category/<slug:category_slug>/' , views.show_category , name = 'show_category'),
    path('page/<slug:page_slug>/' , views.show_page , name = 'show_page'),  
]
