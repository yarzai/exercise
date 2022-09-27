
from django.urls import path
from products.views import list_products, create_product, delete_product, update_product


app_name = 'products'

urlpatterns = [
    path("", list_products, name='list'),
    path("create/", create_product, name='create'),
    path("delete/<int:prod_id>/", delete_product, name="delete"),
    path("update/<int:prod_id>/", update_product, name='update'),

]
