from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import giat_list, giat_detail, GiatViewSet
from .apiviews import ( login,
	UserCreate, AkunList, AkunDetail, DeptList, DeptDetail,  
	ProgramList, ProgramDetail, GiatList, GiatDetail, UnitList, UnitDetail)
from rest_framework.authtoken import views

# router = DefaultRouter()
# router.register('apps', GiatViewSet, base_name='giats')

urlpatterns = [
	# path("login/", LoginView.as_view(), name='login'),
	path("login/", login, name='login'),
	path("users/", UserCreate.as_view(), name="user-create"),

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
	# path("akun/")

	# path("giat/", giat_list, name="giat"),
	# path("giat/<int:id>", giat_detail, name="giat-detail"),
]

# urlpatterns += router.urlsx