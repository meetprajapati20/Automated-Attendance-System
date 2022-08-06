import smtplib

def sendMail():
    fromaddr = "souhardyasarkar20@gnu.ac.in"
    toaddr = "souhardyasarkar735@gmail.com"
    msg = "msg hai"
    username = "souhardyasarkar20@gnu.ac.in"
    password = "gnu15102020"
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr,toaddr,msg)
    server.quit()
    
sendMail()
