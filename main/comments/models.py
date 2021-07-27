from django.db import models

from news.models import News

class Comment(models.Model):
    post = models.ForeignKey(News,on_delete=models.SET_NULL,null=True,related_name='comments')
    # ФОРЕНКИ ДЕЛАЕМ ТАМ ГДЕ ЗАВИСИМЫЙ
    # то есть, если есть пост и комменты, то комментов больше, то форенки делается у коммента
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    # если не работает майкмигратионс, то нужно перейти в сеттингс инсталлед аппс
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'