

from multiprocessing import Process
from os_cmd import command
from multiprocessing.connection import Listener, wait
# import threading
# import time


def main():

    fsm = command.filesys()

    address = ('localhost', 7000)

    print('Listening:', address[0])

    while True:

        with Listener(address, authkey=b'secret password') as listener:

            with listener.accept() as conn:

                print('connection accepted from', listener.last_accepted)

                msg = conn.recv()
               
                fsm.in_com(msg)

                result = fsm.out_com()

                conn.send(result)

def pp(a):
    fsm = command.filesys()
    coms = a.split()
    fsm.in_com('initial')  # register format

    a = fsm.out_com()
    global location
    location = a
    try:
        com = coms[0]
    except IndexError:
        return

    if com == 'help':
        print(
            'pwd \n'
            'cd  [name]\n'
            'ls\n'
            'mkdir  [name]\n'
            'touch  [name]\n'
            'rm [name]\n'
            'clear\n'
            'exit\n')

    elif com == 'exit':
        print('[Process completed]')
        exit(0)

    elif com in ('touch', 'cd', 'ls', 'mkdir', 'rm', 'pwd'):
            fsm.in_com(a)
            result = fsm.out_com()
            if result == 'success':
                pass
            else:
                print(result)

    else:
        print('-bash:', com, ': command not found')


def command_line():

    print('\033[0m[root@localhost \033[0m', location, '\033[0m]$\033[0m', end=' ')

def p1(s):
    global k

    while True:
        command_line()
        a = input()
        if a == 'ssh':
            k = 1
            yield a
            # p1.terminate()

        p2 = Process(target=pp, name='p2', args=(a,))
        p2.start()

if __name__ == '__main__':
    k = 0
    location = '/'
    a = p1(1)
    next(a)
    if k == 1:
        p1 = Process(target=main, name='p1')
        p1.start()
    while True:
        next(a)
