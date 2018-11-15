from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Akun, Dept, Program, Giat, Unit, Kotam, Satkun, Satkr, Subsatkr, Wasgiat

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User(
				email=validated_data['email'],
				username=validated_data['username']
			)
		user.set_password(validated_data['password'])
		user.save()
		Token.objects.create(user=user)
		return user

class AkunSerializer(serializers.ModelSerializer):
	nmakun = serializers.CharField(max_length=50)
	kdjenbel = serializers.IntegerField()
	tahun = serializers.DateField()

	class Meta:
		model = Akun
		fields = ('kdakun', 'nmakun', 'kdjenbel', 'tahun')

	def create(self, validated_data):
		nmakun = validated_data.pop('nmakun')
		instance = Akun.objects.create(**validated_data)

		for nama in nmakun:
			instance.nmakun.add(nama)
		return instance
		

class DeptSerializer(serializers.ModelSerializer):
	# akuns = AkunSerializer(many=True, read_only=True, required=True)

	class Meta:
		model = Dept
		fields = ('kddept', 'nmdept')


class ProgramSerializer(serializers.ModelSerializer):
	# depts = DeptSerializer(many=True, read_only=True, required=True)

	class Meta:
		model = Program
		fields = ('kdfungsi', 'kdsfungsi', 'kdprogram', 'nmprogram', 'tahun', 'versi')


class GiatSerializer(serializers.ModelSerializer):
	# programs = ProgramSerializer(many=True, read_only=True, required=True)

	class Meta:
		model = Giat
		fields = ('kdfungsi', 'kdsfungsi', 'kdprogram', 'kdgiat', 'nmgiat', 'versi', 'tahun')

class UnitSerializer(serializers.ModelSerializer):

	class Meta:
		model = Unit
		fields = ('kddept', 'kdunit', 'nmunit')


class KotamSerializer(serializers.ModelSerializer):

	class Meta:
		model = Kotam
		fields = ('kddept', 'kdunit', 'kdkotama', 'nmkotama', 'kdkukotama')


class SatkunSerializer(serializers.ModelSerializer):

	class Meta:
		model = Satkun
		fields = ('kdgiat', 'kdoutput', 'kdakun', 'kdsakun', 'nmsakun', 'kddipa')


class SatkrSerializer(serializers.ModelSerializer):

	class Meta:
		model = Satkr
		fields = ('kddept', 'kdunit', 'kdkotama', 'kdsatkr', 'nmsatkr', 'kdkusatkr')


class SubsatkrSerializer(serializers.ModelSerializer):

	class Meta:
		model = Subsatkr
		fields = ('kddept', 'kdunit', 'kdkotama', 'kdsatkr', 'kdsubsatkr', 'nmsubsatkr')


class WasgiatSerializer(serializers.ModelSerializer):

	class Meta:
		model = Wasgiat
		fields = ('kdwasgiat', 'nmwasgiat')