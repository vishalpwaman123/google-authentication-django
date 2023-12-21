from rest_framework import serializers
from .models import *


class AllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccountDetail
        fields = ['user_id', 'firstname', 'lastname', 'mobile',
                  'email', 'is_actived', 'created_at', 'updated_at']


class signUpSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(max_length=100)
    lastname = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=200)
    confirmpassword = serializers.CharField(max_length=200)

    class Meta:
        model = UserAccountDetail
        fields = ['firstname', 'lastname',
                  'email', 'password', 'confirmpassword']


class signUpFinalSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(max_length=100)
    lastname = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=200)

    class Meta:
        model = UserAccountDetail
        fields = ['firstname', 'lastname', 'email', 'password']


class signInEmailSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)

    class Meta:
        model = UserAccountDetail
        fields = ['email']


class signInPasswordSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=200)

    class Meta:
        model = UserAccountDetail
        fields = ['email', 'password']


class SendOtpOnEmailSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)

    class Meta:
        model = UserAccountDetail
        fields = ['email']


class findEmailSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)

    class Meta:
        model = UserAccountDetail
        fields = ['email']


class FindEmailEnterFLNameSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(max_length=100)
    lastname = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)

    class Meta:
        model = UserAccountDetail
        fields = ['firstname', 'lastname', 'email']


class EmailOtpDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailOtpAuthenticationSystem
        fields = ['user_id', 'email', 'Otp',
                  'Otp_Created_Count', 'Expire_Time']


class EmailOtpVerificationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    Otp = serializers.CharField(max_length=100)

    class Meta:
        model = EmailOtpAuthenticationSystem
        fields = ['email', 'Otp']


class EnterMobileNumberSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    mobileNumber = serializers.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        model = UserAccountDetail
        fields = ['email', 'mobileNumber']


class SendOtpOnMobileNumberSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    mobileNumber = serializers.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        model = UserAccountDetail
        fields = ['email', 'mobileNumber']


class MobileOtpVerificationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    mobileNumber = serializers.DecimalField(max_digits=10, decimal_places=0)
    Otp = serializers.CharField(max_length=100)

    class Meta:
        model = MobileOtpAuthenticationSystem
        fields = ['email', 'mobileNumber', 'Otp']


class MobileOtpDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileOtpAuthenticationSystem
        fields = ['user_id', 'mobile', 'Otp',
                  'Otp_Created_Count', 'Expire_Time']


class SendVerificationLinkOnEmailSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)

    class Meta:
        model = EmailOtpAuthenticationSystem
        fields = ['email']


class VerifiedAccountViaLinkSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=500)

    class Meta:
        model = EmailOtpAuthenticationSystem
        fields = ['token']


class resetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=200)
    confirmPassword = serializers.CharField(max_length=200)

    class Meta:
        model = UserAccountDetail
        fields = ['email', 'password', 'confirmPassword']


class SendResetPasswordVerificationLinkOnEmailSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)

    class Meta:
        model = UserAccountDetail
        fields = ['email']


class DecodeJwtTokenSerializers(serializers.ModelSerializer):
    token = serializers.CharField(max_length=500)

    class Meta:
        model = UserAccountDetail
        fields = ['token']


class EncodeTokenSerializer(serializers.ModelSerializer):
    user_id = serializers.DecimalField(max_digits=4, decimal_places=0)
    email = serializers.CharField(max_length=100)

    class Meta:
        model = UserAccountDetail
        fields = ['user_id', 'email']
