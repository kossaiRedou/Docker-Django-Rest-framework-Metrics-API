from django.urls import path
from .views import list_datasets, upload_dataset, top_products

urlpatterns = [
    path('datasets/', list_datasets),
    path('datasets/upload/', upload_dataset),
    path('datasets/<int:dataset_id>/top-products/', top_products),
]
