from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.permissions import IsAdminOrReadOnly


# Category CreateView
class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Category read, update, delete
class CategoryApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)

    def post(self, request, id):
        category = get_object_or_404(Category, id=id)
        products = category.products.all().select_related()
        serializer = ProductSerializer(products, many=True)

        result = {
            'status': True,
            'response': serializer.data
        }
        return Response(result)

    def put(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        result = {
            'status': True,
            'response': 'Category is updated!'
        }
        return Response(result)

    def delete(self, request, id):
        category = get_object_or_404(Category, id=id)
        category.delete()

        result = {
            'status': True,
            'response': 'Category is deleted!'
        }
        return Response(result)


# Product create and read
class ProductListCreateApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Product Update, delete, detail
class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




