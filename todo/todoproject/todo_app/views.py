from django.shortcuts import render,redirect
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
class tododeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('classlistview/')

class todoupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('classdetailview',kwargs={'pk':self.object.id})

class tododetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class  todolistview(ListView):
    model=Task
    template_name='index.html'
    context_object_name='task1'
def index(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'index.html', {'task1': task1})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, taskid):
    task = Task.objects.get(id=taskid)
    forms = TodoForm(request.POST or None, instance=task)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request, 'edit.html', {'forms': forms, 'task': task})
