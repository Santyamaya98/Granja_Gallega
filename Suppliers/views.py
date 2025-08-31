from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def Suppliers_View(request):
    return render(request, "Suppliers/suppliers.html")

def Suppliers_Sing_Up_View(request):
    if request.method == "POST":
        # here you would normally process the form and save to DB
        fullname = request.POST.get("fullname")
        company = request.POST.get("company")
        email = request.POST.get("email")

        # TODO: Save supplier to DB via a Model (e.g., Supplier model)

        return HttpResponse(f"Thanks {fullname}, your registration has been received!")

    return render(request, "Suppliers/singup.html")