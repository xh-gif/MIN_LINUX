
from multiprocessing.connection import Client


class UserUI(object):

    def __init__(self):

        self.address = ('localhost', 7000)


        with Client(self.address, authkey=b'secret password') as conn:
            conn.send('initial')  # register format

            a = conn.recv()
            print(a)
            self.location = a



    def start(self):
        print('************************************************************')
        print('*****                   terminal                      ******')
        print('*****                                                 ******')
        print('*****          Welcome to  the min_liunx              ******')
        print('*****               author is xiaohu                  ******')
        print('*****                      v1.0                       ******')
        print('************************************************************')

    def command(self, com_list):

        coms = com_list.split()

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


        elif com in ('touch', 'cd', 'ls', 'mkdir',  'rm', 'pwd'):

            with Client(self.address, authkey=b'secret password') as conn:

                conn.send(com_list)

                result = conn.recv()
                if result == 'success':
                    pass
                else:
                    print(result)
            with Client(self.address, authkey=b'secret password') as conn:
                conn.send('initial')  # register format

                self.location = conn.recv()
                # self.command_line()


        else:
            print('-bash:', com, ': command not found')

    def command_line(self):

        print('\033[0m[root@localhost \033[0m', self.location, '\033[0m]$\033[0m', end=' ')


def main():

    print("user is 'root',password is '123456'")

    user = 'root'
    password = '123456'
    while True:
        use = input('user       : ')
        pwd = input('password   : ')
        if use == user and pwd == password:
            print('--------login success-------')
            break
    ui = UserUI()
    ui.start()
    while True:
        ui.command_line()

        user_input = input()

        ui.command(user_input)


if __name__ == '__main__':
    main()

