from fabric.api import *
env.use_ssh_config=False

def hello():
    print 'hello'
    
def add_sudo_user(nuser=None,keyfile=None):
    if nuser is not None and keyfile is not None:
        env["nuser"] = nuser
        env["keyfile"] = keyfile
    if nuser is None and env.get("nuser") is None:
        env["nuser"] = prompt("What user do you want to add? ")
    if keyfile is None and env.get("keyfile") is None:
        env["keyfile"] = prompt("What key file do you want to add for this user? ")
    check_user_exists(env["nuser"],env["keyfile"])
    
def check_user_exists(user,keyfile):
    print user
    print keyfile
    with settings(warn_only=True):
        if run('id %s' %user).failed:
            print 'user does not exist'
            print 'creating user'
            sudo('/usr/sbin/useradd %s -G wheel' %user)
            sudo ('mkdir /home/%s/.ssh'%user)
            put (keyfile,'/home/%s/.ssh/authorized_keys'%user,use_sudo=True)
            sudo ('chown -R %s:%s /home/%s/.ssh && chmod -R 400 /home/%s/.ssh'%(user,user,user,user))
