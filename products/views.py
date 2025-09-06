from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.
from .forms import SuppliersProductsForm
from .models import SuppliersProductsModel
from Suppliers.models import SuppliersModel

def products_add_view(request, pk):
    
    supplier = get_object_or_404(SuppliersModel, pk=pk, approved=True)

    if request.method == 'POST':
        form = SuppliersProductsForm(request.POST)
        if form.is_valid():
            # 3. Create the product object in memory, but DON'T save to DB yet.
            product = form.save(commit=False)

            # 4. Set the supplier relationship on the new product object.
            product.supplier = supplier

            # 5. Now, save the complete object to the database.
            product.save()

            messages.success(request, 'Producto añadido exitosamente!')
            # Redirect to the detail page for the supplier we're working with
            return redirect('Suppliers:supplier_detail', pk=supplier.pk)
    else:
        # If it's a GET request, create an empty form
        form = SuppliersProductsForm()

    # Pass both the form and the supplier to the template
    context = {
        'form': form,
        'supplier': supplier
    }
    return render(request, 'products/addproducts.html', context)