import os
import django
import json
os.environ['DJANGO_SETTINGS_MODULE']='deeplens.settings'
django.setup()
from random import randrange
from dld.models import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from . import connect
from . import common_func
from pyecharts.charts import Bar,Page,Line


def login(request):
    return render(request,'login.html')

def check_login(func):
    def warpper(request, *args, **kwargs):
        user=request.session.get('user')
        is_login = request.session.get('IS_LOGIN')
        key = request.session.get('my_key')
        if is_login and user and key==1994:
            return func(request, *args, **kwargs)
        else:
            return redirect('/')
    return warpper

@check_login
def home(request):
    return render(request,'index.html')

def auth(request):
     username=request.POST.get('username')
     passwd=request.POST.get('password')
     if passwd==Users.objects.get(name=username).passwd:
         request.session['user']=username
         request.session['IS_LOGIN'] = True
         request.session['my_key'] = 1994
         request.session.set_expiry(0)
         common_func.index_dic['user']=username
         return render(request,'index.html',common_func.index_dic)
     else:
         return render(request,'login.html')

@check_login
def product(request,*args, **kwargs):
    values = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
    return render(request, 'table.html', {'data': values})

@check_login
def send_pic(request,*args, **kwargs):
    pass

@check_login
def fund_reports(request,*args, **kwargs):
    bar = Bar()
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
    bar.add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
    bar1 = Bar()
    bar1.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar1.add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
    bar1.add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])

    page = Page()
    page.add(bar)
    page.add(bar1)
    page.render('templates/test.html')
    return render(request,'test.html')

@check_login
def fund_info(request,*args,**kwargs):
    user_name=request.session.get('user')
    profile="关于基金基本资料的描述"
    compose="基金组合应该是什么类型的数据？文本？表格？"
    analysis="纯文本描述"
    cost="关于该基金费用的描述"
    bonus="something about bonus"
    files="归档一些资料"
    info={
    "user":user_name,
    "profile":profile,
    "compose":compose,
    "analysis":analysis,
    "cost":cost,
    "bonus":bonus,
    "files":files, 
    }
	
    return render(request,"details.html",info)

@check_login
def data_json(request,*args,**kwargs):
    values= []
    for i in range(8):
        tmp={}
        tmp["id"]=i
        tmp["name"]="test"
        tmp["price"]="100.00"
        values.append(tmp)
    data={}
    data["total"]=3
    data["rows"]=values
    return JsonResponse(data)

@check_login
def setChart(request,*args,**kwargs):
    data={"name":["iso","english","china","ufo","seo"],"data":[400,200,300,100,11]}
    return JsonResponse(data)

@check_login
def login_out(request):
    request.session.flush()
    return render(request,'login.html')
