from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, exceptions, permissions
from .filters import ProductFilter
from django.contrib.auth.models import User
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, CreateProductSerializer, UserCreateSerializer
from rest_framework import generics 


# Create your views here.
# class CategoryEndpoint(APIView):
#       def get(self, request, *args, **kwargs):   # get category 
#             category=Category.objects.all()
#             serializer=CategorySerializer(category, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
      

#       def post(self, request, *args, **kwargs):       # add a new category
#             request.data
#             serializer=CategorySerializer(data=request.data)
#             if serializer.is_valid():
#                   serializer.save()  # calls the create or update method depending on the request type
#                   return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class UpgradedCategoryEndpoint(generics.ListCreateAPIView):
      queryset=Category.objects.all()
      serializer_class=CategorySerializer      

class SingleCategoryEndpoint(generics.RetrieveAPIView):
      queryset=Category.objects.all()
      serializer_class=CategorySerializer 
      lookup_field="pk"

class CategoryDeleteEndpoint(generics.DestroyAPIView):
      queryset=Category.objects.all()
      serializer_class=CategorySerializer 
      lookup_field="pk"

      
# class ProductEndpoint(APIView):
#       def get(self, request, *args, **kwargs):
#             products=Product.objects.all()
#             serializer=ProductSerializer(products, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
      

#       def post(self, request, *args, **kwargs):
#             request.data
#             serializer=CreateProductSerializer(data=request.data)
#             if serializer.is_valid():
#                   serializer.save()
#                   return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class ProductListEndpoint(generics.ListAPIView):
      serializer_class=ProductSerializer
      queryset=Product.objects.all()
      # permission_classes=permissions.IsAuthenticated

      def get_queryset(self):
            queryset=super().get_queryset()
            category=self.request.query_params.get('category')
            queryset.filter()
            if category is not None:
                  queryset=queryset.filter(category__name=category)
            return queryset
      

class UpgradedProductEndpoint(generics.ListCreateAPIView):
      queryset=Product.objects.all()
      serializer_class=CreateProductSerializer    
      


class ProductDetailEndpoint(APIView):
      def get_object(self, pk):
            try:
                  product=Product.objects.get(id=pk)
                  return product
            except Product.DoesNotExist:
                  raise exceptions.NotFound(f'product with this id: {pk} does not exist')



      def get(self, request, *args, **kwargs):
            product=self.get_object(self.kwargs['product_id'])
            serializer=ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
      
      def put(self, request, *args, **kwargs):
            product=Product.objects.get(self.kwargs['product_id'])
            serializer=CreateProductSerializer(instance=product, data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      def delete(self, request, *args, **kwargs):
            product=Product.objects.get(self.kwargs['product_id'])
            product.delete()
            return Response({'message':'product deleted successfully'}, status=status.HTTP_200_OK)


# class UserRegisterEndpoint(generics.CreateAPIView):
#       queryset=User.objects.all()
#       permission_classes=[permissions.AllowAny]
#       serializer_class=UserCreateSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def product_list(self, request, *args, **kwargs):
            queryset=Product.objects.all()
            filterset_class=ProductFilter

            
