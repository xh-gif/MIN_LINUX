# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()

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
                print('-------------')
                print(msg)
                print(type(msg))
                print('------------')
                fsm.in_com(msg)

                result = fsm.out_com()

                conn.send(result)

print('-----')
if __name__ == '__main__':

    main()