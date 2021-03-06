from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from . import models, fiters
from django.template.loader import get_template
from furniture.utils import render_to_pdf
from users.models import User
from datetime import datetime
from django.http import HttpResponse
from django.views.generic import View


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES['image']
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        product = models.Products(name=name, image=image, status=int(status), price=price, quantity=quantity)
        product.save()
        if product.pk:
            return redirect('home_page')
        else:
            return redirect('home_page')
    return render(request, 'store/add_product.html')


def search_products(request):
    products = models.Products.objects.all()
    prod_filter = fiters.ProductsFilter(request.GET, queryset=products)
    prods = prod_filter.qs
    context = {"products": prods, "myfilter": prod_filter}
    return render(request, 'store/products.html', context=context)


class ProductAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('products-all-pdf.html')
        products = models.Products.objects.all()
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "Furniture Home ",
            "user": user_obj,
            "products": products,
            "topic": "Report for All Products ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('products-all-pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class CustomerAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('customer-all-pdf.html')
        customers = User.objects.filter(user_type=2)
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "Furniture Home ",
            "user": user_obj,
            "customers": customers,
            "topic": "Report for All Customers ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('customer-all-pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
