from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_extensions.mixins import DetailSerializerMixin
from .models import *
#venv/lib/python3.11/site-packages/rest_framework/templates
class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'data']
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.HyperlinkedRelatedField(many=True,
                                                        view_name='subcategory-detail',
                                                        read_only=True)
    class Meta:
        model = Category
        fields = ['url',
        'name','description',
        'наименование','описание',
                  'subcategories',]
        extra_kwargs = {'name':{'source':'name_eng'},
                        'description':{'source':'description_eng'},
                        'наименование':{'source':'name_rus'},
                        'описание': {'source':'description_rus'}}


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(read_only=True)
    
    class Meta:
        model = SubCategory
        fields = ['url', 'name','category','cat1','description',
                  'наименование','описание',
                  'category',]
        extra_kwargs = {'name': {'source': 'name_eng'},
                        'description': {'source': 'description_eng'},
                        'наименование': {'source': 'name_rus'},
                        'описание': {'source': 'description_rus'},
                        'cat1':{'source':'category','label':'Category', 'write_only':True}
        }
        

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    subcategory = serializers.CharField(read_only=True)
    
    class Meta:
        model = Type
        fields = ['url', 'name', 'subcategory', 'sub1', 'description',
                  'наименование', 'описание',
                  ]
        extra_kwargs = {'name': {'source': 'name_eng'},
                        'description': {'source': 'description_eng'},
                        'наименование': {'source': 'name_rus'},
                        'описание': {'source': 'description_rus'},
                        'sub1': {'source': 'subcategory', 'label': 'Subcategory', 'write_only': True}
                        }
        
class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        exclude = ['datex','date1']
        
class BodySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Body
        exclude = ['datex','date1']
        
class ProductionMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductionMethod
        exclude = ['datex','date1']
        
 
class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Brand
        exclude = ['datex','date1']

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = ['datex','date1']

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    #regiones = serializers.HyperlinkedRelatedField(many=True,
    #                                                    view_name='region-detail',
    #                                                    read_only=True)
    
    # regiones = serializers.StringRelatedField(many=True) #,read_only=True)
    
    class Meta:
        model = Country
        fields = ['url','country', 'страна','regiones', 'description', 'описание']
        extra_kwargs = {'url':{'source':'url','read_only':True},
                        'country': {'source': 'name_eng'},
                        'description': {'source': 'description_eng'},
                        'страна': {'source': 'name_rus'},
                        'описание': {'source': 'description_rus'},
                        'regiones':{'read_only':True}}


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.CharField(read_only=True)
    class Meta:
        model = Region
        fields = ['url', 'region', 'country', 'state', 'description', 'регион', 'описание', 'state']
        extra_kwargs = {'url': {'source': 'url', 'read_only': True},
                        'region': {'source': 'name_eng'},
                        'description': {'source': 'description_eng'},
                        'регион': {'source': 'name_rus'},
                        'описание': {'source': 'description_rus'},
                        'country':{'read_only':True},
                        'state':{'source':'country', 'label':'Country','write_only':True}
                        }
        

class RawMaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RawMaterial
        exclude = ['datex','date1']

class VarietySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variety
        exclude = ['datex','date1']

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        exclude = ['datex','date1']


class PotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Potion
        exclude = ['datex','date1']


class ReadingLabelSerializer(serializers.HyperlinkedModelSerializer):
    #country  = CountryForeignSerializer(label='country')
    class Meta:
        model = ReadingLabel
        depth = 0
        exclude = ['datex', 'date1']
        