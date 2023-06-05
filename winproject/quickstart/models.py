from django.db import models
from django.db.models import UniqueConstraint
from . modelsabs import StdDateX, StdMultiLang, StdUrl

class Category(StdDateX, StdMultiLang, StdUrl):
	"""
	categories of drinks (wine, beer, hard liquor, Cider
	"""
	
	class Meta:
		verbose_name = 'Категория напитка'
		verbose_name_plural = 'Категории напитков'
		ordering = ('name_eng',)
		constraints = [
			UniqueConstraint(name='category_unique_index', fields=['name_rus', 'name_eng']) #, include=['full_name'])
		]
	
	def __str__(self):
		return '%s: %s' % (self.name_eng, self.name_rus)

class SubCategory(StdDateX, StdMultiLang, StdUrl):
	"""
	subcategory of drink (Whiskey, Vodka, Vermouth, Porto, Wine, ...
	"""
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                             db_column='сategory', verbose_name='Сategory', related_name='subcategories')
	
	class Meta:
		verbose_name = 'Тип напитка'
		verbose_name_plural = 'Типы напитков'
		constraints = [
			UniqueConstraint(name='subcategory_unique_index', fields=['name_rus', 'name_eng', 'category'])  # , include=['full_name'])
		]

	def __str__(self):
		return f'{self.category.name_eng or self.category.name_rus} / {self.name_eng or self.name_rus}'
				#'%s: %s' % (self.name_eng, self.name_rus)

class Type(StdDateX, StdMultiLang, StdUrl):
	"""
	RED/WHITE/ROSE/BLEND/MALT/DARK/LAGER/...
	"""
	subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                                db_column='subcategory', verbose_name='Sub Category')
	
	class Meta:
		verbose_name = 'Тип'
		verbose_name_plural = 'Типы'
		constraints = [
			UniqueConstraint(name='type_unique_index', fields=['name_rus', 'name_eng', 'subcategory'])  # , include=['full_name'])
		]

class Color(StdDateX, StdMultiLang, StdUrl):
	"""
	"""
	type = models.ForeignKey(Type, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                         db_column='type', verbose_name='Type of drink')
	
	class Meta:
		verbose_name = 'Color'
		verbose_name_plural = 'Colors'
		constraints = [
			UniqueConstraint(name='color_unique_index', fields=['name_rus', 'name_eng', 'type'])  # , include=['full_name'])
		]


class Body(StdDateX, StdMultiLang, StdUrl):
	class Meta:
		verbose_name = 'Wine Bod'
		verbose_name_plural = 'Wine Bodies'
		constraints = [
			UniqueConstraint(name='body_unique_index', fields=['name_rus', 'name_eng'])  # , include=['full_name'])
		]

class ProductionMethod(StdDateX, StdMultiLang, StdUrl):
	class Meta:
		verbose_name = 'Способ производства'
		verbose_name_plural = 'Способы производства'
		constraints = [
			UniqueConstraint(name='prod_unique_index', fields=['name_rus', 'name_eng'])  # , include=['full_name'])
		]


class Brand(StdDateX, StdMultiLang, StdUrl):
	class Meta:
		verbose_name = 'Бренд'
		verbose_name_plural = 'Бренды'
		constraints = [
			UniqueConstraint(name='brand_unique_index', fields=['name_rus', 'name_eng'])  # , include=['full_name'])
		]

class Manufacturer(StdDateX, StdMultiLang, StdUrl):
	brand = models.ForeignKey(Category, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                          db_column='brand', verbose_name='Brand')
	
	class Meta:
		verbose_name = 'Производитель'
		verbose_name_plural = 'Производители'
		constraints = [
			UniqueConstraint(name='man_unique_index', fields=['name_rus', 'name_eng', 'brand'])  # , include=['full_name'])
		]

class Country(StdDateX, StdMultiLang, StdUrl):
	class Meta:
		verbose_name = "Страна происхождения"
		verbose_name_plural = "Страны происхождения"
		ordering = ('name_eng',)
		constraints = [
			UniqueConstraint(name='country_unique_index', fields=['name_rus', 'name_eng'])  # , include=['full_name'])
		]
	def __str__(self):
		return f'{self.name_eng or self.name_rus}'

class Region(StdDateX, StdMultiLang, StdUrl):
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                            db_column='country', verbose_name='country', related_name='regiones')
	
	class Meta:
		verbose_name = "Регион происхождения"
		verbose_name_plural = "Регионы происхождения"
		constraints = [
			UniqueConstraint(name='reg_unique_index', fields=['name_rus', 'name_eng','country'])  # , include=['full_name'])
		]

class RawMaterial(StdDateX, StdMultiLang, StdUrl):
	"""
	grapes, rice, peach, corn, barley etc.
	"""
	
	class Meta:
		verbose_name = "Сырье"
		verbose_name_plural = "Сырье"
		constraints = [
			UniqueConstraint(name='raw_unique_index', fields=['name_rus', 'name_eng'])  # , include=['full_name'])
		]

class Variety(StdDateX, StdMultiLang, StdUrl):
	"""
	сорта виноматериалов
	"""
	raw = models.ForeignKey(Country, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                        db_column='rawmaterial', verbose_name='Raw Material')
	
	class Meta:
		verbose_name = "Сорт"
		verbose_name_plural = "Сорта"
		constraints = [
			UniqueConstraint(name='var_unique_index', fields=['name_rus', 'name_eng'])  # , include=['full_name'])
		]

class Food(StdDateX, StdMultiLang, StdUrl):
	"""
	type of food
	"""
	
	class Meta:
		verbose_name = "Гастрономия"
		verbose_name_plural = "Гастрономия"
		ordering = ('name_eng',)
		constraints = [
			UniqueConstraint(name='food_unique_index', fields=['name_rus', 'name_eng'])  # , include=['full_name'])
		]


class Potion(StdDateX, StdMultiLang, StdUrl):

	type = models.ForeignKey(Type, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                         db_column='type', verbose_name='Type',
	                         related_name='wine_type')
	
	region = models.ForeignKey(Region, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                                db_column='region', verbose_name='Region')
	
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                                 db_column='manufacturer', verbose_name='Manufacturer')
	
	productionmethod = models.ForeignKey(ProductionMethod, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                                db_column='productionmethod', verbose_name='Production Method')
	
	variety = models.ForeignKey(Variety, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                            db_column='variety', verbose_name='Variety of Raw Material')
	
	alcohol = models.PositiveIntegerField(null=True, blank=True, unique=False,
	                                      db_column='alcoholvolume', verbose_name='Alcohol by volume')
	
	sugar = models.PositiveIntegerField(null=True, blank=True, unique=False,
	                                      db_column='sugarvolume', verbose_name='Sugar by volume')
	
	color = models.ForeignKey(Color, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                          db_column='color', verbose_name='Color')
	
	bod = models.ForeignKey(Body, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                        db_column='winebod', verbose_name='Wine bod')
	
	food = models.ManyToManyField('Food', blank=True, db_column='food', verbose_name='Food',
                                    related_name='potion_food')
	year = models.PositiveIntegerField(null=True, blank=True, unique=False,
	                                      db_column='year', verbose_name='Year')

	class Meta:
		verbose_name = 'Напиток'
		verbose_name_plural = 'Напитки'
		constraints = [
			UniqueConstraint(name='potion_unique_index', fields=['name_rus', 'name_eng','year','region','manufacturer'])  # , include=['full_name'])
		]


class ReadingLabel(StdMultiLang, StdDateX):
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, db_index=True, null=True, blank=True,
	                            db_column='country', verbose_name='Country')
	class Meta:
		verbose_name = "Терминология"
		verbose_name_plural = "Терминология"
		ordering = ('name_eng',)
		constraints = [
			UniqueConstraint(name='label_unique_index', fields=['name_rus', 'name_eng'])  # , include=['full_name'])
		]
