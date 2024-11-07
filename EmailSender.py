"""Converting Script to a module
We convert this code into a module that we can reuse.
For that we can either convert it manually or use pycharms refactor "extract method" feature
"""
import smtplib, ssl ## 1. Import smtplib and ssl standard modules
import os  ## 11. We import os standard module to make an environment variable

## 10. We convert this code into a function, but we need to add parameters manually.
def send_email(subject, body):
    ## 2. We then save the username and password in variables
    username = "alifseen@gmail.com"
    password = os.getenv("EMAILSENDERPASS")  ## 12. It is not safe to store sensitive information in a script, best way to do it is to store it in an environment variable on your computer and then simply call it here by making sure the name is same. in this case, "EMAILSENDERPASS"
    ## 3. We save email service providers smtp server address and port
    emailHost = "smtp.gmail.com"
    hostPort = 465
    ## 4. We create an ssl certificate
    sslContext = ssl.create_default_context()
    ## 5. Specify receiver
    receiver = "alifseen@gmail.com"
    ## 6. specify message
    message = "Subject: " + subject + "\n" + body
    message = message.encode("utf-8")  ## added this to ensure bytes object are processed properly when replacing str object
    ## 7. Using context manager, we send the email:
    with smtplib.SMTP_SSL(emailHost, hostPort, context=sslContext) as server:
        ## 8. We add login information to login method
        server.login(username, password)

        ## 9. Create and send an email
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    print("You are running this script on itself")

