from django.urls import path

from Product.views import (
    product_detail_view,
    dynamic_lookup_view,
    )

app_name ="product"
urlpatterns = [
    path('', product_detail_view, name='details'),
    path('<int:my_id>/', dynamic_lookup_view, name='product_details'),
]