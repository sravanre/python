#paramiko helps in communicating with ssh2 servers.

import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('10.1.0.65',username='automation',password='auto123')


stdin,stdout,stderr=ssh.exec_command("uname -r")

print ('OUTPUT')
for line in stdout:
	print (line)

print ('ERROR')
for line in stderr:
	print(line)

ssh.close()
"""
ftp = ssh.open_sftp()
ftp.put('sample.txt', 'sampleremote.txt') # copy to remote system
# use ftp.get to copy from remote system
ftp.close()
ssh.close()
"""
