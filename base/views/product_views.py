from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.serializer import ProductSerializer
from base.models import Product

from rest_framework import status
from datetime import datetime

@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all() 
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProduct(request, pk):
    product = Product.objects.get(_id = pk)
    serializer = ProductSerializer(product,many = False)
    return Response(serializer.data)




    
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def createProduct(request):
    data = request.data
    product = Product.objects.create(
        user=request.user,
        name=data["name"],
        brand = data["brand"],
        category = data["category"],
        description= data["description"],
        rating= 0,
        numReviews= 0,
        price= data["price"],
        countInStock= data["countInStock"],
    )

    
    product.save()
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id = pk)
    
    product.user=request.user
    product.name=data["name"]
    product.brand = data["brand"]
    product.category = data["category"]
    product.description= data["description"]
    product.price= data["price"]
    product.countInStock= data["countInStock"]

    
    product.save()
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    print(pk)
    product = Product.objects.get(_id = pk) 
    print(product.name)

    product.delete()
    
    return Response("Product Deleted")

@api_view(["POST"])
def uploadImage(request):
    data = request.data
    product_id = data["product_id"]
    product = Product.objects.get(_id = product_id)

    product.image = request.FILES.get('image')
    product.save()
    return Response("Image Uploaded")