from django.http import HttpResponse
from django.shortcuts import render
from . models import People

# Create your views here.
def demo(request):
    obj = People.objects.all()

    # name: str = "india"
    return render(request, "index.html", {'result':obj})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request, "result.html", {'add_result':add, 'sub_result':sub, 'mul_result':mul, 'div_result':div })
