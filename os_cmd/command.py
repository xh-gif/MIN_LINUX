from os_cmd.method_dir_file import *
from os_cmd.superblock import SuperBlock
class filesys(object):
    def __init__(self):
        self.cmds = {    'initial':self.cur_dir,
                         'mkdir':self.mkdir,
                         'ls':self.ls,
                         'pwd':self.pwd,
                         'cd':self.cd,
                         'clear':self.clear,
                         'touch':self.touch,
                         'rm':self.rm}
        self.pwd_index = 0
        self.pwddir = ['/',[]]
        self.dir0 = ['/',['bin'],['etc'],['lib'],['root'],['home'],['sys'],['usr'],
                     ['sbin'],['boot'],['mnt'],['proc'],['srv'],['var'],['dev']]
        print('difhuuifads')
        self.Superblock = SuperBlock
        
    def in_com(self,msg):
        self.a(msg)
        self.disptch()

    def out_com(self):
        result = self.result
        self.result = '\033[0m\033[0m'
        return result

    def cur_dir(self):
        i = self.pwd_index
        s = []
        cc(self.pwddir, i, s)  # 所在路径的目录名按顺序转换为一个列表
        self.result = s[-1]
        self.result = '\033[0m{}\033[0m'.format(self.result)

    def a(self,msg):
        self.msg_list = msg.split()
        # print(self.msg_list)
        self.command = self.msg_list[0]
        if len(self.msg_list) > 1:
            self.can = self.msg_list[1]
        # print('can:', self.can)

    def disptch(self):
        co = self.cmds.get(self.command)
        if self.command in ('rm','mkdir','touch','cd'):
            if len(self.msg_list) < 2:
                self.result = "'help' can see how to use"
            else:
                co()
        else:
            co()

    def mkdir(self):
        a = self.pwd_index
        b=bb(self.dir0, a, self.pwddir[1], self.can,1)
        print(b)
        print(self.dir0)
        self.result = 'success'
        self.result = '\033[0m{}\033[0m'.format(self.result)

    def ls(self):
        a = self.pwd_index
        a1 = self.dir0
        a2 = self.pwddir
        b = aa(a1, a, a2[1])
        b1 = []
        for i in b:
            b1.append(i)
        k = hh(b1)

        self.result = k
        # k = '\033[0m{}\033[0m'.format(k)

    def pwd(self):
        a = []
        b = self.pwd_index
        c = self.pwddir
        cc(c,b,a)
        print(a)
        d = '/'.join(a)
        if d == '/':
            self.result = d
            self.result = '\033[0m{}\033[0m'.format(self.result)
        else:
            d = d[1:]
            self.result = d
            self.result = '\033[0m{}\033[0m'.format(self.result)


    def cd(self):
        if self.can == '/':
            self.pwddir = ['/',[]]
            self.pwd_index = 0
            self.result = 'success'
            self.result = '\033[0m{}\033[0m'.format(self.result)
        elif self.can == '..':
            i = self.pwd_index
            gg(i, self.pwddir)
            self.pwd_index -= 1
            self.result = 'success'
            self.result = '\033[0m{}\033[0m'.format(self.result)
        elif self.can == '.':
            self.result = 'success'
            self.result = '\033[0m{}\033[0m'.format(self.result)
        else:
            a = self.f_t_dir(self.can)
            c = self.pwd_index
            print(a)
            print(self.can)
            print(self.pwd_index)
            if a:
                if self.can[0] == '/':
                    b = self.can.split('/')
                    b.pop(0)
                    c = ['/',[]]
                    for i in range(len(b)):
                        ff(i, c, b[i])
                    print(c)
                    self.pwddir = c
                    self.pwd_index = len(b)
                else:
                    b = self.can.split('/')
                    for i in b:
                        ff(c, self.pwddir, i)
                        self.pwd_index += 1
                self.result = 'succuss'
                self.result = '\033[0m{}\033[0m'.format(self.result)
            else:
                self.result = "'{}' is not directory".format(self.can)
                self.result = '\033[0m{}\033[0m'.format(self.result)



    def touch(self):
        a = self.pwd_index
        b = bb(self.dir0, a, self.pwddir[1], self.can, 0)

        self.result = 'success'
        self.result = '\033[0m{}\033[0m'.format(self.result)
    def clear(self):
        self.result = '\n' * 15

    def rm(self):


        if self.can == '/':
            # pass
            self.result ="not can rm '/'"
        else:
            a = self.can.split('/')
            # if a[0] == '':
            #     a[0] = '/'
            # c = dd(self.pwddir,len(a)-1,a)
            # print(c)
            b = self.f_t_dir(self.can)
            print(b)
            if b:
                if self.can[0] == '/':
                    if len(a) >= self.pwd_index:
                        a[0] = '/'
                        ii(self.dir0,len(a)-1,a)
                        self.result = 'success'
                    else:
                        self.result = 'error'
                        return
                else:
                    if a[-1] == '':
                        a.pop(-1)
                    v = []
                    h = self.pwd_index
                    c = self.pwddir
                    cc(c, h, v)
                    v.extend(a)
                    ii(self.dir0, len(v)-1, v)
                    self.result = 'rm success'
            else:
                # s = self.dir0
                self.result = "'{}' is not directory".format(self.can)
        self.result = '\033[0m{}\033[0m'.format(self.result)



    def f_t_dir(self,a):
        if a[0] == '/':
            a = a.split('/')
            a[0] = '/'
            s = self.dir0
            b = dd(s,len(a)-1,a)
            return b
        else:
            i = self.pwd_index
            j = self.pwd_index
            s = self.dir0
            sf = self.pwddir
            v = ee(s,j,sf[1]) #获取当前目录下的所有子目录及文件
            s = []

            cc(sf,i,s) #所在路径的目录名按顺序转换为一个列表
            print('vvvvv---',v)
            if s[-1] == '/':
                a = '/' + a
            else:
                a = s[-1]+'/'+a

            a = a.split('/')
            if a[0] == '':
                a[0] = '/'
            print(a)
            b = dd(v,len(a)-1,a)
            return b


# a = filesys()
# a.in_com('mkdir aaa')
# a.in_com('mkdir bbb')
# a.in_com('mkdir ccc')
# print(a.dir0)
# print(a.pwddir)
# a.in_com('cd aaa')
# print(a.out_com())
# a.in_com('pwd')
# print(a.out_com())
# b = 'ls'
# a.in_com(b)
# print(a.out_com())
# b = 'cd bin'
# a.in_com(b)
# print(a.out_com())
# while True:
#     b = input()
#     a.in_com(b)
#     print(a.out_com())