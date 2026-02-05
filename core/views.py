from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm


from django.shortcuts import render
from .models import Produk

def dashboard(request):
    status_filter = request.GET.get('status', 'bisa dijual')  # default

    produk = Produk.objects.select_related('kategori', 'status')

    if status_filter == 'bisa dijual':
        produk = produk.filter(status__nama_status__iexact='bisa dijual')
    elif status_filter == 'tidak bisa dijual':
        produk = produk.filter(status__nama_status__iexact='tidak bisa dijual')
    elif status_filter == 'all':
        pass  # tampilkan semua

    context = {
        'produk': produk,
        'status_filter': status_filter,
    }

    return render(request, 'dashboard/dashboard.html', context)

def tambah_produk(request):
    form = ProdukForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():  # ✅ WAJIB
            form.save()
            return redirect('dashboard:dashboard')

    return render(request, 'dashboard/form_produk.html', {
        'form': form,
        'title': 'Tambah Produk'
    })


def edit_produk(request, id):
    produk = get_object_or_404(Produk, id_produk=id)
    form = ProdukForm(request.POST or None, instance=produk)

    if request.method == 'POST':
        if form.is_valid():  # ✅ WAJIB
            form.save()
            return redirect('dashboard:dashboard')

    return render(request, 'dashboard/form_produk.html', {
        'form': form,
        'title': 'Edit Produk'
    })


def hapus_produk(request, id):
    produk = get_object_or_404(Produk, id_produk=id)
    produk.delete()
    return redirect('dashboard:dashboard')

