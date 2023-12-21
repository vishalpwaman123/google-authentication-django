from decouple import config
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.utils import timezone
import jwt
import random
import math
import smtplib
import requests
import json

# Database library File
from django.db import connection

# Templete
from .templete.otptemplete import *
from .templete.SendVerificationLinktemplete import *
from .serializers import *

# Email Service Header File
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from datetime import datetime, timedelta


class EmailService:
    Response = None

    @staticmethod
    def send_OtpOnEmail(data, email):
        try:
            print("flag SE 1")
            to_addr = str(email)
            from_addr = config("EMAIL_HOST_USER")
            password = config("EMAIL_HOST_PASSWORD")
            smtp = config("EMAIL_HOST")

            print("MIME Setting")
            msgRoot = MIMEMultipart('related')
            msgRoot['Subject'] = 'Verify your Account'
            msgRoot['From'] = from_addr
            msgRoot['To'] = to_addr
            msgRoot.preamble = 'This is a multi-part message in MIME format.'

            # Encapsulate the plain and HTML versions of the message body in an
            # 'alternative' part, so message agents can decide which they want to display.
            msgAlternative = MIMEMultipart('alternative')
            msgRoot.attach(msgAlternative)

            msgText = MIMEText('This email was sent from Python')
            msgAlternative.attach(msgText)

            # We reference the image in the IMG SRC attribute by the ID we give it below
            # Create Send Otp Html Body
            print("Html Format start")
            html = SendOtpHtmlBody.GenerateOtpHtmlBody(data)
            if not html:
                return False
            msgText = MIMEText(html, 'html')
            msgAlternative.attach(msgText)

            # Send Email
            s = smtplib.SMTP(smtp, 587)
            s.starttls()
            s.login(from_addr, password)
            s.sendmail(from_addr, to_addr, msgRoot.as_string())
            s.quit()
            print("Email Send successfully")
            return True
        except:
            return False

    @staticmethod
    def send_VerificationLinkOnEmail(email, token):
        try:
            print("flag SE 1", str(email))
            to_addr = str(email)
            from_addr = config("EMAIL_HOST_USER")
            password = config("EMAIL_HOST_PASSWORD")
            smtp = config("EMAIL_HOST")

            print("MIME Setting")
            msgRoot = MIMEMultipart('related')
            msgRoot['Subject'] = 'Verify your Account'
            msgRoot['From'] = from_addr
            msgRoot['To'] = to_addr
            msgRoot.preamble = 'This is a multi-part message in MIME format.'

            # Encapsulate the plain and HTML versions of the message body in an
            # 'alternative' part, so message agents can decide which they want to display.
            msgAlternative = MIMEMultipart('alternative')
            msgRoot.attach(msgAlternative)

            msgText = MIMEText('This email was sent from Python')
            msgAlternative.attach(msgText)

            # We reference the image in the IMG SRC attribute by the ID we give it below
            # Create Send Otp Html Body
            print("Html Format start")
            html = SendVerificationLinkHtmlBody.GenerateVerificationLinkHtmlBody(
                token)
            # print("html :", html)
            if not html:
                return False
            msgText = MIMEText(html, 'html')
            msgAlternative.attach(msgText)

            # Send Email
            s = smtplib.SMTP(smtp, 587)
            s.starttls()
            s.login(from_addr, password)
            s.sendmail(from_addr, to_addr, msgRoot.as_string())
            s.quit()
            print("Email Send successfully")
            return True
        except:
            return False

    @staticmethod
    def send_ResetPasswordLinkOnEmail(email, token):
        try:
            print("flag SE 1", str(email))
            to_addr = str(email)
            from_addr = config("EMAIL_HOST_USER")
            password = config("EMAIL_HOST_PASSWORD")
            smtp = config("EMAIL_HOST")

            print("MIME Setting")
            msgRoot = MIMEMultipart('related')
            msgRoot['Subject'] = 'Verify your Account'
            msgRoot['From'] = from_addr
            msgRoot['To'] = to_addr
            msgRoot.preamble = 'This is a multi-part message in MIME format.'

            # Encapsulate the plain and HTML versions of the message body in an
            # 'alternative' part, so message agents can decide which they want to display.
            msgAlternative = MIMEMultipart('alternative')
            msgRoot.attach(msgAlternative)

            msgText = MIMEText('This email was sent from Python')
            msgAlternative.attach(msgText)

            # We reference the image in the IMG SRC attribute by the ID we give it below
            # Create Send Otp Html Body
            print("Html Format start")
            html = SendVerificationLinkHtmlBody.SendResetPasswordVerificationLinkOnEmail(
                token)
            # print("html :", html)
            if not html:
                return False
            msgText = MIMEText(html, 'html')
            msgAlternative.attach(msgText)

            # Send Email
            s = smtplib.SMTP(smtp, 587)
            s.starttls()
            s.login(from_addr, password)
            s.sendmail(from_addr, to_addr, msgRoot.as_string())
            s.quit()
            print("Email Send successfully")
            return True
        except:
            return False


class TokenService:

    @staticmethod
    def EncodeToken(user_id, email):
        try:
            Token_Payload = {
                'user_id': user_id,
                'email': email,
                'exp': timezone.now()+timedelta(seconds=settings.JWT_EXPIRATION_TIME)
            }
            access_token = jwt.encode(Token_Payload, config(
                'JWT_SECRET_KEY'), algorithm=config('JWT_ALGORITHM'))
            print("access_token", access_token)

            token = {
                "AccessToken": access_token
            }
            return token
        except:
            return False

    @staticmethod
    def DecodeToken(token):
        try:
            print("SECRET KEY :", settings.SECRET_KEY)
            decode = jwt.decode(token, settings.SECRET_KEY,
                                options={"verify_signature": False})
            print("user id ", decode['user_id'])
            print("email id ", decode['email'])
            return decode
        except:
            return False

    @staticmethod
    def EncodeTokenWithOtp(user_id, email):
        try:
            Token_Payload = {
                'user_id': user_id,
                'email': email,
                'exp': timezone.now()+timedelta(seconds=settings.JWT_EXPIRATION_TIME)
            }
            access_token = jwt.encode(Token_Payload, config(
                'JWT_SECRET_KEY'), algorithm=config('JWT_ALGORITHM'))
            print("access_token", access_token)

            token = {
                "AccessToken": access_token
            }
            return token
        except:
            return False


class OtpService:

    @staticmethod
    def generateOtp():
        try:
            digits = "0123456789"
            otp_variable = ""
            for i in range(6):
                otp_variable += digits[math.floor(random.random() * 10)]

            return otp_variable
        except:
            return False

    @staticmethod
    def saveOtpInEmaildatabase(user_id, otp, email):
        try:
            otp_count = None
            print("user_id ", user_id,
                  " otp ", otp,
                  " email ", email)

            c = connection.cursor()
            try:
                try:
                    c.execute("SELECT Otp_Created_Count FROM authentication_emailotpauthenticationsystem WHERE email=%s", [
                        email])
                    user = c.fetchall()
                    otp_count = user[0][0]
                except:
                    otp_count = 0
            except:
                # Email Id not valid
                Flag = 1
                return Flag

            otp_count += 1
            print("otp_count", otp_count)
            try:
                if otp_count == 1:
                    present_time = datetime.now()
                    expire_date_after_20minute = present_time + \
                        timedelta(minutes=20)

                    print("present time ", present_time)
                    print("Expire time ", expire_date_after_20minute)
                    otp_data = {
                        "user_id": user_id,
                        "email": email,
                        "Otp": otp,
                        "Otp_Created_Count": otp_count,
                        "Expire_Time": str(expire_date_after_20minute)
                    }
                    print(otp_data)
                    serializers = EmailOtpDetailSerializer(data=otp_data)
                    print("serializers ", serializers.is_valid())
                    if serializers.is_valid():
                        print("before save")
                        serializers.save()
                        print("After save")
                        Flag = 0
                        return Flag
                    Flag = 4
                    return Flag

                else:
                    print("update")
                    c.execute("UPDATE authentication_emailotpauthenticationsystem SET Otp = %s , Otp_Created_Count = %s WHERE email = %s", [
                              otp, otp_count, email])
                    Flag = 0
                    return Flag
            except Exception:
                # Otp save database errro
                print(Exception)
                Flag = 2
                return Flag

        except:
            Flag = 3
            return Flag

    @staticmethod
    def SendOtpOnMobileNumber(otp_variable, mobileNumber, request):
        try:
            Message = "Your V Technology Account OTP : " + otp_variable
            print("Message ", Message)
            url = str(settings.URL)
            print("url ", url)
            print("sender id ", config("SENDER_ID"))
            my_data = {
                'sender_id': str(config("SENDER_ID")),
                'message': str(Message),
                'language': 'english',
                'route': 'p',
                'numbers': str(request.data.get("mobileNumber"))
            }
            print("My data", my_data)
            headers = {
                'authorization': str(config("AUTHENTICATION_ID")),
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            print("Header ", headers)
            response = requests.request("POST",
                                        url,
                                        data=my_data,
                                        headers=headers)
            returned_msg = json.loads(response.text)
            print(returned_msg['message'])
            Data = {
                "status": 200,
                "Message": returned_msg['message']
            }
            return Data
        except:
            Data = {
                "status": 500,
                "Message": "Unexpected OTP Send Error"
            }
            return Data

    @staticmethod
    def saveOtpInMobiledatabase(user_id, otp, mobileNumber):
        try:
            otp_count = None
            print("user_id ", user_id,
                  " otp ", otp,
                  " email ", mobileNumber)

            c = connection.cursor()
            try:
                try:
                    c.execute("SELECT Otp_Created_Count FROM authentication_mobileotpauthenticationsystem WHERE mobile=%s", [
                        mobileNumber])
                    user = c.fetchall()
                    otp_count = user[0][0]
                except:
                    otp_count = 0
            except:
                # Email Id not valid
                Flag = 1
                return Flag

            otp_count += 1
            print("otp_count", otp_count)
            try:
                if otp_count == 1:
                    present_time = datetime.now()
                    expire_date_after_20minute = present_time + \
                        timedelta(minutes=20)

                    print("present time ", present_time)
                    print("Expire time ", expire_date_after_20minute)
                    otp_data = {
                        "user_id": user_id,
                        "mobile": mobileNumber,
                        "Otp": otp,
                        "Otp_Created_Count": otp_count,
                        "Expire_Time": str(expire_date_after_20minute)
                    }
                    print(otp_data)
                    serializers = MobileOtpDetailSerializer(data=otp_data)
                    print("serializers ", serializers.is_valid())
                    if serializers.is_valid():
                        print("before save")
                        serializers.save()
                        print("After save")
                        Flag = 0
                        return Flag
                    Flag = 4
                    return Flag

                else:
                    print("update")
                    c.execute("UPDATE authentication_mobileotpauthenticationsystem SET Otp = %s , Otp_Created_Count = %s WHERE mobile = %s", [
                              str(otp), str(otp_count), str(mobileNumber)])
                    Flag = 0
                    return Flag
            except Exception:
                # Otp save database errro
                print(Exception)
                Flag = 2
                return Flag

        except:
            Flag = 3
            return Flag


class InternetServices:

    @staticmethod
    def CheckInternetConnection():
        url = "http://www.google.com"
        timeout = 2  # time out in second
        try:
            request = requests.get(url, timeout=timeout)
            print("Connected to the Internet")
            data = {
                "status": 200,
                "Message": "Connected to the Internet"
            }
            return data
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")
            data = {
                "status": 500,
                "Message": "No internet connection"
            }
            return data
