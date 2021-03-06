from django.shortcuts import render


def home_page(request):
    return render(request, 'main/home.html')


def contact_page(request):
    return render(request, 'main/contact.html')


def about_page(request):
    return render(request, 'main/about.html')


def reports(request):
    return render(request, 'main/reports.html')
