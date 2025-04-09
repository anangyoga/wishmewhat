from django.shortcuts import render, redirect
from django.views import View
from .models import Wishes
from .tasks import task_do_something

# Create your views here.
class IndexView(View):
    def get(self, request):
        wishes = Wishes.objects.all()

        context = {
            'wishes': wishes
        }

        return render(request, 'index.html', context)

    def post(self, request):
        text = request.POST.get('wish')

        task_do_something()
        Wishes.objects.create(text=text)
        return redirect('index')