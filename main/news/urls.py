from django.urls import path
# НАДО ПРОСТО ИМПОРТИРОВАААААТЬ
from .views import news_detail, news, news_new, news_edit,news_delete,tag_detail_view,create_tag

urlpatterns = [
    # короче прикол в том что если у нас есть переход от корневого юрлс, и поэтому пишет news/news ААААААААААААА
    # правило хорошего тона дать атрибут name 
    # тут <> -заставляет искать эту переменнуб в базе данныъх 
    path('',news,name ='all_news'),
    path('<int:pk>/', news_detail, name='news_detail'),
    path('new/', news_new ,name='news_new'),
    path('<int:pk>/edit/', news_edit ,name='news_edit'),
    path('<int:pk>/delete/', news_delete, name='news_delete'),
    path('tag/<int:pk>/',tag_detail_view,name='news_by_tag'),
    path('tag/create/',create_tag,name='create_tag')
]
