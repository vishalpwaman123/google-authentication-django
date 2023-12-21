from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, generics, views
from django.contrib.sites.shortcuts import get_current_site
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import *
from .validations import *
from .models import *
from .services import *

# Create your views here.

# Sign Up Api


class signUpView(GenericAPIView):
    serializer_class = signUpSerializer

    def post(self, request):
        try:
            # Validation
            Validation_Response = signUpView_Validation(request)
            if Validation_Response:
                return Response(Validation_Response, status=status.HTTP_400_BAD_REQUEST)

            # Email id already present or not
            try:
                email_Response = UserAccountDetail.objects.get(
                    email=request.data.get('email'))
                data = {
                    "message": "Signup Unsuccessful. Email id already present",
                    "data": request.data
                }
                # return Response(message=data, status=status.HTTP_400_BAD_REQUEST)
                return Response({"data": {"message": "Unsuccessful"}}, 400)
            except:
                # Email id Not found
                pass

            # Password match
            if request.data.get("password") != request.data.get("confirmpassword"):
                Message = "Password not match"
                return Response(Message, status=status.HTTP_400_BAD_REQUEST)

            # Save in Database process
            try:
                Serializer_class = signUpFinalSerializer(data=request.data)
                if Serializer_class.is_valid():
                    Serializer_class.save()
                    data = {
                        "message": "Sign up Successful",
                        "data": request.data
                    }
                    print(data)
                    return Response(data, status=status.HTTP_201_CREATED)
                data = {
                    "message": "Sign Up Failed",
                    "data": request.data
                }
                print(data)
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            except:
                data = {
                    "message": "Error in Database",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            data = {
                "message": "Sign Up Exception",
                "Exception": Exception
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Sign In Enter Email Api


class signInEmailView(GenericAPIView):
    serializer_class = signInEmailSerializer

    def post(self, request):
        try:
            validation_Response = EmailView_Validation(request)
            if validation_Response:
                return Response(validation_Response, status=status.HTTP_400_BAD_REQUEST)

            # Check Email Id Present Or not
            try:
                email_Response = UserAccountDetail.objects.get(
                    email=request.data.get('email'))
            except:
                data = {
                    "message ": "Email Id Not Found",
                    "data ": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # Check Account Verified or not
            if email_Response.is_verified == False:
                data = {
                    "message": "Account Not Verified"
                }
                return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)

            serializer_class = AllDataSerializer(email_Response, many=False)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Sign In Enter Password Api


class signInPasswordView(GenericAPIView):
    serializer_class = signInPasswordSerializer

    def post(self, request):
        try:
            validation_Response = signInPasswordView_Validation(request)
            if validation_Response:
                return Response(validation_Response, status=status.HTTP_400_BAD_REQUEST)

            try:
                signIn_Response = UserAccountDetail.objects.get(
                    email=request.data.get('email'), password=request.data.get("password"))
            except:
                data = {
                    "message ": "Sign In Failed",
                    "data ": request.data
                }
                return Response(data, status=status.HTTP_401_UNAUTHORIZED)

            serializer_class = AllDataSerializer(signIn_Response, many=False)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Find Email Api


class FindEmailView(GenericAPIView):
    serializer_class = findEmailSerializer

    def post(self, request):
        try:
            validation_Response = EmailView_Validation(request)
            if validation_Response:
                return Response(validation_Response, status=status.HTTP_400_BAD_REQUEST)

            try:
                email_Response = UserAccountDetail.objects.get(
                    email=request.data.get('email'))
            except:
                data = {
                    "message ": "Email Id Not Found",
                    "data ": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            serializer_class = AllDataSerializer(email_Response, many=False)
            data = {
                "message": "Email Id found in database",
                "data": serializer_class.data
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Find Email Using First & Last Name


class FindEmailEnterFLNameView(GenericAPIView):
    serializer_class = FindEmailEnterFLNameSerializer

    def post(self, request):
        try:
            validation_Response = FindEmailEnterFLNameValidation(request)
            if validation_Response:
                return Response(validation_Response, status=status.HTTP_400_BAD_REQUEST)

            try:
                data_Response = UserAccountDetail.objects.get(
                    email=request.data.get('email'),
                    firstname=request.data.get('firstname'),
                    lastname=request.data.get('lastname'))
            except:
                data = {
                    "message ": "Data Not Found",
                    "data ": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            serializer_class = AllDataSerializer(data_Response, many=False)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Send Otp On Email Api


class SendOtpOnEmailView(GenericAPIView):
    serializer_class = SendOtpOnEmailSerializer

    def post(self, request):
        try:
            # Check Internet Connection
            CheckInternetConnection = InternetServices.CheckInternetConnection()
            if CheckInternetConnection['status'] == 500:
                return Response(CheckInternetConnection, status=status.HTTP_503_SERVICE_UNAVAILABLE)

            # Check Validation
            validation_Response = EmailView_Validation(request)
            if validation_Response:
                return Response(validation_Response, status=status.HTTP_400_BAD_REQUEST)

            try:
                email_Response = UserAccountDetail.objects.get(
                    email=request.data.get('email'))
            except:
                data = {
                    "message": "Invalid Email Id",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # Create Otp by Service
            otp = OtpService.generateOtp()
            if not otp:
                return Response("Otp service Error", status=status.HTTP_404_NOT_FOUND)

            # Send Email Service
            Sendemail_Response = EmailService.send_OtpOnEmail(
                otp, request.data.get('email'))
            if not Sendemail_Response:
                data = {
                    "message ": "Send Otp Error",
                    "data ": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # Save Otp detail In database
            flagStatus = OtpService.saveOtpInEmaildatabase(email_Response.user_id, otp,
                                                           request.data.get('email'))
            if flagStatus == 0:
                Message = "Email Send successfully"

            elif flagStatus == 1:
                Message = "Email Id not valid"

            elif flagStatus == 2:
                Message = "Otp database error"

            elif flagStatus == 3:
                Message = "Internel Server Error"

            data = {
                "message": Message,
                "data": request.data
            }
            if flagStatus == 0:
                return Response(data, status=status.HTTP_200_OK)

            elif flagStatus == 1 or flagStatus == 2:
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Email Otp Verification Api


class EmailOtpVerificationView(GenericAPIView):

    serializer_class = EmailOtpVerificationSerializer

    def post(self, request):
        try:
            c = connection.cursor()
            validation_Response = EmailOtpVerificationValidation(request)
            if validation_Response:
                return Response(validation_Response, status=status.HTTP_400_BAD_REQUEST)

            email = request.data.get("email")
            Request_otp = request.data.get("Otp")
            try:
                c.execute(
                    "SELECT * FROM authentication_emailotpauthenticationsystem WHERE email=%s", [email])
                user = c.fetchall()
                # print("User :", user)
                # print("Index :", user[0][0])

                try:
                    c.execute("SELECT Otp FROM authentication_emailotpauthenticationsystem WHERE email=%s", [
                              email])
                    user = c.fetchall()
                    Real_otp = user[0][0]
                    print(int(Real_otp) == int(Request_otp))
                    if Real_otp == int(Request_otp):
                        try:
                            c.execute("SELECT * FROM authentication_useraccountdetail WHERE email=%s", [
                                email])
                            user = c.fetchall()
                            # Fetch first name in database
                            firstName = user[0][1]
                            # Fetch last name in database
                            lastName = user[0][2]
                            # Fetch mobile number in database
                            mobileNumber = user[0][4]
                            print("first Name ", firstName,
                                  "\nlast Name", lastName,
                                  "\nmobile Number", mobileNumber)
                        except:
                            data = {
                                "message": "Fetch error at first, last name , mobile number error",
                                "data": request.data
                            }
                            return Response(data, status=status.HTTP_400_BAD_REQUEST)
                        data = {
                            "message": "Otp Match",
                            "data": {
                                "firstname": firstName,
                                "lastname": lastName,
                                "mobile": mobileNumber
                            }
                        }
                        return Response(data, status=status.HTTP_202_ACCEPTED)
                    Message = "Invalid Otp"
                    return Response(Message, status=status.HTTP_400_BAD_REQUEST)
                except:
                    Message = "Exception at otp matching"
                    return Response(Message, status=status.HTTP_406_NOT_ACCEPTABLE)

            except:
                Message = "Email Not Found"
                return Response(Message, status=status.HTTP_406_NOT_ACCEPTABLE)
        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Enter mobile number Api


class EnterMobileNumberView(GenericAPIView):

    serializer_class = EnterMobileNumberSerializer

    def post(self, request):
        try:
            c = connection.cursor()
            validation_Response = EnterMobileNumberValidation(request)
            if validation_Response:
                return Response(validation_Response, status=status.HTTP_400_BAD_REQUEST)
            email = request.data.get('email')
            mobileNumber = request.data.get('mobileNumber')
            try:
                c.execute(
                    "SELECT user_id FROM authentication_useraccountdetail WHERE email=%s", [email])
                user = c.fetchall()
                user_id = user[0][0]
                try:
                    c.execute(
                        "UPDATE authentication_useraccountdetail set mobile = %s WHERE email=%s", [mobileNumber, email])
                    data = {
                        "message": "Mobile number save successfully",
                        "data": request.data
                    }
                    return Response(data, status=status.HTTP_200_OK)
                except:
                    data = {
                        "message ": "Something Error In Mobile number in Updation",
                        "data": request.data
                    }
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
            except:
                data = {
                    "message": "Email Id Not Found",
                    "data": request.data
                }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Send Otp on mobile number Api


class SendOtpOnMobileNumberView(GenericAPIView):
    serializer_class = SendOtpOnMobileNumberSerializer

    def post(self, request):
        try:
            # Check Internet Connection
            CheckInternetConnection = InternetServices.CheckInternetConnection()
            if CheckInternetConnection['status'] == 500:
                return Response(CheckInternetConnection, status=status.HTTP_503_SERVICE_UNAVAILABLE)

            c = connection.cursor()

            # EmailOtpVerificationValidation same as Enter mobile Number View
            validation_Response = EnterMobileNumberValidation(request)
            if validation_Response:
                return Response(validation_Response, status=status.HTTP_400_BAD_REQUEST)

            email = request.data.get('email')
            mobileNumber = request.data.get('mobileNumber')
            try:
                c.execute(
                    "SELECT user_id FROM authentication_useraccountdetail WHERE email=%s and mobile=%s", [email, mobileNumber])
                user = c.fetchall()
                user_id = user[0][0]
                try:
                    # Generate Otp
                    otp_variable = OtpService.generateOtp()

                    # Send otp on Mobile Number
                    Sendotp_Result = OtpService.SendOtpOnMobileNumber(
                        otp_variable, mobileNumber, request)

                    if Sendotp_Result['status'] == 500:
                        return Response(Sendotp_Result, status=status.HTTP_417_EXPECTATION_FAILED)

                    # Save Otp Information Into database
                    flagStatus = OtpService.saveOtpInMobiledatabase(
                        user_id, otp_variable, mobileNumber)
                    if flagStatus == 0:
                        Message = "Save OTP detail successfully"

                    elif flagStatus == 1:
                        Message = "Email Id not valid"

                    elif flagStatus == 2:
                        Message = "Otp database error"

                    elif flagStatus == 3:
                        Message = "Internel Server Error"

                    data = {
                        "message": Message,
                        "data": request.data,
                        "user_id": user_id
                    }
                    if flagStatus == 0:
                        return Response(data, status=status.HTTP_200_OK)

                    elif flagStatus == 1 or flagStatus == 2:
                        return Response(data, status=status.HTTP_400_BAD_REQUEST)

                    else:
                        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                    data = {
                        "message": "Mobile number save successfully",
                        "data": request.data
                    }
                    return Response(data, status=status.HTTP_200_OK)
                except:
                    data = {
                        "message ": "Error Occur in Otp Processing",
                        "data": request.data
                    }
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
            except:
                data = {
                    "message": "Email Id or mobile number combination not found in database",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Mobile Otp verification Api


class MobileOtpVerificationView(GenericAPIView):
    serializer_class = MobileOtpVerificationSerializer

    def post(self, request):
        try:
            # Validation
            validation_Response = MobileOtpVerificationValidation(request)
            if validation_Response:
                return Response(validation_Response, status=status.HTTP_400_BAD_REQUEST)

            # Database Connection
            c = connection.cursor()
            email = request.data.get('email')
            mobile = request.data.get('mobileNumber')
            request_otp = request.data.get('Otp')

            try:
                userDetail = UserAccountDetail.objects.get(
                    email=request.data.get('email'), mobile=request.data.get('mobileNumber'))
            except:
                data = {
                    "message": "email & mobile Detail not match",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            try:
                # Check valid email Or not
                c.execute(
                    "SELECT * FROM authentication_useraccountdetail WHERE email=%s", [email])
                user = c.fetchall()
                # print("User :", user)
                # print("Index :", user[0][0])
                try:
                    # Check mobile number valid or not
                    c.execute(
                        "SELECT Otp FROM authentication_mobileotpauthenticationsystem WHERE mobile=%s", [mobile])
                    user = c.fetchall()
                    # print("User :", user)
                    # print("Index :", user[0][0])
                    database_Otp = user[0][0]

                    if int(database_Otp) == int(request_otp):
                        try:
                            # Update Verification bit
                            c.execute(
                                "UPDATE authentication_useraccountdetail SET is_verified = 1 where mobile=%s", [mobile])
                        except:
                            data = {
                                "message ": "Error occur at Verification bit modification",
                                "data ": request.data
                            }
                            return Response(data, status=status.HTTP_304_NOT_MODIFIED)
                        data = {
                            "message": "Otp Match",
                            "data": request.data,
                            "user_id": userDetail.user_id
                        }
                        return Response(data, status=status.HTTP_202_ACCEPTED)
                    data = {
                        "message": "Otp not match",
                        "data": request.data
                    }
                    return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
                except:
                    # Invalid mobile number
                    data = {
                        "message": "Invalid Mobile ",
                        "data": request.data
                    }
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
            except:
                # Invalid Email id
                data = {
                    "message": "Invalid Email id",
                    "data ": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Send Verification Link on Regster Email Id Api


class SendVerificationLinkOnEmailView(GenericAPIView):
    serializer_class = SendVerificationLinkOnEmailSerializer

    def post(self, request):
        try:
            # Check Internet Connection
            CheckInternetConnection = InternetServices.CheckInternetConnection()
            if CheckInternetConnection['status'] == 500:
                return Response(CheckInternetConnection, status=status.HTTP_503_SERVICE_UNAVAILABLE)

            # Check Validation
            print("flag 1")
            validation_Response = EmailView_Validation(request)
            if validation_Response:
                return Response(validation_Response, status=status.HTTP_400_BAD_REQUEST)

            try:
                print("flag 2")
                email_Response = UserAccountDetail.objects.get(
                    email=request.data.get('email'))
            except:
                data = {
                    "message": "Invalid Email Id",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # Create Otp
            print("flag 3")
            otp_variable = OtpService.generateOtp()

            # Create token
            print("flag 4")
            token_Response = TokenService.EncodeTokenWithOtp(
                email_Response.user_id, request.data.get('email'))
            if not token_Response:
                data = {
                    "message": "Token Encoding Error",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # Send Email Service
            Sendemail_Response = EmailService.send_VerificationLinkOnEmail(
                request.data.get('email'), token_Response['AccessToken'])
            if not Sendemail_Response:
                data = {
                    "message ": "Send Link Error",
                    "data ": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            data = {
                "message": "Send Verification Link Sucessfully",
                "data": request.data,
                "token": token_Response['AccessToken'],
            }
            return Response(data, status=status.HTTP_200_OK)

        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Verified Account Via Email Id Verification Link Api


class VerifiedAccountViaLinkView(GenericAPIView):
    serializer_class = VerifiedAccountViaLinkSerializer

    def post(self, request):
        try:

            Validation_Response = Token_Validation(request)
            if Validation_Response:
                return Response("Validation Error", status=status.HTTP_400_BAD_REQUEST)

            token = request.data.get('token')
            decodeToken_Response = TokenService.DecodeToken(token)
            if not decodeToken_Response:
                data = {
                    "message": "Token decode Error",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            try:
                # Database Connection
                c = connection.cursor()
                c.execute(
                    "Update authentication_useraccountdetail set is_verified = 1 WHERE email=%s", [decodeToken_Response['email']])
                data = {
                    "message": "Account Verified Successfully",
                    "data": {"email":
                             decodeToken_Response['email'],
                             "user_id": decodeToken_Response['user_id']
                             }
                }
                return Response(data, status=status.HTTP_200_OK)
            except:
                data = {
                    "message ": "Error in database updation",
                    "data ": request.data
                }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Reset Password Api


class ResetPasswordView(GenericAPIView):
    serializer_class = resetPasswordSerializer

    def post(self, request):
        try:
            Validation_Response = ResetPassword_Validation(request)
            if Validation_Response:
                return Response("Validation Error", status=status.HTTP_400_BAD_REQUEST)

            try:
                email = request.data.get('email')
                password = request.data.get('password')
                confirmPassword = request.data.get('confirmPassword')

                if str(password) != str(confirmPassword):
                    data = {
                        "message": "Password & Confirm Password not match",
                        "data": request.data
                    }
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)

                email_Response = UserAccountDetail.objects.get(
                    email=email)
                try:
                    # Database Connection
                    c = connection.cursor()
                    c.execute(
                        "UPDATE authentication_useraccountdetail SET password = %s WHERE email=%s", [password, email])
                    # user = c.fetchall()
                    # print("User :", user)
                    # print("Index :", user[0][0])
                    data = {
                        "message": "password update successfully.",
                        "firstName": email_Response.firstname,
                        "lastName": email_Response.lastname,
                        "mobileNumber": email_Response.mobile
                    }
                    return Response(data, status=status.HTTP_200_OK)
                except:
                    data = {
                        "message ": "Error Occur at data Updation",
                        "data": request.data
                    }
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
            except:
                data = {
                    "message ": "Invalid Email Id",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Send Resetpassword Link to Email


class SendResetPasswordVerificationLinkOnEmailView(GenericAPIView):
    serializer_class = SendResetPasswordVerificationLinkOnEmailSerializer

    def post(self, request):
        try:
            # Check Internet Connection
            CheckInternetConnection = InternetServices.CheckInternetConnection()
            if CheckInternetConnection['status'] == 500:
                return Response(CheckInternetConnection, status=status.HTTP_503_SERVICE_UNAVAILABLE)

            # Verification
            Validation_Response = ResetPasswordVerification_Validation(request)
            if Validation_Response:
                return Response("Validation Error", status=status.HTTP_400_BAD_REQUEST)

            try:
                email_Response = UserAccountDetail.objects.get(
                    email=request.data.get('email'))
            except:
                data = {
                    "message": "Invalid Email Id",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # Create token
            token_Response = TokenService.EncodeTokenWithOtp(
                email_Response.user_id, request.data.get('email'))
            if not token_Response:
                data = {
                    "message": "Token Encoding Error",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # Send Email Service
            Sendemail_Response = EmailService.send_ResetPasswordLinkOnEmail(
                request.data.get('email'), token_Response['AccessToken'])
            if not Sendemail_Response:
                data = {
                    "message ": "Send Link Error",
                    "data ": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            data = {
                "message": "Send Verification Link Sucessfully",
                "data": request.data,
                "token": token_Response['AccessToken'],
            }
            return Response(data, status=status.HTTP_200_OK)

        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Decode JWT token


class DecodeJWTTokenView(GenericAPIView):
    serializer_class = DecodeJwtTokenSerializers

    def post(self, request):
        try:
            # Validation
            Validation_Response = DecodeTokenValidation_Validation(request)
            if Validation_Response:
                return Response("Validation Error", status=status.HTTP_400_BAD_REQUEST)

            # Decode Token token
            token_Response = TokenService.DecodeToken(
                request.data.get('token'))
            if not token_Response:
                data = {
                    "message": "Token Decoding Error",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            data = {
                "message ": "Jwt Token decode Successfully",
                "user_id": token_Response['user_id'],
                "email": token_Response['email']
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Encode JWT Token


class EncodeJWTTokenView(GenericAPIView):
    serializer_class = EncodeTokenSerializer

    def post(self, request):
        try:
            # Validation
            Validation_Response = EncodeTokenValidation_Validation(request)
            if Validation_Response:
                return Response("Validation Error", status=status.HTTP_400_BAD_REQUEST)

            try:
                email_Response = UserAccountDetail.objects.get(
                    email=request.data.get('email'), user_id=request.data.get('user_id'))
            except:
                data = {
                    "message": "user_id & email Not Match In database",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # Create Token
            token_Response = TokenService.EncodeToken(
                request.data.get('user_id'), request.data.get('email'))
            if not token_Response:
                data = {
                    "message": "Token Encoding Error",
                    "data": request.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            data = {
                "message ": "Jwt Token Encode Successfully",
                "accessToken": token_Response['AccessToken']
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            data = {
                "message ": "Internal Server Error",
                "data ": request.data
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
