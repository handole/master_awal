import uuid
import datetime
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
	YEAR_CHOICES.append((r,r))
# def year_choices():
# 	return [(r,r) for r in range(1940, datetime.date.today().year+1)]

def current_year():
	return datetime.date.today().year


class Akun(models.Model):
	kdakun = models.CharField(max_length=6, verbose_name='Kode akun')
	nmakun = models.CharField(max_length=100, verbose_name='Nama akun')
	kdjenbel = models.CharField(max_length=2, verbose_name='Kode Jenis Beli')
	tahun = models.IntegerField(_('Tahun'), choices=YEAR_CHOICES, default=current_year)

	def __str__(self):
		return self.nmakun

class Bulan(models.Model):
	kdbulan = models.CharField(max_length=2, verbose_name='Kode bulan')
	nmbulan = models.CharField(max_length=15, verbose_name='Nama Bulan')

	def __str__(self):
		return self.nmbulan

class Dept(models.Model):
	kddept = models.CharField(max_length=3, verbose_name='Kode Dept')
	nmdept = models.CharField(max_length=70, verbose_name='Nama Dept')

	def __str__(self):
		return self.nmdept

class Fungsi(models.Model):
	kdfungsi = models.CharField(max_length=2, verbose_name='Kode Fungsi')
	nmfungsi = models.CharField(max_length=30, verbose_name='Nama Fungsi')


	def __str__(self):
		return self.nmfungsi


class Program(models.Model):
	kdfungsi = models.ForeignKey(Fungsi, on_delete=models.CASCADE, verbose_name='Kode Fungsi')
	kdsfungsi = models.CharField(max_length=2, verbose_name='Kode SFungsi')
	kdprogram = models.CharField(max_length=2, verbose_name='Kode Program')
	nmprogram = models.CharField(max_length=45, verbose_name='Nama Program')
	tahun = models.IntegerField(choices=YEAR_CHOICES, default=current_year, verbose_name='Tahun Program')
	versi = models.CharField(max_length=20, verbose_name='Versi')

	def __str__(self):
		return self.nmprogram

class Giat(models.Model):
	kdfungsi = models.ForeignKey(Fungsi, on_delete=models.CASCADE, verbose_name='Kode Fungsi')
	kdsfungsi = models.CharField(max_length=2, verbose_name='Kode SFungsi')
	kdprogram = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='Kode Program')
	kdgiat = models.CharField(max_length=4, verbose_name='Kode Giat')
	nmgiat = models.CharField(max_length=70, verbose_name='Nama Giat')
	versi = models.CharField(max_length=25, verbose_name='Versi')
	tahun = models.IntegerField(choices=YEAR_CHOICES, default=current_year, verbose_name='Tahun Giat')

	def __str__(self):
		return self.nmgiat


class Unit(models.Model):
	kddept = models.ForeignKey(Dept, on_delete=models.CASCADE, verbose_name='Kode Dept')
	kdunit = models.IntegerField(null=True, verbose_name='Kode Unit')
	nmunit = models.CharField(max_length=60, verbose_name='Nama Unit')

	def __str__(self):
		return self.nmunit

class Kotam(models.Model):
	kddept = models.ForeignKey(Dept, on_delete=models.CASCADE, related_name='kotam_dept', verbose_name='Kode Dept')
	kdunit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='kotam_unit', verbose_name='Kode Unit')
	kdkotama = models.CharField(max_length=255, verbose_name='Kode Kotama')
	nmkotama = models.CharField(max_length=255, verbose_name='Nama Kotama')
	kdkukotama = models.CharField(max_length=255, verbose_name='Kode Kukotama')

	def __str__(self):
		return self.nmkotama

class Output(models.Model):
	kdfungsi = models.ForeignKey(Fungsi, on_delete=models.CASCADE, verbose_name='Output')
	kdsfungsi = models.CharField(max_length=2, verbose_name='Kode SFungsi')
	kdprogram = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='Kode Program')
	kdgiat = models.ForeignKey(Giat, on_delete=models.CASCADE, verbose_name='Kode Giat')
	kdoutput = models.CharField(max_length=3, verbose_name='Kode Output')
	kdoutput1 = TreeForeignKey('self', on_delete=models.CASCADE, max_length=2, verbose_name='Kode Output 1')
	nmoutput = models.CharField(max_length=75, verbose_name='Nama Output')

	def __str__(self):
		return self.nmoutput

class Satkun(models.Model):
	kdgiat = models.ForeignKey(Giat, on_delete=models.CASCADE, related_name='satkun_giat', verbose_name='Kode Giat')
	kdoutput = models.ForeignKey(Output, on_delete=models.CASCADE, related_name='satkun_output', verbose_name='Kode Output')
	kdakun = models.ForeignKey(Akun, on_delete=models.CASCADE, related_name='satkun_akun', verbose_name='Kode Akun')
	kdsakun = models.IntegerField(null=True, verbose_name='Kode Satuan Kunjungan')
	nmsakun = models.CharField(max_length=255, verbose_name='Nama Satuan Kunjungan')
	kddipa = models.CharField(max_length=1, verbose_name='Kode Dipa')

	def __str__(self):
		return self.nmsakun

class Satkr(models.Model):
	kddept = models.ForeignKey(Dept, on_delete=models.CASCADE, verbose_name='Kode Dept')
	kdunit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='Kode Unit')
	kdkotama = models.ForeignKey(Kotam, on_delete=models.CASCADE, verbose_name='Kode Kotama')
	kdsatkr = models.CharField(max_length=2, verbose_name='Kode Satuan Kerja')
	nmsatkr = models.CharField(max_length=80, verbose_name='Nama Satuan Kerja')
	kdkusatker = models.ForeignKey(Satkun, on_delete=models.CASCADE, verbose_name='Kode Kusatuan Kerja')

	def __str__(self):
		return self.nmsatkr

class Subsatkr(models.Model):
	kddept = models.ForeignKey(Dept, on_delete=models.CASCADE, verbose_name='Kode Dept')
	kdunit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='Kode Unit')
	kdkotama = models.ForeignKey(Kotam, on_delete=models.CASCADE, verbose_name='Kode Kotama')
	kdsatkr = models.ForeignKey(Satkr, on_delete=models.CASCADE, verbose_name='Kode Satuan Kerja')
	kdsubsatkr = models.CharField(max_length=2, verbose_name='Kode Sub SatKer')
	nmsubsatkr = models.CharField(max_length=100, verbose_name='Nama SubSatkr')

	def __str__(self):
		return self.nmsubsatkr

class Wasgiat(models.Model):
	kdwasgiat = models.CharField(max_length=2, verbose_name='Kode Wasgiat')
	nmwasgiat = models.CharField(max_length=30, verbose_name='Nama Wasgiat')

	def __str__(self):
		return self.nmwasgiat

class Tingkat(models.Model):
	kdtingkat = models.IntegerField(null=True)
	pengguna = models.CharField(max_length=30)
	kdwasgiat = models.ForeignKey(Wasgiat, on_delete=models.CASCADE)


class Kegiatan(MPTTModel):
	kdkegiatan = models.CharField(max_length=4, verbose_name='Kode Kegiatan')
	nmkegiatan = models.CharField(max_length=255, verbose_name='Nama Kegiatan')
	keterangan = models.TextField()
	budget = models.DecimalField(max_digits=2, decimal_places=2, verbose_name='Budget')
	status = models.CharField(max_length=100, verbose_name='Status')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Created By')
	parent_id = TreeForeignKey('self', on_delete=models.CASCADE, related_name='child', verbose_name='Child Id')

	class MPTTMeta:
		order_insertion_by = ['nmkegiatan']

	def get_children(self):
		parent =  self.parent.cleeaned_data.get('parent_id')
		for obj in Kegiatan.objects.all():
			obj.kdkegiatan, obj.nmkegiatan, obj.parent_id = (0, 0, obj.parent)
			obj.save()
		Kegiatan.tree.rebuild()
		return parent


# tambah tabel kegiatan
# id, kode, nama, keterangan, budget, status, created_by, parent_id,
# parent childs
#  https://github.com/django-mptt/django-mptt