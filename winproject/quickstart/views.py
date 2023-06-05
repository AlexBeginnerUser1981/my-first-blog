from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework_extensions.mixins import NestedViewSetMixin

from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-last_login')
        
        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)
    

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name_eng')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all().order_by('name_eng')
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all().order_by('name_eng')
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all().order_by('name_eng')
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticated]

class BodyViewSet(viewsets.ModelViewSet):
    queryset = Body.objects.all().order_by('name_eng')
    serializer_class = BodySerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductionMethodViewSet(viewsets.ModelViewSet):
    queryset = ProductionMethod.objects.all().order_by('name_eng')
    serializer_class = ProductionMethodSerializer
    permission_classes = [permissions.IsAuthenticated]




class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('name_eng')
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('name_eng')
    serializer_class = ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]

class CountryViewSet(NestedViewSetMixin,viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('name_eng')
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

class RegionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Region.objects.all().order_by('name_eng')
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]

class RawMaterialViewSet(viewsets.ModelViewSet):
    queryset = RawMaterial.objects.all().order_by('name_eng')
    serializer_class = RawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

class VarietyViewSet(viewsets.ModelViewSet):
    queryset = Variety.objects.all().order_by('name_eng')
    serializer_class = VarietySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all().order_by('name_eng')
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class PotionViewSet(viewsets.ModelViewSet):
    queryset = Potion.objects.all().order_by('name_eng')
    serializer_class = PotionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
#class PotionXlsViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
#    queryset = Potion.objects.all().order_by('name_eng')
#    serializer_class = PotionSerializer
#    renderer_classes = [XLSXRenderer]
#    filename = 'my_export.xlsx'
    
class ReadingLabelViewSet(viewsets.ModelViewSet):
    queryset = ReadingLabel.objects.all().select_related('country').order_by('name_eng')
    serializer_class = ReadingLabelSerializer
    permission_classes = [permissions.IsAuthenticated]