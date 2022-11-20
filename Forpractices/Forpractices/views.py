import sys
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect


sys.path.insert(1,'D:/All_laptop_data/DATA_STURCTURE/Basic_programming_of_ C,C++,python/Django Frame Work/This is now for practice/Forpractices')
from service import views

from service.models import Service

# print(sys.path)
def userform(request):
    ServiceData=Service.objects.all()
    data={
        "servicedata":ServiceData
    }
    # print(ServiceData)
    # for x in ServiceData:
    #     print(x)
    # fn=usersform()
    # # data={'form':fn}
    # d={}
    # try:
    #     if request.method=="POST":
    #         if request.POST.get('usern1')=="":
    #             return render(request,"userform.html",{'error':True})
    #         passw=int(request.POST.get('pass1'))
    #         user_name=(request.POST.get('usern1'))
           
    #         d={
    #             'passwor':passw,
    #             'user':user_name,
    #             # 'we':rt,
    #             }
    #         # url="/new/?output={}".format(d['user'])
    #         # if d['passwor']==12345:
    #         #     return HttpResponseRedirect('new')
    #         # else:
    #         #     return HttpResponseRedirect('Worng_pass')
    #         # return HttpResponseRedirect(url)
    # except:
    #     pass
  
    return render(request,"userform.html",data)
    # return render(request,"userform.html",data)
    
def saveform(request):
    if request.method=="POST":
        passward=request.POST.get('pass1')
        user_name=request.POST.get('usern1')
        data=Service(passward=passward,user_name=user_name)
        data.save()   
    return render(request,"userform.html")


# def new(request):
#     if request.method=="GET":
#         # return HttpResponse(request)
#         output=request.GET.get('output')
#     return HttpResponse(output)
    
    
    
# def w_pass(request):
#     return HttpResponse('Sorry Worng password')
# # def Google(request):
#     return 


# def submitform(request):
#     d={}
#     try:
#         if request.method=="POST":
#             user_name=(request.POST.get('usern1'))#userform se aaya hua data yhan parr liya gya hai.
#             passw=int(request.POST.get('pass1'))
           
#             d={
#                 'passwor':passw,
#                 'user':user_name,
#                 # 'we':rt,
#                 }
#             url="/new/?output={}".format(d['user'])
#             # if d['passwor']==12345:
#             #     return HttpResponseRedirect('new')
#             # else:
#             #     return HttpResponseRedirect('Worng_pass')
#         return HttpResponse(d['user'])
#         # return HttpResponse(d['passwor'],d['user'])  Ye khojen ki 2 ekk sath kese display karaye.
#     except:
#         pass
  
    # return HttpResponse(request)
    

    