from django.shortcuts import render,redirect
from .forms import ProfileForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProfileForm()
    
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')