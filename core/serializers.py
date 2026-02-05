from rest_framework import serializers
from .models import Produk

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ['id_produk', 'nama_produk', 'harga', 'kategori', 'status']

    def validate_nama_produk(self, value):
        if not value:
            raise serializers.ValidationError("Nama produk wajib diisi")
        return value

    def validate_harga(self, value):
        if value <= 0:
            raise serializers.ValidationError("Harga harus berupa angka lebih dari 0")
        return value
