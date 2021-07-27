from django.db import models
from django.db.models.fields import CharField

# Create your models here.

# тут создаются таблицы, наша база данных
# 

class Tag(models.Model):
    name = CharField(max_length=63)
    
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.URLField()
    # models.SET_NULL - все новости с тегом не удалятся  null - если нет тега то все норм не надо записыавать в дефолтное состояние  cascade delete - 
    # если удалить 1 то удалятся все которые были с этим тегом
    tag = models.ForeignKey(Tag,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

#makemigration - переводит с пайтона на sql и чтобы ее применить используем
# migration
