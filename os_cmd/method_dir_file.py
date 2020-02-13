
def aa(s,i,sf):
    if i > 0:
        i -= 1
        for j in s:
            if j[0] == sf[0]:
                return aa(j,i,sf[1])
    else:
        b = []
        a = s[1:]
        for j in a:
            # if isinstance(j,list):
            #     # j[0] = '\033[0;34m{}\033[0;34m'.format(j[0])
            #     b.append(j[0])
            # else:
                # j = '\033[0m{}\033[0m'.format(j)
            b.append(j)
        # d = '            '
        # c = d.join(b)
        return b


def bb(s,i,sf,vvv,a): #在当前目录sf下创建目录vvv，s为总目录结构，这样s就会改变，sf不会变
    if i > 0:
        i -= 1
        for j in s:
            if isinstance(j,list):
                if j[0] == sf[0]:
                    return bb(j,i,sf[1],vvv,a)
    else:
        if a:
            s.append([vvv])
        else:
            s.append(vvv)
        return s


def cc(s,i,v):
    if i > 0:
        v.append(s[0])
        s = cc(s[1],i-1,v)
        return v
    else:
        v.append(s[0])
        return v


def dd(s, i, sf):
    if i > 0:
        for j in s:
            if isinstance(j,list):
                if j[0] == sf[-i]:
                    i -= 1
                    return dd(j,i,sf)
        else:
            return False
    else:
        return True


def ee(s,i,sf): #获取sf目录下的所有子目录及文件
    if i > 0:
        i -= 1
        for j in s:
            if j[0] == sf[0]:
                return ee(j,i,sf[1])
    else:
        b = []
        a = s
        for j in a:
            b.append(j)
        return b


def ff(i,sf,vvv): #添加名为vvv的目录到当前目录，即切换目录，vvv为字符串
    if i > 0:
        i -= 1
        return ff(i,sf[1],vvv)
    else:
        sf[1] = [vvv,[]]
        return True


def gg(i,sf): #删除当前目录的最后一级，即切换目录到上一级
    if i > 0:
        i -= 1
        return gg(i,sf[1])
    else:
        sf[:] = []
        return True


def hh(b):
    k = ''
    # print(b)
    l = '              '
    for i in b:
        if isinstance(i, list):
            a = '\033[0;34m{}\033[0;34m'.format(i[0])
            k = k + l + a
        else:
            i = '\033[0m{}\033[0m'.format(i)
            k = k + l + i
    k = k[len(l):]
    return k


def ii(s,i,sf):
    # i += 1
    if i > 1:

        for j in s:
            if isinstance(j,list):

                if j[0] == sf[-i]:
                    i -= 1

                    # for k in j:
                    #     if isinstance(k,list):
                    return ii(j, i, sf)
    else:

        for j in range(len(s)):
            if isinstance(s[j],list):
                if s[j][0] == sf[-i]:

                    s.pop(j)
                    return

            else:
                if s[j] == sf[-i]:
                    s.pop(j)
                    return