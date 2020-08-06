from django.db import models

# Create your models here.
'''
	Задаём курс: сначала названия блоков через | потом названия внутренности блоков между собой делим плюсом, между блоками | .
	Тип внутренности блока: если теория, то teo:<имя страницы теории>, если практика, то pr:Название задачи или id задачи, img:id картинки через %*%
'''


class Course(models.Model):
	teacher = models.IntegerField()
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=150)
	blocks = models.CharField(max_length=10000000)
	blocks_inner = models.CharField(max_length = 100000000000000000000000000000)

class Teo(models.Model):
	text = models.CharField(max_length = 1000000000000000000000000)

