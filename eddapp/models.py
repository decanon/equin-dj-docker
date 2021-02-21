from django.db import models


# Create your models here.
class PelamarKerja(models.Model):
    idpelamarkerja = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    alamat = models.CharField(max_length=255, blank=True, null=True)
    skill = models.CharField(max_length=255, blank=True, null=True)
    pendidikan_terakhir = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'pelamarkerja'
        verbose_name = 'Pelamar Kerja'
        verbose_name_plural = 'Pelamar Kerja'


class PemberiKerja(models.Model):
    idpemberikerja = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    perusahaan = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.nama}({self.perusahaan})'

    class Meta:
        db_table = 'pemberikerja'
        verbose_name = 'Pemberi Kerja'
        verbose_name_plural = 'Pemberi Kerja'


class Pekerjaan(models.Model):
    idpemberikerjapekerjaan = models.AutoField(primary_key=True)
    namapekerjaan = models.CharField(max_length=255, blank=True, null=True)
    id_pemberikerja = models.ForeignKey(PemberiKerja, models.CASCADE, db_column='id_pemberikerja', blank=True, null=True)
    gaji = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.namapekerjaan} dari {self.id_pemberikerja}'

    class Meta:
        db_table = 'pemberikerja_pekerjaan'
        verbose_name = 'Pekerjaan'
        verbose_name_plural = 'Pekerjaan'


class PekerjaanPelamarKerja(models.Model):
    idpemberikerjapekerjaanpelamarkerja = models.AutoField(primary_key=True)
    id_pemberikerja_pekerjaan = models.ForeignKey(Pekerjaan, models.CASCADE, db_column='id_pemberikerja_pekerjaan', blank=True, null=True)
    id_pelamarkerja = models.ForeignKey(PelamarKerja, models.CASCADE, db_column='id_pelamarkerja', blank=True, null=True)
    tanggal_melamar = models.DateTimeField(blank=True, null=True)
    cover_letter = models.TextField(blank=True, null=True)
    gaji_yang_diminta = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.id_pemberikerja_pekerjaan}: {self.id_pelamarkerja}'

    class Meta:
        db_table = 'pemberikerja_pekerjaan_pelamarkerja'
        verbose_name = 'Daftar Pelamar'
        verbose_name_plural = 'Daftar Pelamar'

        constraints = [
            models.UniqueConstraint(fields=['id_pemberikerja_pekerjaan', 'id_pelamarkerja'],
                                    name='Pelamar tidak mungkin melamar yang sama 2x')
        ]
