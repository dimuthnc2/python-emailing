import smtplib
fromaddr = 'dimuthu.13@cse.mrt.ac.lk'
toaddrs  = 'dimuththaraka@outlook.com'
msg = "\r\n".join([
  "From: Dimuth Tharaka Menikgama",
  "To: Dimuth <dimuthnc@gmail.com>",
  "Subject:Educational",
  "Signed by: D2S2 Sollutions"
  "from <dimuthu.13@cse.mrt.ac.lk>",
  

""" We would like to invite you to participate in our forthcoming online programming contest:

 Ural Regional School Programming Contest 2015
 Date: Saturday, October 17, 2015 at 13:00 UTC+5
 Duration: 5 hours
 Link: http://acm.timus.ru/contest.aspx?id=304
 Timus Online Judge presents an Internet-version of the Ural Regional School Programming Contest. Runs in the same time with the onsite contest. Problem statements will be in both Russian and English.

 For more details about contest schedule see
http://acm.timus.ru/schedule.aspx


 Timus Online Judge
http://acm.timus.ru"""
  
  ])
try:
    
    username = 'dimuthu.13@cse.mrt.ac.lk'
    password = 'Priyadarshani@143'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)

    server.quit()
    print "Email Delivered Successfully"
except:

    print "Email not Delivered"
    
