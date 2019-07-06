from django.shortcuts import render,redirect
from .models import *
from .forms import *

def add(request):
	if request.method=="POST":
		form=DiaryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
	    form=DiaryForm()
	context={'form':form}
	return render(request,'add.html',context)


def reset(request):
    Diary.objects.all().delete()
    return render(request,'index.html')


def index(request):
	entries=Diary.objects.order_by('-date')
	context={'entries':entries}
	return render(request,'index.html',context)

