from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SuppliersModel
from .forms import SuppliersForm
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

def Suppliers_Sing_Up_View(request):
    if request.method == "POST":
        # here you would normally process the form and save to DB
        fullname = request.POST.get("fullname")
        company = request.POST.get("company")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password != confirm_password:
            return HttpResponse("Passwords do not match!")
        # TODO: Save supplier to DB via a Model (e.g., Supplier model)

        return HttpResponse(f"Thanks {fullname}, your registration has been received!")

    return render(request, "Suppliers/singup.html")