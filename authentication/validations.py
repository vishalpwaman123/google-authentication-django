import re

Email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
Password_regrex = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
Mobile_regrex = '^[7-9][0-9]{9}$'


def check_Email(email):
    if(re.search(Email_regex, email)):
        return False
    return True


def check_MobileNumber(mobileNumber):
    print("regrex", re.search(Mobile_regrex, mobileNumber))
    if (re.search(Mobile_regrex, mobileNumber)):
        return False
    return True


def check_Password(password):
    print(re.search(Password_regrex, password))
    if(re.search(Password_regrex, password)):
        return False
    return True


def parameter_Validation_Checker(attribute, attribute_value, request):
    if attribute is None or attribute == "":
        Message = attribute_value + " Is Required"
        data = {
            "Message": Message,
            "data": request.data
        }
        return data
    return False


def Otp_Validation_Checker(attribute, request):
    final_value = 999999
    if int(attribute) > final_value:
        Message = "Otp Must be 6 digit"
        data = {
            "Message : ": Message,
            "data : ": request.data
        }
        return data
    return False


def signUpView_Validation(request):
    try:
        firstname = request.data.get("firstname")
        Response = parameter_Validation_Checker(
            firstname, "firstname", request)
        if Response:
            return Response

        lastname = request.data.get("lastname")
        Response = parameter_Validation_Checker(
            lastname, "lastname", request)
        if Response:
            return Response

        email = request.data.get("email")
        Response = parameter_Validation_Checker(
            email, "email", request)
        if Response:
            return Response

        Response = check_Email(str(email))
        if Response:
            Message = "Invalid Email Id. Example : vishalpwaman@gmail.com"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data

        password = request.data.get("password")
        Response = parameter_Validation_Checker(password, "password", request)
        if Response:
            return Response

        Response = check_Password(str(password))
        print(Response)
        if Response:
            Message = "Use 8 or more characters with a mix of letters, numbers & symbols"
            data = {
                "Status": "Failed",
                "Message": Message,
                "data": request.data
            }
            return data

        confirmpassword = request.data.get("confirmpassword")
        Response = parameter_Validation_Checker(
            confirmpassword, "confirmpassword", request)
        if Response:
            return Response

        return False

    except:
        data = {
            "Message :": "Error In validation",
            "data :": request.data
        }
        return data


def EmailView_Validation(request):
    try:
        email = request.data.get("email")
        Response = parameter_Validation_Checker(
            email, "email", request)
        if Response:
            return Response

        Response = check_Email(str(email))
        if Response:
            Message = "Invalid Email Id. Example : vishalpwaman@gmail.com"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data
        return False

    except:
        data = {
            "Message ": "Error In Validation",
            "data ": request.data
        }
        return data


def signInPasswordView_Validation(request):
    try:
        email = request.data.get("email")
        Response = parameter_Validation_Checker(
            email, "email", request)
        if Response:
            return Response

        Response = check_Email(str(email))
        if Response:
            Message = "Invalid Email Id. Example : vishalpwaman@gmail.com"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data
        return False

        password = request.data.get("password")
        Response = parameter_Validation_Checker(password, "password", request)
        if Response:
            return Response

    except:
        data = {
            "Message ": "Error In Validation",
            "data ": request.data
        }
        return data


def FindEmailEnterFLNameValidation(request):
    try:
        firstname = request.data.get("firstname")
        Response = parameter_Validation_Checker(
            firstname, "firstname", request)
        if Response:
            return Response

        lastname = request.data.get("lastname")
        Response = parameter_Validation_Checker(
            lastname, "lastname", request)
        if Response:
            return Response

    except:
        data = {
            "Message ": "Error In Validation",
            "data ": request.data
        }
        return data


def EmailOtpVerificationValidation(request):
    try:
        email = request.data.get("email")
        Response = parameter_Validation_Checker(
            email, "email", request)
        if Response:
            return Response

        Response = check_Email(str(email))
        if Response:
            Message = "Invalid Email Id. Example : vishalpwaman@gmail.com"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data

        Otp = request.data.get("Otp")
        Response = Otp_Validation_Checker(Otp, request)
        if Response:
            return Response

        return False
    except:
        data = {
            "Message ": "Error In Validation",
            "data ": request.data
        }
        return data


def EnterMobileNumberValidation(request):
    try:
        email = request.data.get("email")
        Response = parameter_Validation_Checker(
            email, "email", request)
        if Response:
            return Response

        Response = check_Email(str(email))
        if Response:
            Message = "Invalid Email Id. Example : vishalpwaman@gmail.com"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data

        mobileNumber = request.data.get("mobileNumber")
        Response = parameter_Validation_Checker(
            mobileNumber, "mobile Number", request)
        if Response:
            return Response

        Response = check_MobileNumber(str(mobileNumber))
        if Response:
            Message = "Mobile number must be 10 digit"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data

    except:
        data = {
            "Message ": "Error In Validation",
            "data ": request.data
        }
        return data


def MobileOtpVerificationValidation(request):
    try:
        email = request.data.get("email")
        Response = parameter_Validation_Checker(
            email, "email", request)
        if Response:
            return Response

        Response = check_Email(str(email))
        if Response:
            Message = "Invalid Email Id. Example : vishalpwaman@gmail.com"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data

        mobileNumber = request.data.get("mobileNumber")
        Response = parameter_Validation_Checker(
            mobileNumber, "mobile Number", request)
        if Response:
            return Response

        Response = check_MobileNumber(str(mobileNumber))
        if Response:
            Message = "Mobile number must be 10 digit"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data

        Otp = request.data.get("Otp")
        Response = parameter_Validation_Checker(
            mobileNumber, "mobile Number", request)
        if Response:
            return Response

        Response = Otp_Validation_Checker(str(Otp), request)
        if Response:
            Message = "Otp number must be 6 digit"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data
        return False
    except:
        data = {
            "Message ": "Internal Error In Validation",
            "data ": request.data
        }
        return data


def Token_Validation(request):
    try:
        token = request.data.get("token")
        Response = parameter_Validation_Checker(
            token, "token", request)
        if Response:
            return Response
    except:
        data = {
            "Message ": "Internal Error In Validation",
            "data ": request.data
        }
        return data


def ResetPassword_Validation(request):
    try:
        email = request.data.get("email")
        Response = parameter_Validation_Checker(
            email, "email", request)
        if Response:
            return Response

        Response = check_Email(str(email))
        if Response:
            Message = "Invalid Email Id. Example : vishalpwaman@gmail.com"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data

        password = request.data.get("password")
        Response = parameter_Validation_Checker(
            password, "password", request)
        if Response:
            return Response

        confirmPassword = request.data.get("confirmPassword")
        Response = parameter_Validation_Checker(
            confirmPassword, "confirmPassword", request)
        if Response:
            return Response
    except:
        data = {
            "Message ": "Internal Error In Validation",
            "data ": request.data
        }
        return data


def ResetPasswordVerification_Validation(request):
    try:
        email = request.data.get("email")
        Response = parameter_Validation_Checker(
            email, "email", request)
        if Response:
            return Response

        Response = check_Email(str(email))
        if Response:
            Message = "Invalid Email Id. Example : vishalpwaman@gmail.com"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data
    except:
        data = {
            "Message ": "Internal Error In Validation",
            "data ": request.data
        }
        return data


def DecodeTokenValidation_Validation(request):
    try:
        token = request.data.get("token")
        Response = parameter_Validation_Checker(
            token, "token", request)
        if Response:
            return Response
    except:
        data = {
            "Message ": "Internal Error In Validation",
            "data ": request.data
        }
        return data


def EncodeTokenValidation_Validation(request):
    try:
        user_id = request.data.get("user_id")
        Response = parameter_Validation_Checker(
            user_id, "user_id", request)
        if Response:
            return Response

        email = request.data.get("email")
        Response = parameter_Validation_Checker(
            email, "email", request)
        if Response:
            return Response

        Response = check_Email(str(email))
        if Response:
            Message = "Invalid Email Id. Example : vishalpwaman@gmail.com"
            data = {
                "Message": Message,
                "data": request.data
            }
            return data
        return False
    except:
        data = {
            "Message ": "Internal Error In Validation",
            "data ": request.data
        }
        return data
