from django.shortcuts import render

# Create your views here.

def first(request):
    d={'name':'MAMMU','age':21}
    return render(request,'jinja_print.html',context=d)