from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from .apiviews import *
from rest_framework.authtoken import views

# router = DefaultRouter()
# router.register('apps', GiatViewSet, base_name='giats')

urlpatterns = [
	# path("login/", LoginView.as_view(), name='login'),
	path("login/", login, name='login'),
	path("users/", UserCreate.as_view(), name="user-create"),

	path("home/", home, name="home"),

	path("akun/", AkunList.as_view(), name="akun-list"),
	path("akun/<int:id>/", AkunDetail.as_view(), name="akun-detail"),
	path("dept/", DeptList.as_view(), name="dept-list"),
	path("dept/<int:pk>/", DeptDetail.as_view(), name="dept-detail"),
	path("program/", ProgramList.as_view(), name="program-list"),
	path("program/<int:pk>/", ProgramDetail.as_view(), name="program-detail"),
	path("giat/", GiatList.as_view(), name="giat-list"),
	path("giat/<int:pk>/", GiatDetail.as_view(), name="giat-detail"),
	path("unit/", UnitList.as_view(), name="unit-list"),
	path("unit/<int:pk>/", UnitDetail.as_view(), name="unit-detail"),
	# path("export/", export_xls, name='export-xls'),
	# path("")
	path("exportakun/", export_akun, name='export-akun'),
	path("exportbulan/", export_bulan, name='export-bulan'),
	path("exportfungsi/", export_fungsi, name='export-fungsi'),
	path("exportprogram/", export_program, name='export-program'),
	path("exportgiat/", export_giat, name='export-giat'),
	path("exportkegiatan/", export_kegiatan, name='export-kegiatan'),
	path("exportkotam/", export_kotam, name='export-kotam'),
	path("exportoutput/", export_output, name='export-output'),
	path("exportdept/", export_dept, name='export-dept'),
	path("exportsatkun/", export_satkun, name='export-satkun'),
	path("exportsatkur/", export_satkur, name='export-satkur'),
	path("exportsubsatkur/", export_subsatkr, name='export-subsatkur'),
	path("exporttingkat/", export_tingkat, name='export-tingkat'),
	path("exportunit/", export_unit, name='export-unit'),
]

# urlpatterns += router.urlsx  http://indoxx1.club/munafik-2-2018/