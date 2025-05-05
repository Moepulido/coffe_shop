from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirige a la lista de productos.
                return redirect('products:product_list')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
        
    return render(request, 'users/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Ya has iniciado sesión.')
            return redirect('products:product_list')
        else:
            messages.error(request, 'Por favor corrige los errores indicados abajo.')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
