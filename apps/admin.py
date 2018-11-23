from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse, path
from django.utils.html import format_html
# from django.core.urlresolvers import reverse
from django.contrib.admin import widgets 
from .models import *
import xlsxwriter

# Register your models here.
def get_column():
	column = []
	return column

class DownloadXLS(widgets.AdminFileWidget):
	id = None
	template_name = 'widgets/download_excel.html'

	def __init__(self, id, attrs=None):
		self.id = id
		super().__init__(attrs)

	def get_context(self, name, value, attrs):
		context = super().get_context(name, value, attrs)
		print(self, name, value, attrs, self.id)
		context['download_excel'], reverse('export', kwargs={'pk': self.id})
		return context

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

	def export_program(self, request, program_id, *args, **kwargs):
		return self.proses_action(
			request=request,
			program_id=program_id,
			action_title = 'Export Program'
		)

	def proses_action(self, request, program_id, action_title):
		account = self.get_object(request, program_id)

		# if request.method != 'POST':

	# def get_urls(self):
	# 	urls = super().get_urls()
	# 	custom_urls = [
	# 		path('program-export', self.views.export_xls, name='program-excel'),
	# 	]		

	# 	return custom_urls + urls

	# def program_actions(self, obj):
	# 	return format_html(
	# 		'<a class="button" href="#">Export</a>',
	# 		reverse('export-xls'),
	# 	)
	# program_actions.short_description = "Program Action"
	# program_actions.allow_tags = True

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

class OutputAdmin(admin.ModelAdmin):
	list_display = ('kdfungsi', 'kdprogram', 'kdgiat', 'kdoutput', 'nmoutput')
	search_fields = ['nmoutput']
	list_filter = ('nmoutput',)
admin.site.register(Output, OutputAdmin)

class SubsatkrAdmin(admin.ModelAdmin):
	list_display = ('kddept', 'kdunit', 'kdkotama', 'kdsatkr', 'kdsubsatkr', 'nmsubsatkr')
	search_fields = ['nmsubsatkr']
	list_filter = ('nmsubsatkr',)
admin.site.register(Subsatkr, SubsatkrAdmin)

class WasgiatAdmin(admin.ModelAdmin):
	list_display = ('kdwasgiat', 'nmwasgiat')
	search_fields = ['nmwasgiat']
	list_filter = ('nmwasgiat',)
admin.site.register(Wasgiat, WasgiatAdmin)

class KegiatanAdmin(admin.ModelAdmin):
	list_display = ('kdkegiatan', 'nmkegiatan', 'keterangan', 'budget', 'status', 'created_by', 'parent')
	search_fields = ['nmkegiatan']
	list_filter = ('nmkegiatan',)
admin.site.register(Kegiatan, KegiatanAdmin)	

admin.site.register(Bulan)

# https://stackoverflow.com/questions/51492206/how-can-i-add-a-link-to-download-a-file-in-a-django-admin-detail-page
# https://impythonist.wordpress.com/2016/08/05/building-an-excel-file-dump-service-in-django/
# https://xlsxwriter.readthedocs.io/example_django_simple.html
# https://stackoverflow.com/questions/40160738/why-does-xlsxwriter-export-the-data-in-my-database-from-django-admin-to-excel-in

# 