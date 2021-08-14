from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    # return render(request,'articles/articlelist.html')

    arti=models.Articles.objects.all().order_by('date')
    arg={'maghale':arti}
    return render (request,'articles/articlelist.html',arg )
