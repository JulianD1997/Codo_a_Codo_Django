from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserForm
from .models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'¡Usuario creado con éxito!')
            return redirect('login')
        context={'form':form,
                 'errors':form.errors} 
        return render(request,'users/register.html',context)
        
    form = UserForm()
    context={'form':form}
    return render(request,'users/register.html',context)