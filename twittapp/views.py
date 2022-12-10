from os import stat
from django.http import  JsonResponse
from django.shortcuts import render, redirect

from .forms import TwittForm
from .models import Twitt

def home_view(request, *arg, **kwargs):
    return render(request, "pages/home.html", context = {}, status = 200)

def twitt_create_view(request, *arg, **kwargs):
    form = TwittForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form = TwittForm()
    return render(request, 'components/form.html', context={"form" : form})

def twitt_list_view(request, *arg, **kwargs):
    queryset = Twitt.objects.all()
    twitt_list = [{"id" : x.id, "content": x.content, "likes": x.likes} for x in queryset]
    data = {
        "isUser" : False,
        "response" : twitt_list
    }
    
    return JsonResponse(data)

def twitt_detailed_view(request, twitt_id, *args, **kwargs):
    data = {
        "id" : twitt_id
    }
    status = 200
    try:
        obj = Twitt.objects.get(id = twitt_id)
        data['content'] = obj.content
    except:
        data['message'] = "content doest not exist."
        status = 404
    
    return JsonResponse(data, status = status)
