from django.shortcuts import render,HttpResponse,redirect
from .models import *
import random


# Create your views here.
def home(request):
    return render(request, 'home.html')

def createShortUrl(request):
    if request.method=='POST':
        long_url=request.POST['long_url']
        s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQUSTUVWXYZ1234567890!@#$^&*%+-?~"
        shorturl=("".join(random.sample(s,8)))
        obj=ShortUrl.objects.create(long_url=long_url,short_url=shorturl)
        print('Object Created')
        # print('Your Long URL is ',long_url)
        alpaurl="http://127.0.0.1:8000/"+shorturl
    # return HttpResponse("Your Long url is {} converted short url is {}".format(long_url,alpaurl))
    return render(request,'shortUrl.html',{'shorturl':alpaurl,'long_url':long_url})

def redirectUrl(request,shorturl):
    try:
        obj=ShortUrl.objects.get(short_url=shorturl)
    except ShortUrl.DoesNotExist:
        obj = None
    
    if obj is not None:
        print(obj.long_url)
        obj.count+=1
        obj.save()
        return redirect(obj.long_url)
    else:
        return HttpResponse('Check your URL')
