from django.shortcuts import render
from .models import Place,Actor
# Create your views here.
def index(request):
    obj1=Place.objects.all()
    obj2=Actor.objects.all()
    return render(request,'myindex.html',{'result1':obj1,'result2':obj2})