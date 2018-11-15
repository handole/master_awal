import uuid
from django.db import models

# Create your models here.
class Akun(models.Model):
	kdakun = models.IntegerField(null=True)
	nmakun = models.CharField(max_length=100)
	kdjenbel = models.IntegerField(null=True)
	tahun = models.DateField(null=True)

	def __str__(self):
		return self.nmakun

class Bulan(models.Model):
	kdbulan = models.IntegerField(null=True)
	nmbulan = models.CharField(max_length=15)

	def __str__(self):
		return self.nmbulan

class Dept(models.Model):
	kddept = models.IntegerField(null=True)
	nmdept = models.CharField(max_length=70)

	def __str__(self):
		return self.nmdept

class Fungsi(models.Model):
	kdfungsi = models.IntegerField(null=True)
	nmfungsi = models.CharField(max_length=30)

	def __str__(self):
		return self.nmfungsi


class Program(models.Model):
	kdfungsi = models.ForeignKey(Fungsi, on_delete=models.CASCADE)
	kdsfungsi = models.IntegerField(null=True)
	kdprogram = models.IntegerField(null=True)
	nmprogram = models.CharField(max_length=45)
	tahun = models.DateField(null=True)
	versi = models.CharField(max_length=20)

	def __str__(self):
		return self.nmprogram

class Giat(models.Model):
	kdfungsi = models.ForeignKey(Fungsi, on_delete=models.CASCADE)
	kdsfungsi = models.IntegerField(null=True)
	kdprogram = models.ForeignKey(Program, on_delete=models.CASCADE)
	kdgiat = models.IntegerField(null=True)
	nmgiat = models.CharField(max_length=70)
	versi = models.CharField(max_length=25)
	tahun = models.DateField(null=True)

	def __str__(self):
		return self.nmgiat


class Unit(models.Model):
	kddept = models.ForeignKey(Dept, on_delete=models.CASCADE)
	kdunit = models.IntegerField(null=True)
	nmunit = models.CharField(max_length=60)

	def __str__(self):
		return self.nmunit

class Kotam(models.Model):
	kddept = models.ForeignKey(Dept, on_delete=models.CASCADE)
	kdunit = models.ForeignKey(Unit, on_delete=models.CASCADE)
	kdkotama = models.IntegerField(null=True)
	nmkotama = models.CharField(max_length=255)
	kdkukotama = models.CharField(max_length=255)

	def __str__(self):
		return self.nmkotama

class Satkun(models.Model):
	kdgiat = models.ForeignKey(Giat, on_delete=models.CASCADE)
	kdoutput = models.CharField(max_length=3)
	kdakun = models.ForeignKey(Akun, on_delete=models.CASCADE)
	kdsakun = models.IntegerField(null=True)
	nmsakun = models.CharField(max_length=255)
	kddipa = models.IntegerField(null=True)

	def __str__(self):
		return self.nmsakun

class Satkr(models.Model):
	kddept = models.ForeignKey(Dept, on_delete=models.CASCADE)
	kdunit = models.ForeignKey(Unit, on_delete=models.CASCADE)
	kdkotama = models.ForeignKey(Kotam, on_delete=models.CASCADE)
	kdsatkr = models.IntegerField(null=True)
	nmsatkr = models.CharField(max_length=80)
	kdkusatker = models.ForeignKey(Satkun, on_delete=models.CASCADE)

	def __str__(self):
		return self.nmsatkr

class Subsatkr(models.Model):
	kddept = models.ForeignKey(Dept, on_delete=models.CASCADE)
	kdunit = models.ForeignKey(Unit, on_delete=models.CASCADE)
	kdkotama = models.ForeignKey(Kotam, on_delete=models.CASCADE)
	kdsatkr = models.ForeignKey(Satkr, on_delete=models.CASCADE)
	kdsubsatkr = models.IntegerField(null=True)
	nmsubsatkr = models.CharField(max_length=100)

	def __str__(self):
		return self.nmsubsatkr

class Wasgiat(models.Model):
	kdwasgiat = models.IntegerField(null=True)
	nmwasgiat = models.CharField(max_length=30)

	def __str__(self):
		return self.nmwasgiat

class Tingkat(models.Model):
	kdtingkat = models.IntegerField(null=True)
	pengguna = models.CharField(max_length=30)
	kdwasgiat = models.ForeignKey(Wasgiat, on_delete=models.CASCADE)