from django.shortcuts import get_object_or_404, redirect
from rest_framework.renderers import TemplateHTMLRenderer, AdminRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from . import models

class PotionList(APIView):
	#queryset = models.Potion.objects.all()
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'potion_list.html'
	
	def get(self, request):
		queryset = models.Potion.objects.all()
		return Response({'potion': queryset})
	
