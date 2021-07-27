from django import forms
from django.forms import widgets
from .models import Comment



class Comment_form(forms.ModelForm):
    
    class Meta:
        model = Comment()
        fields = ('name','email','body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form_control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }


# какие файлы нужны для новой форма - forms, views,urls, new.html

# каталог книг можно сдклать с комантами и оценками
# сравнение цен из разных магазинов веб портал
# vixie
# агрегаторы курсов 