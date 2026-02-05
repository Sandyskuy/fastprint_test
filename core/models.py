from django.db import models

class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=100)

    class Meta:
        db_table = "kategori"  # pakai tabel existing

    def __str__(self):
        return self.nama_kategori


class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=50)

    class Meta:
        db_table = "status"  # pakai tabel existing

    def __str__(self):
        return self.nama_status


class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=150)
    harga = models.IntegerField()

    kategori = models.ForeignKey(
        Kategori,
        on_delete=models.CASCADE,
        related_name="produk"
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name="produk"
    )

    class Meta:
        db_table = "produk"  # pakai tabel existing

    def __str__(self):
        return self.nama_produk
