from django.shortcuts import render

# Cree your views here.
def home_page_view(request):
    return render(request, 'website/paginainicial.html')

def second_page_view(request):
    return render(request, 'website/sobre.html')

def third_page_view(request):
    return render(request, 'website/contacto.html')