from django.shortcuts import render
from django.urls import reverse
from Home.models import SanPham
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.


def ShowProduct(request):
    try:
        products = SanPham.objects.all();
    except SanPham.DoesNotExist:
        raise Http404('Khong tim thay san pham nao!!!')
    return render(request, 'index.html', context={'products':products})

def ProductDetail(request, id):
    try:
        products = SanPham.objects.get(pk=id);
    except SanPham.DoesNotExist:
        raise Http404('Khong tim thay san pham nao!!!')
    return render(request, 'productdetail.html', context={'products':products})
def add(request):
    return render(request,'add.html')

def addrecord(request):
    try:
        ten=request.POST['tensanpham']
        ma=request.POST['masanpham']
        sanpham=SanPham(Ten_San_Pham=ten, Ma_San_Pham=ma)
        sanpham.save()
    except:
        raise Http404('Loi thuc thi!!!')
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    try:
        products= SanPham.objects.get(pk=id);
        products.delete()
    except:
        raise Http404('Khong tim thay san pham')
    return HttpResponseRedirect(reverse('index'))
def update(request, id):
    try:
        products = SanPham.objects.get(pk=id);
    except SanPham.DoesNotExist:
        raise Http404('Khong tim thay san pham nao!!!')
    return render(request, 'update.html', context={'products':products})

def updaterecord(request, id):
    try:
        products= SanPham.objects.get(pk=id)
        ten=request.POST['tensanpham']
        ma=request.POST['masanpham']
        products.Ten_San_Pham=ten
        products.Ma_San_Pham=ma
        products.save()
    except:
        raise Http404('Khong tim thay san pham!!!')
    return HttpResponseRedirect(reverse('index'))