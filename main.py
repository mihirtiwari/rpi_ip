import subprocess, smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('mtiw999@gmail.com', 'Doam&3oP!')

ip_0 = subprocess.check_output('ipconfig getifaddr en0', shell=True)

if ip_0:
    server.sendmail('mtiw999@gmail.com', 'mtiw999@gmail.com', ip_0)
else:
    print 'Not connected to internet'
server.quit()
