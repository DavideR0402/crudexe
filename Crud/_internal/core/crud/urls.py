from django.urls import path # type: ignore
from . import views

app_name = 'crud'

urlpatterns = [
    ## rutas de los datos de los productos
    path('register/', views.register_product, name='register'),
    path('list/', views.get_product, name='list'),
    path('update/<int:pk>/', views.update_product, name='update'),
    path('delete/<int:pk>/', views.delete_product, name='delete'),
]
