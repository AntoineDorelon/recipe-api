from rest_framework import serializers

from core.models import Tag, Ingredient

class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredients bjects"""

    class Meta:
        model : Ingredient
        fiels = ('id', 'name')
        read_only_fields = ('id',)