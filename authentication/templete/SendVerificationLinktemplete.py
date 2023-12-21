from email.mime.text import MIMEText
from rest_framework.response import Response


class SendVerificationLinkHtmlBody:

    @staticmethod
    def GenerateVerificationLinkHtmlBody(token):
        try:
            print("Enter in generate Verification link class")
            html = """
            <html>
            <head>
                <!-- <script> -->

                <!-- </script> -->
                <style>
                .container {
                    height: 100%;
                    width: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }

                .subContainer {
                    height: 70%;
                    width: 45%;
                }

                .google {
                    font-size: 26px;
                    height: 15%;
                    width: 100%;
                    display: flex;
                    align-items: center;
                    font-family: Helvetica;
                    font-weight: 400;
                }

                .body {
                    height: 85%;
                    width: 605px;
                    font-family: Helvetica;
                    font-size: 13px;
                    box-shadow: none;
                    border-radius: 0 0 3px 3px;
                }

                .header {
                    background-color: #4184f3;
                    height: 30%;
                    width: 99.5%;
                    margin-left: 0.25%;
                    border-radius: 3px 3px 0 0;
                }

                .h2 {
                    height: 100%;
                    font-size: 24px;
                    color: #ffffff;
                    font-weight: 400;
                    font-family: Helvetica;
                    margin: 0 0 0 40px;
                    display: flex;
                    align-items: center;
                }
                .subBody {
                    background-color: #fafafa;
                    height: 289px;
                    min-width: 332px;
                    max-width: 753px;
                    border: 1px solid #f0f0f0;
                    border-bottom: 1px solid #c0c0c0;
                }
                .innersubBody {
                    width: 86%;
                    height: 83.5%;
                    margin: 4% 6%;
                }
                .button {
                    font-size: 20px;
                    margin: 0 40%;
                }
                .btn {
                    width: 200px;
                }
                </style>
            </head>
            <body>
                <div class="container">
                <div class="subContainer">
                    <div class="google">
                    <!-- <span style="color: #4285f4">G</span>
                                        <span style="color: #db4437">o</span>
                                        <span style="color: #f4b400">o</span>
                                        <span style="color: #4285f4">g</span>
                                        <span style="color: #0f9d58">l</span>
                                        <span style="color: #db4437">e</span> -->
                    </div>
                    <div class="body">
                    <div class="header" style="height: 120px">
                        <div class="h2" style="height: 120px; padding: 40px 0">
                        V Tech Verification Link
                        </div>
                    </div>
                    <div class="subBody">
                        <div class="innersubBody">
                        <div>
                            This verification link was sent to verify your email account
                        </div>
                        <br />
                        <div class="button">
                            <a class="btn btn-primary" href="http://localhost:3000/AccountVerificationByEmail/""" + str(token)+"""">Click Here</a>
                        </div>
                        <br />
                        <div>Don’t know why you received this?</div>
                        <br />
                        <div>
                            Please confirm that you want to use this as your V Tech account email address. Once it's done you will be able to access your V tech Account
                        </div>
                        <br />
                        <div>
                            To protect your account, don’t forward this email or give this
                            code to anyone.
                        </div>
                        <br />
                        <div>V Tech Accounts team</div>
                        <br />
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </body>
            </html>
            """
            return html
        except:
            return Response(False)

    @staticmethod
    def SendResetPasswordVerificationLinkOnEmail(token):
        try:
            print("Enter in generate Verification link class")
            html = """
            <html>
            <head>
                <style>
                .container {
                    height: 100%;
                    width: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }

                .subContainer {
                    height: 70%;
                    width: 45%;
                }

                .google {
                    font-size: 26px;
                    height: 15%;
                    width: 100%;
                    display: flex;
                    align-items: center;
                    font-family: Helvetica;
                    font-weight: 400;
                }

                .body {
                    height: 85%;
                    width: 605px;
                    font-family: Helvetica;
                    font-size: 13px;
                    box-shadow: none;
                    border-radius: 0 0 3px 3px;
                }

                .header {
                    background-color: #4184f3;
                    height: 30%;
                    width: 99.5%;
                    margin-left: 0.25%;
                    border-radius: 3px 3px 0 0;
                }

                .h2 {
                    height: 100%;
                    font-size: 24px;
                    color: #ffffff;
                    font-weight: 400;
                    font-family: Helvetica;
                    margin: 0 0 0 40px;
                    display: flex;
                    align-items: center;
                }
                .subBody {
                    background-color: #fafafa;
                    height: 289px;
                    min-width: 332px;
                    max-width: 753px;
                    border: 1px solid #f0f0f0;
                    border-bottom: 1px solid #c0c0c0;
                }
                .innersubBody {
                    width: 86%;
                    height: 83.5%;
                    margin: 4% 6%;
                }
                .button {
                    font-size: 20px;
                    margin: 0 40%;
                }
                .btn {
                    width: 200px;
                }
                </style>
            </head>
            <body>
                <div class="container">
                <div class="subContainer">
                    <div class="google">
                    <!-- <span style="color: #4285f4">G</span>
                                        <span style="color: #db4437">o</span>
                                        <span style="color: #f4b400">o</span>
                                        <span style="color: #4285f4">g</span>
                                        <span style="color: #0f9d58">l</span>
                                        <span style="color: #db4437">e</span> -->
                    </div>
                    <div class="body">
                    <div class="header" style="height: 120px">
                        <div class="h2" style="height: 120px; padding: 40px 0">
                        V Tech Reset password Link
                        </div>
                    </div>
                    <div class="subBody">
                        <div class="innersubBody">
                        <div>
                            This reset password link was sent to verify your email account
                        </div>
                        <br />
                        <div class="button">
                            <a class="btn btn-primary" href="http://localhost:3000/ResetPassword/""" + str(token)+"""">Click Here</a>
                        </div>
                        <br />
                        <div>Don’t know why you received this?</div>
                        <br />
                        <div>
                            Please confirm that you want to use this as your V Tech account email address. Once it's done you will be able to access reset password link
                        </div>
                        <br />
                        <div>
                            To protect your account, don’t forward this email or give this
                            code to anyone.
                        </div>
                        <br />
                        <div>V Tech Accounts team</div>
                        <br />
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </body>
            </html>
            """
            return html
        except:
            return Response(False)
