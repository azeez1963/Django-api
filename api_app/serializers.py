from rest_framework import serializers, exceptions
from .models import Category, Product
from django.contrib.auth.models import User


class CategorySerializer(serializers.Serializer):
      id=serializers.IntegerField(read_only=True)
      name=serializers.CharField(max_length=50, min_length=4)


      def validate(self, attrs):
            name=attrs.get('name')
            if name == 'acid':
                  raise exceptions.ValidationError("please acid is not accepted category")
            return attrs

      def create(self, validated_data):
            return Category.objects.create(name=validated_data['name'])

      def update(self, instance, validated_data):
            instance.name=validated_data.get('name', instance.name)
            instance.save()
            return instance
      
class CreateProductSerializer(serializers.ModelSerializer):
      class Meta:
            model=Product
            fields=['product_name', 'description', 'price', 'discount_price', 'category', 'expire_date', 'production_date', 'product_img', 'rating']
      

class ProductSerializer(serializers.ModelSerializer):
      class Meta:
            model=Product
            fields=['id', 'product_name', 'description', 'price', 'discount_price', 'category','expire_date',]


class UserCreateSerializer(serializers.ModelSerializer):
      password=serializers.CharField(max_length=68, min_length=3, write_only=True)
      password2=serializers.CharField(max_length=68, min_length=3, write_only=True)
      class Meta:
            model=User
            fields=['username', 'email', 'password', 'password2']


      def validate(self, attrs):
            user=User.objects.filter(username=attrs.get('username'))
            if user.exists():
                  raise exceptions.ValidationError('user already exist try a different username')
            password1=attrs.get('password')
            password2=attrs.get('password2')
            if password1 != password2:
                  raise exceptions.ValidationError('password does not match')
            
            return attrs
      
      def create(self, validated_data):

            return User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
      