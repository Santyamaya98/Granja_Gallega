from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.
from .forms import SuppliersProductsForm
from Suppliers.models import SuppliersModel

def products_add_view(request):
    if request.method == 'POST':
        form = SuppliersProductsForm(request.POST)
        if form.is_valid():
            token_id = form.cleaned_data['token_id']
            # 1. Validate supplier by token (uuid)
            supplier = get_object_or_404(SuppliersModel, pk=token_id, approved=True)
            
            product = form.save(commit=False)
            product.supplier = supplier
            product.save()
            
            messages.success(request, 'Producto añadido exitosamente!')
            return redirect('addproducts')  # Make sure your urls.py uses addproducts as the name for this view
    else:
        form = SuppliersProductsForm()
    return render(request, 'products/addproducts.html', {'form': form})