from rest_framework import serializers #type: ignore
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    """
        ProductSerializer Class

        Serializer for Product model

    """    
    class Meta:
        model = Product
        fields = '__all__'
        
    def to_representation(self, instance):
        
        """ 
            to_representation method in ProductSerializer class

            :param instance: Product object
            :type instance: Product
            :return: Product object
            :rtype: Product
            :raises: None
        """
    
        return super(ProductSerializer, self).to_representation(instance)    
