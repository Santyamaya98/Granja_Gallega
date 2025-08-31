from django.shortcuts import render

# Create your views here.
def Suppliers_View(request):
    return render(request, "Suppliers/suppliers_list.html")