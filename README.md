# MIN_LINUX
这是用Python写的一个小型Linux，主要还是代码的练习和知识巩固，后面有时间就进行升级，
原理：开启2个进程，一个作为Linux，另一个作为cmd终端，Linux进程会监听另一个，cmd输入命令时会发送到Linux，由Linux调用系统命令。
目录结构使用树的原理，用列表来完成
使用方式：先开启linux_system文件,在开启teminal文件,运行teminal时，会要求输入用户名和密码，默认为root和123456，然后方可使用
命令：cd,mkdir,touch,pwd,ls,clear,rm,exit,help.
