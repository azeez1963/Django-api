from django.db import models

# Create your models here.

class Category(models.Model):
      name=models.CharField(max_length=20)

      def __str__(self) -> str:
            return self.name


class Product(models.Model):
      RATING_CHOICE=(
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5")
      )
      
      product_name=models.CharField(max_length=150)
      description=models.TextField()
      price=models.DecimalField(max_digits=20, decimal_places=2)
      discount_price=models.DecimalField(max_digits=20, decimal_places=2)
      category=models.ForeignKey(Category, on_delete=models.CASCADE)
      expire_date=models.DateField()
      production_date=models.DateField()
      product_img=models.ImageField(upload_to='product')
      rating=models.IntegerField(choices=RATING_CHOICE)


      def __str__(self) -> str:
            return self.product_name