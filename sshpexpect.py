from pexpect import pxssh
import getpass
p = pxssh.pxssh()
p.force_password= True
hostname = raw_input('hostname: ')
username = raw_input('username: ')
password = getpass.getpass('password: ')
p.login(hostname, username, password)
              
p.sendline('ls -l')
p.prompt()
print p.before
   

	
	
