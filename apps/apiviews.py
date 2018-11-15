from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)
from django.contrib.auth import authenticate
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer

from .models import (Akun, Dept, Program, Giat, Unit, Kotam, Satkun, Satkr)
from .serializers import (
		AkunSerializer, DeptSerializer, ProgramSerializer, GiatSerializer, UserSerializer,
		UnitSerializer, KotamSerializer, SatkunSerializer, SatkrSerializer, SubsatkrSerializer,
		WasgiatSerializer
		)

# class LoginView(APIView):
# 	permission_classes = ()

# 	def post(self, request, ):
# 		username = request.data.get("username")
# 		password = request.data.get("password")
# 		user = authenticate(username=username, password=password)
# 		if user:
# 			return Response({"token": user.auth_token.key})
# 		else:
# 			return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provpke both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalpk Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)



class UserCreate(generics.CreateAPIView):
	authenticatation_classes = ()
	permission_classes = ()
	serializer_class = UserSerializer


class AkunList(APIView):
	def get(self, request):
		akuns = Akun.objects.all()[:20]
		serializers = AkunSerializer(akuns, many=True)
		return Response(serializers.data)

class AkunDetail(APIView):
	def get(self, request, pk):
		akun = get_objects_or_404(Akun, pk=pk)
		data = AkunSerializer(akun).data
		return Response(data)

class DeptList(APIView):
	# queryset = Dept.objects.all()
	# serializer_class = DeptSerializer
	# renderer_classes = (XLSXRenderer,)
	# filename = 'dept_export.xlsx'
	
	def get(self, request, ):
		depts = Dept.objects.all()[:20]
		serializers = DeptSerializer(depts, many=True)
		return Response(serializers.data)

	def post(self, request, format=None):
		serializer = DeptSerializer(data=request.data)
		if serializer.is_valpk():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeptDetail(APIView):
	def get_object(self, pk):
		try:
			return Dept.objects.get(pk=pk)
		except Dept.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		dept = self.get_object(pk)
		data = DeptSerializer(dept)
		return Response(dept.data)

	def put(self, request, pk, format=None):
		dept = self.get_object(pk)
		serializer = DeptSerializer(dept, data=request.data)
		if serializer.is_valpk():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		dept = self.get_object(pk)
		dept.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class ProgramList(APIView):
	def get(self, request):
		programs = Program.objects.all()[:20]
		serializers = ProgramSerializer(programs, many=True)
		return Response(serializers.data)

class ProgramDetail(APIView):
	def get(self, request, pk):
		program = get_objects_or_404(Program, pk=pk)
		serializers = ProgramSerializer(Program)
		return Response(serializers.data)

class GiatList(APIView):
	def get(self, request):
		giats = Giat.objects.all()[:20]
		serializers = GiatSerializer(giats, many=True)
		return Response(serializers.data)

class GiatDetail(APIView):
	def get(self, request, pk):
		giat = get_objects_or_404(Giat, pk=pk)
		data = GiatSerializer(giat)
		return Response(data)

class UnitList(APIView):
	def get(self, request):
		units = Unit.objects.all()
		serializers = UnitSerializer(units, many=True)
		return Response(serializers.data)

class UnitDetail(APIView):
	def get(self, request, pk):
		unit = get_objects_or_404(Unit, pk=pk)
		data = UnitSerializer(unit)
		return Response(data)



# session_key, session_data, expire_date