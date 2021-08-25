from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def articles_list(request):
    # return render(request,'articles/articlelist.html')

    arti=models.Articles.objects.all().order_by('-date')
    arg={'maghale':arti}
    return render (request,'articles/articlelist.html',arg )

def article_detail(request, slug):
    # return HttpResponse(slug)
# show slug Variable in new page
    article=models.Articles.objects.get(slug=slug)
    return render(request,'articles/article_det.html',{'article':article})

@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method=='POST':
        form=forms.ArticleCreate(request.POST,request.FILES)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:list')

    else:
        form=forms.ArticleCreate()

    return render(request,'articles/article_create.html',{'form':form})
