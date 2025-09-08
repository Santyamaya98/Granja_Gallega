from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.
from .forms import SuppliersProductsForm
from .models import SuppliersProductsModel
from Suppliers.models import SuppliersModel

def products_add_view(request, pk):
    supplier = get_object_or_404(SuppliersModel, pk=pk)
    if request.method == 'POST':
        form = SuppliersProductsForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.supplier = supplier  # Make sure product is linked to supplier!
            product.save()
            messages.success(request, 'Producto añadido exitosamente!')
            return redirect('supplier_detail', pk=pk)
        else:
            messages.error(request, 'Error al añadir el producto. Revisa los datos.')
            print(form.errors) # This is key! It shows general form errors
            print(form.non_field_errors()) # And non-field errors
            messages.error(request, 'Error al añadir el producto. Revisa los datos.')
    else:  # GET request
        form = SuppliersProductsForm()

    context = {'form': form, 'supplier': supplier}
    return render(request, 'products/addproducts.html', context)