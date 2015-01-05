#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect    #与第7行一样
import datetime
#from django.template.response import SimpleTemplateResponse as STR
from shixisheng.models import student,Image
from django.template.response import TemplateResponse as TR
def home(request):
    d= {}
    all=student.objects.all()
    d['all']=all

    all_img=Image.objects.all()             
    d['all_img']=all_img
    return TR(request,"index.html",d)

def hello(request,a):
    #return HttpResponse("Hello world zhai" + '\t' + a)
    d= {"a":a,"date":str(datetime.datetime.now())}
    all=student.objects.all()
   # all=student.objects.filter(name="....")            #过滤
    d['all']=all
    #return STR("hello.html",d)
    return TR(request,"hello.html",d)

def new(request):
    s=student()                    #产生新的记录。
    s.name = request.POST['name']    
    s.address = request.POST['address']
    s.content = request.POST['content']
    s.count = 0
    s.save()
    return redirect("/hell/fdsa")


def delete(request,id):
    s=student.objects.get(id=int(id))   
    #s=student.objects.get(name="tom")    
    s.delete()
    return redirect("/hell/fdsa")


def edit_view(request,id):
    s=student.objects.get(id=int(id))   #通过id 得到一条记录
    d={"s":s}
    return TR(request,"edit.html",d)


def edit(request,id):
    s=student.objects.get(id=int(id))
    s.name=request.POST['name']
    s.address=request.POST['address']
    s.save()
    return redirect("/hell/fdsa")
