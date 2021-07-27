from django.contrib import admin
from .models import News, Tag

admin.site.register(News)
admin.site.register(Tag)
# зарегестрировали, если не сделать, то он не появится в админке

# что тут не зарегано, то не появится

# Register your models here.

# виртуальное окружение джанго скачал потом django-admin startproject (название) потом python3 manage.py startapp (название)
# потом переходим в settigs install apps и записываем название стартапа потом в models сделать таблицы импортируем все делаем красиво
# python3 manage.py makemigrations | migrate , потом создаем суперюзера теперь создаем страницу темплатес в папке темплатес /неус
# в доке виюс пау создаем функцию где аргуменрт request в urls.py пишем новую куйню и будет работать