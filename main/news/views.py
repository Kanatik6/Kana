from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseNotFound
from django.utils.translation import activate
from .models import News, Tag 
from .forms import NewsFormTag, NewsFrom
from comments.forms import Comment_form
# точка озночает что импортируем из этой же папки

# Create your views here.


# тут мы пишем чтото чтобы показывало в htmlке
# пишем путь к нашему html

def news(request):
    # получили все обьекты статьи
    news = News.objects.all()
    tags = Tag.objects.all()
    # принимает несколько аргументов сначала реквест который принимает запросы, потом путь, а дальше все значения которые нужно ловить
    return render(request,'news/news.html',
    {'all_news':news,
    'all_tags':tags})
    # в сеттигсе нужно писать в дирсе название папки темплатес 
    # тут можно получить еще и теги


# pk - primary key - айдишка у всех
def news_detail(request,pk):
    one_news = get_object_or_404(News,pk=pk)
    # comments = news_detail.comments.filter(activate=True)
    # if request.method == 'POST':
    #     comment_form =  Comment_form(request.POST)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.post = news_detail
    #         new_comment.save()
    #     else:
    #         comment_form = Comment_form()
    return render(request,'news/news_detail.html',{'news_detail':one_news,
                                                    })



# post - запрос на создание 
def news_new(request):
    if request.method == 'POST':
        form = NewsFrom(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news_detail',pk=news.pk)
    else:
        form = NewsFrom()
    return render(request,'news/news_edit.html',{'form':form})
    # http.method() = post - отправить| update delete |get - получить 

def news_edit(request,pk):
    news = get_object_or_404(News,pk=pk)
    if request.method == "POST":
        form = NewsFrom(request.POST,instance=news)
        if form.is_valid():
            news.form.save(commit=False)
            news.save()
            return redirect('news_detail',pk=news.pk)
    else:
        form = NewsFrom(instance=news)
    return render(request,'news/news_edit.html',{'form':form})

def news_delete(request,pk):
    try:
        news = News.objects.get(id=pk)
        news.delete()
        return redirect('all_news')
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>News not found<h2>")

def tag_detail_view(request,pk):
    tag = get_object_or_404(Tag,id=pk)
    news_by_tag = tag.news_set.all()
    return render(request,'news/news_by_tag.html',{'news_by_tag':news_by_tag})

def create_tag(request):
    if request.method == 'POST':
        form = NewsFormTag(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news_new')
            # редирект это куда отправит в случае удачного использования 
    else:
        form = NewsFormTag()
    return render(request,'news/create_tag.html',{'form':form})



# вьюшки делают логику
# контроллер - темплайтс (шаблоны) что отображает html 
# если фирма использует unittest - значит это хорошая фирма