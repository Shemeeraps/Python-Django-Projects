from django.shortcuts import render,redirect
from .models import task
from .forms import todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

# Create your views here.


class task_listview(ListView):
    model=task
    template_name='task_view.html'
    context_object_name='obj1'

class task_detailview(DetailView):
    model=task
    template_name='detail.html'
    context_object_name='i'
class task_updateview(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name = 't'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('abcdetailtask',kwargs={'pk':self.object.id})
class task_deleteview(DeleteView):
    model = 'task'
    template_name = 'delete.html'
    success_url = reverse_lazy('abctask')

def task_view(request):
    obj1 = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = task(name=name, priority=priority,date=date)
        obj.save()

    return render(request,'task_view.html',{'obj1':obj1})

def delete(request,taskid):
    obj=task.objects.get(id=taskid)
    return render(request,'delete.html',{'obj':task})
def update(request,taskid):
    obj=task.objects.get(id=taskid)
    return render(request,'edit.html',{'obj':task})








