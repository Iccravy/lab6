from models import Article
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
def archive(request):
   return render(request, 'archive.html', {"posts":Article.objects.all()})

def get_article(request, article_id):
 try:
    post = Article.objects.get(id=article_id)
    return render(request, 'article.html', {"post": post})
 except Article.DoesNotExist:
    raise Http404

def create_post(request):
 if not request.user.is_anonymous():
    if request.method == "POST":
      article = None
      # обработать данные формы, если метод POST
      form = {
        'text': request.POST["text"],
        'title': request.POST["title"]
        }
      try:
          article = Article.objects.get(title=form["title"])
          print (u"Название статьи существует")
      except Article.DoesNotExist:
          print (u"job")

        # в словаре form будет храниться информация, введенная пользователем
      if form["text"] and form["title"]:
         # если поля заполнены без ошибок
         article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
         return redirect('get_article', article_id=article.id)
         # перейти на страницу поста
      else:
         # если введенные данные некорректны
         form['errors'] = u"Не все поля заполнены"
         
         return render(request, 'create_post.html', {'form': form})
    else:
     # просто вернуть страницу с формой, если метод GET
     return render(request, 'create_post.html', {})
     # Здесь будет основной код представления
 else:
   raise Http404
