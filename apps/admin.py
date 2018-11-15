from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse, path
from django.utils.html import format_html
from django.contrib.admin import widgets 
from .models import *
import xlsxwriter

# Register your models here.
def get_column():
	column = []
	return column

class AkunAdmin(admin.ModelAdmin):
	list_display = ('kdakun', 'nmakun', 'kdjenbel', 'tahun')
	search_fields = ['kdakun', 'nmakun', 'kdjenbel', 'tahun']
	list_filter = ('nmakun', 'tahun')

	def get_xlsx(self, request):
		output = io.Bytes
		workbook = xlsxwriter.Workbook(output)
		worksheet = workbook.add_worksheet()
		data = get_column()

		for row_num, columns in enumerate(data):
			for col_num, cell_data in enumerate(columns):
				worksheet.write(row_num, col_num, cell_data)

		workbook.close()
		output.seek(0)
		filename = 'akun.xlsx'
		response = HttpResponse(
				output,
				content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
			)
		response ['Content-Disposition'] = 'attachment; filename=%s' % filename
		return response

	def get_urls(self):
		urls = super(AkunAdmin, self).get_urls()
		urls += [
			path("export-xlsx", self.get_xlsx, name='export-xlsx'),
		]
		return urls

	def download_links(self, obj):
		return format_html(
				'<a href="{}">Export Xlsx</a>', reverse('admin:export-xlsx', args=[obj.pk])
			)

	
admin.site.register(Akun, AkunAdmin)

class ProgramAdmin(admin.ModelAdmin):
	list_display = ('kdfungsi', 'kdsfungsi', 'kdprogram', 'nmprogram')
	search_fields = ['kdfungsi', 'kdprogram', 'nmprogram']
	list_filter = ('kdprogram', 'nmprogram')
	fieldsets = (
			('Section 1', {
				'fields': ('kdfungsi', 'kdsfungsi')
				}),
			('Section 2', {
				'fields': ('kdprogram', 'nmprogram')
				}),
		)
admin.site.register(Program, ProgramAdmin)

class DeptAdmin(admin.ModelAdmin):
	list_display = ('kddept', 'nmdept')
	search_fields = ['kddept', 'nmdept']
	list_filter = ('kddept', 'nmdept')
admin.site.register(Dept, DeptAdmin)

class FungsiAdmin(admin.ModelAdmin):
	list_display = ('kdfungsi', 'nmfungsi')
	search_fields = ['kdfungsi', 'nmfungsi']
	list_filter = ('kdfungsi', 'nmfungsi')
admin.site.register(Fungsi, FungsiAdmin)

class GiatAdmin(admin.ModelAdmin):
	list_display = ('kdfungsi', 'kdgiat', 'nmgiat', 'versi', 'tahun')
	search_fields = ['kdfungsi', 'kdgiat', 'nmgiat', 'tahun']
	list_filter = ('kdfungsi', 'kdgiat', 'nmgiat', 'tahun')
admin.site.register(Giat, GiatAdmin)

class UnitAdmin(admin.ModelAdmin):
	list_display = ('kddept', 'kdunit', 'nmunit')
	search_fields = ['kddept', 'kdunit', 'nmunit']
	list_filter = ('kddept', 'kdunit', 'nmunit')
admin.site.register(Unit, UnitAdmin)

class KotamAdmin(admin.ModelAdmin):
	list_display = ('kddept', 'kdunit', 'kdkotama', 'nmkotama', 'kdkukotama')
	search_fields = ['nmkotama']
	list_filter = ('kddept', 'kdunit', 'kdkotama', 'nmkotama', 'kdkukotama')
admin.site.register(Kotam, KotamAdmin)

class SatkunAdmin(admin.ModelAdmin):
	list_display = ('kdgiat', 'kdoutput', 'kdakun', 'kdsakun', 'nmsakun', 'kddipa')
	search_fields = ['kdsakun', 'nmsakun']
	list_filter = ('kdsakun', 'nmsakun')
admin.site.register(Satkun, SatkunAdmin)

class SatkrAdmin(admin.ModelAdmin):
	list_display = ('kddept', 'kdunit', 'kdkotama', 'kdsatkr', 'nmsatkr', 'kdkusatker')
	search_fields = ['kdsatkr', 'nmsatkr', 'kdkusatker']
	list_filter = ('kdsatkr', 'nmsatkr', 'kdkusatker')
admin.site.register(Satkr, SatkrAdmin)


admin.site.register(Subsatkr)
admin.site.register(Wasgiat)
admin.site.register(Bulan)