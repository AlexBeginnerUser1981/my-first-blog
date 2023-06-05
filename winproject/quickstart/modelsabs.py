from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# ----------abstract models----------------
class StdModel(models.Model):
	objects = models.Manager()
	
	class Meta:
		abstract = True
	
	def __iter__(self):
		for field in self._meta.fields:
			value = getattr(self, field.name, None)
			yield field.verbose_name, field.name, value


class StdUrl(models.Model):
	uri = models.URLField(null=True, blank=True, db_column='uri', verbose_name='url')
	class Meta:
		abstract = True

class StdDesc(StdModel):
	description = models.TextField(null=True, blank=True, default=None,
	                               db_column='description', verbose_name='description')
	
	class Meta:
		abstract = True


class StdDateX(StdModel):
	# CHANGE DATE
	datex = models.DateTimeField(auto_now=True, db_column='datex', null=True, blank=True)
	# CREATE DATE
	date1 = models.DateTimeField(auto_now_add=True, db_column='datea', null=True, blank=True)
	
	class Meta:
		abstract = True


# ----------abstract lang models--------------
class StdRus(StdModel):
	name_rus = models.CharField(max_length=255, null=True, unique=False,
	                        db_column='name_rus', db_index=True, verbose_name='наименование')
	description_rus = models.TextField(null=True, blank=True, default=None,
	                               db_column='description_rus', verbose_name='описание')
	
	
	class Meta:
		abstract = True


class StdEng(StdModel):
	# english
	name_eng = models.CharField(max_length=255, null=False, unique=False, default='default',
	                           db_column='name_eng', verbose_name='name', db_index=True)
	description_eng = models.TextField(null=True, blank=True, default=None,
	                                  db_column='description_eng', verbose_name='description')
	
	class Meta:
		abstract = True


class StdFra(StdModel):
	# francaise
	name_fra = models.CharField(max_length=255, null=True, unique=False,
	                           db_column='name_fr', verbose_name='nom', db_index=True)
	description_fra = models.TextField(null=True, blank=True, default=None,
	                                  db_column='description_fr', verbose_name='description')
	
	class Meta:
		abstract = True



class StdMultiLang(StdRus, StdEng, StdFra):
	class Meta:
		abstract = True
		ordering = ('-nameeng',)
		
	def __str__(self):
		# this very importatn thing! for the right veiw of combo readable-view
		return f'{self.name_eng or self.name_rus}'