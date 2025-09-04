from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SuppliersModel
from .forms import SuppliersForm, SuppliersSignupForm, SupplierLoginForm
# from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login 
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def Suppliers_View(request):
    """Display all suppliers"""
    suppliers = SuppliersModel.objects.all()
    return render(request, "Suppliers/suppliers.html", {'suppliers': suppliers})

def Suppliers_List(request):
    """Display all suppliers"""
    suppliers = SuppliersModel.objects.all()
    return render(request, "Suppliers/supplier_list.html", {'suppliers': suppliers})

def supplier_detail(request, pk):
    """View supplier details"""
    supplier = get_object_or_404(SuppliersModel, pk=pk)
    return render(request, 'suppliers/supplier_detail.html', {'supplier': supplier})

def supplier_create(request):
    """Create new supplier"""
    if request.method == 'POST':
        form = SuppliersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor creado exitosamente!')
            return redirect('supplier_list')
    else:
        form = SuppliersForm()
    return render(request, 'suppliers/supplier_create.html', {'form': form, 'title': 'Crear Proveedor'})

def supplier_edit(request, pk):
    """Edit supplier"""
    supplier = get_object_or_404(SuppliersModel, pk=pk)
    if request.method == 'POST':
        form = SuppliersForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado exitosamente!')
            return redirect('supplier_detail', pk=supplier.pk)
    else:
        form = SuppliersForm(instance=supplier)
    return render(request, 'suppliers/supplier_edit.html', {'form': form, 'title': 'Editar Proveedor'})

def supplier_delete(request, pk):
    """Delete supplier"""
    supplier = get_object_or_404(SuppliersModel, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        messages.success(request, 'Proveedor eliminado exitosamente!')
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_confirm_delete.html', {'supplier': supplier})

def Suppliers_Sign_Up_View(request):
    if request.method == 'POST':
        form = SuppliersSignupForm(request.POST)
        if form.is_valid():
            token_id = form.cleaned_data['token_id']

            # 1. Validate supplier by token (uuid)
            supplier = get_object_or_404(SuppliersModel, pk=token_id, approved=True)

            if supplier.user:
                messages.error(request, "Este proveedor ya tiene una cuenta de usuario.")
                return redirect('login')

            # 2. Create user
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )

            # 3. Link supplier to new user
            supplier.user = user
            supplier.save()

            messages.success(request, "Cuenta creada exitosamente! Ahora puedes iniciar sesión.")
            return redirect('Login') # TODO log in
    else:
        form = SuppliersSignupForm()

    return render(request, 'suppliers/signup.html', {
        'form': form,
        'title': "Suppliers Users Signup"
    })

def Suppliers_Login_View(request):
    if request.method == 'POST':
        form = SupplierLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # 1. Log the user in first
                login(request, user)

                # 2. Handle the session expiry logic
                if not remember_me:
                    request.session.set_expiry(0)  # Session expires on browser close

                messages.success(request, "Has iniciado sesión exitosamente.")
                
                # 3. Then, handle the redirection
                try:
                    # Access the related supplier object from the user
                    supplier = SuppliersModel.objects.get(user=user)
                    return redirect('supplier_detail', pk=supplier.pk)
                except SuppliersModel.DoesNotExist:
                    # Handle the case where a User has no related SupplierModel
                    messages.error(request, "Error: Cuenta de proveedor no encontrada.")
                    # Redirect to a generic page or log out the user
                    return redirect('suppliers')
            
            # The 'else' should handle the authentication failure
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = SupplierLoginForm()

    return render(request, 'suppliers/login.html', {
        'form': form,
        'title': "Suppliers Users Login"
    })
def Suppliers_Logout_View(request):
    
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('Login')  # Redirect to a success page.

def Suppliers_Dashboard_View(request):
    return HttpResponse("Dashboard - To be implemented")