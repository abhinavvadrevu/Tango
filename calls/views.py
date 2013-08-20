# Create your views here.

from django.http import HttpResponse
from twilio2 import sendit
import smtplib  

def index(request):    
    fromaddr = 'leadtheway.abhinav@gmail.com'  
    toaddrs  = 'vadrevus@gmail.com'  
    msg = """
Hey dad,
    I realized that if I don't have internet, and you don't have magic jack plugged in, then I can't call you.
    So I created this app I'm calling Tango (because it uses Twilio and Django lol).
    All I do is call a number from my phone.  It then sends you this email, and texts me back to confirm it worked.
    So if you are getting this message, you should call me through magic jack if possible!
    Although if this is one of the first few emails, I'm probs just testing it :P
    """
    # Credentials (if needed)  
    username = 'leadtheway.abhinav'  
    password = ''  
    # The actual mail send  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username,password)  
    server.sendmail(fromaddr, toaddrs, msg)  
    server.quit()  
    sendit.send()
    return HttpResponse("You sent the email!")