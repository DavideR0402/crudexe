from rest_framework import status  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.decorators import api_view, authentication_classes, permission_classes # type: ignore
from rest_framework.authentication import TokenAuthentication # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from .serializers import ProductSerializer
from .forms import ProductValidator
from .models import Product
# Create your views here.


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_product (request):
    """
        Get all Product
        :param request: Request object
        :type request: HttpRequest
        :return: Response object
        :rtype: HttpResponse
    """
        
    try:
        product = Product.objects.all()
        
        data = []
        for products in product:
            item = {
                "id": product.id,
                "product": products.product,
                "price": products.price
            }    
            data.append(item)
                            
        return Response(data)
    except:
        message = {"detail": "No hay productos registrados"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def register_product(request):
    
    """
        Register a new Product

        :param request: Request object
        :type request: HttpRequest
        :return: Response object
        :rtype: HttpResponse
        :raises IntegrityError: If the product already exists
        :raises Exception: If there is an error when registering the product
    """
    try:
        data = request.data
        defaults = {
            'product': data.get('product'),
            'price': data.get('price'),           
        }
        
        Assembly = Product.objects.create(**defaults) 
        serializer = ProductSerializer(Assembly, many=False) 
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    except Exception as e:
        message = {
            'detail': f'Error al registrar el producto: {str(e)}'}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  
    
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_product(request, pk):
    """
        Update a product by id

        :param request: Request object
        :type request: HttpRequest
        :param pk: Product id
        :type pk: int
        :return: Response object
        :rtype: HttpResponse

    """
    try:
        data = request.data
        product_validator = ProductValidator(data)
        if product_validator.is_valid():
            product = Product.objects.get(id=pk)
            product.product = data['product']
            product.save()
            serializer = ProductSerializer(product, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {
                'detail': 'El nombre solo puede contener letras, espacios y acento'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except:
        message = {'detail': 'El regimen no existe'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_product(request, pk):
    """
        Delete a product by id

        :param request: Request object
        :type request: HttpRequest
        :param pk: Product id
        :type pk: int
        :return: Response object
        :rtype: HttpResponse

    """
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        message = {'detail': 'El product ha sido eliminado'}
        return Response(message, status=status.HTTP_200_OK)
    except:
        message = {'detail': 'El product no existe'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)    