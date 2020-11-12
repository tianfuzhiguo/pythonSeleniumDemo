import pexpect

def setDate():
    ip='192.168.50.45'
    password='n-1'
    cmd='date\n'
    ret = -1
    ssh = pexpect.spawnu('ssh root@%s "%s"' % (ip, '2016-01-01 \n'))
    try:
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)
        if i == 0 :
            ssh.sendline(password)
        elif i == 1:
            ssh.sendline('yes\n')
            ssh.expect('password: ')
            ssh.sendline(password)
        ssh.sendline(cmd)
        ssh.sendline('2016-01-01 \n')
        r = ssh.read()

        ret = 0
    except pexpect.EOF:
        ssh.close()
        ret = -1
    except pexpect.TIMEOUT:
        ssh.close()
        ret = -2
    return ret