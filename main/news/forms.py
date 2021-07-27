from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import News,Tag

# тут мы прописываем форма и это более легкая форма админки 
# если ты добавил в модели чтото, но не добавил в формы, то оно не отобразится

class NewsFrom(forms.ModelForm):
    
    class Meta:
        model = News
        fields = ('title','text','img','tag')
        # тут он отправляет  в html 

        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'text':forms.Textarea(attrs={'class':'form-control'}),
        'img': forms.URLInput(attrs={'class':'form_control'}),
        }

class NewsFormTag(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }





# у меня вопрос, можно ли сделать хоткеи, чтобы например на "команд + l" =  = list() 