from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.
from .forms import ProductPromotionForm, ProductPromotionForm, SuppliersProductsForm
from .models import SuppliersProductsModel, PromosModel
from Suppliers.models import SuppliersModel

def products_add_view(request, supplier_pk):
    supplier = get_object_or_404(SuppliersModel, pk=supplier_pk)
    if request.method == 'POST':
        form = SuppliersProductsForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.supplier = supplier  # Make sure product is linked to supplier!
            product.save()
            messages.success(request, 'Producto añadido exitosamente!')
            return redirect('supplier_detail',supplier_pk=supplier_pk)
        else:
            messages.error(request, 'Error al añadir el producto. Revisa los datos.')
            print(form.errors) # This is key! It shows general form errors
            print(form.non_field_errors()) # And non-field errors
            messages.error(request, 'Error al añadir el producto. Revisa los datos.')
    else:  # GET request
        form = SuppliersProductsForm()

    context = {'form': form, 'supplier': supplier}
    return render(request, 'products/addproducts.html', context)

def products_list_view(request, supplier_pk):
    supplier = get_object_or_404(SuppliersModel, pk=supplier_pk)
    products = SuppliersProductsModel.objects.filter(supplier=supplier)
    return render(request, 'products/products_list.html', {'products': products, 'supplier': supplier})

def product_edit(request, supplier_pk, product_pk):
    supplier = get_object_or_404(SuppliersModel, pk=supplier_pk)
    product = get_object_or_404(SuppliersProductsModel, pk=product_pk)
    if request.method == 'POST':
        form = SuppliersProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente!')
            return redirect('products_list', supplier_pk=supplier_pk)
    else:
        form = SuppliersProductsForm(instance=product)
    return render(request, 'products/editproduct.html', {'form': form, 
                                                         'title': 'Editar Producto',
                                                         'supplier':supplier,
                                                         'product': product
                                                         })


def products_promo_view(request, supplier_pk, product_pk):
    supplier = get_object_or_404(SuppliersModel, pk=supplier_pk)
    product = get_object_or_404(SuppliersProductsModel, pk=product_pk)
    if request.method == 'POST':
        if product.promotion == False:
            messages.error(request, 'Producto no está en promoción')
            return redirect('editproduct', supplier_pk=supplier_pk, product_pk=product_pk)
        
        form = ProductPromotionForm(request.POST)
        
        if form.is_valid():
            new_promo = form.save(commit=False)
            new_promo.product = product # This is the crucial line
            new_promo.save()
            messages.success(request, 'Promo realizada exitosamente')
            return redirect('products_list', supplier_pk=supplier_pk)
    else:
        form = ProductPromotionForm(instance=product)
    return render(request, 'products/promoproduct.html',
                   {
                       'form': form, 
                       'title': 'Has tu promoción',
                       'supplier' : supplier,
                       'product': product

                    })

        
def promo_list_view(request, supplier_pk):
    supplier = get_object_or_404(SuppliersModel, pk=supplier_pk)
    
    # Products of this supplier that are marked as promo
    products = SuppliersProductsModel.objects.filter(supplier=supplier, promotion=True)
    
    # Get promos linked to those products
    promos = PromosModel.objects.filter(product__in=products)
    
    return render(
        request,
        'products/products_promo.html',
        {
            'promotion': promos,
            'supplier': supplier,
            'products': products,  # plural, since it can be many
        }
    )
