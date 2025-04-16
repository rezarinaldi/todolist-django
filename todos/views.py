from django.shortcuts import render
from .models import Todo

# Create your views here.
def index_view(request):
  todos = Todo.objects.all()
  print(todos)

  return render(request, 'index.html', {'todos': todos})

def detail_view(request, id):
  todo = Todo.objects.get(id=id)

  return render(request, 'detail.html', {'todo': todo})
