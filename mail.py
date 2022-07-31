import smtplib
ser = smtplib.SMTP('smtp.gmail.com',587)
ser.starttls()
frm ='quitclaim007@gmail.com'
ser.login(frm,'arunaravinth')
to = ['aravinthkarthi5@gmail.com']
bdy = '\r\n'.join(['To: %s'%'aravintharasai5@gmail.com','From :%s'%'aravinthkarthi5@gmail.com','Subject:%s'%'Testing fot otp','',''' name : ;otp'''])
ser.sendmail(frm,to,bdy)
