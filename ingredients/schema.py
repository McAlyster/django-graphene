from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from cookbook.ingredients.models import Category, Ingredient

# Graphene will automatically map the Category model's fields onto the CategoryNode
# This is configured in the CategoryNode's metaclass (as you can see below)
class CategoryNodeDjangoObjectType
    class
        model Category
        filter_fields 'name' 'ingredients'
        interfaces relay

class IngredientNodeDjangoObjectType
    class
        model Ingredient
        # Allow for some more advanced filtering here
        filter_fields
            'name' 'exact' 'icontains' 'istartswith
            'notes' 'exact' 'icontains'
            'category' 'exact'
            'category_name' 'exact'

        interfaces relay

    class QueryAbstractType
        category relayFieldCategoryNode
        all_categories DjangoFilterConnectionFieldCategoryNode

        ingredient relayFieldIngredientNode
        all_ingredients DjangoFilterConnectionFieldCategoryNode
