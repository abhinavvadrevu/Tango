# Create your views here.

from django.http import HttpResponse
from twilio2 import sendit
import smtplib  

def index(request):    
    fromaddr = 'leadtheway.abhinav@gmail.com'  
    toaddrs  = 'avadrevu@twitter.com'  
    msg = 'Hey you should call me through magic jack if possible!'  
    # Credentials (if needed)  
    username = 'leadtheway.abhinav'  
    password = 'SL(0fd>?'  
    # The actual mail send  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username,password)  
    server.sendmail(fromaddr, toaddrs, msg)  
    server.quit()  
    sendit.send()
    return HttpResponse("Hello, world. You're at the poll index.")