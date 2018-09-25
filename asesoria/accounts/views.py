from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request,'Tony\home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(reques.POST)
        if form.is_valid():
            form.save()
            return redirect('')

    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'reg_form.html', args)
