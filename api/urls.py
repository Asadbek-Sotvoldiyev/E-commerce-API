from django.urls import path
from .views import (CategoryApiView, CategoryCreateApiView, ProductListCreateApiView,
                    ProductRetrieveUpdateDestroyView)


urlpatterns = [
    #category
    path('categories/', CategoryApiView.as_view()),
    path('categories/<int:id>/', CategoryApiView.as_view()),
    path('add-category/', CategoryCreateApiView.as_view()),

    #product
    path('product-list-create/', ProductListCreateApiView.as_view()),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),
]