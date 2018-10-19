# Main module for the bot. Run this to start.

import cfg
import socket
import api
import commands
import point_db
import command_db
import chat_db

from time import sleep, time
import threading
import signal
import sys


def chat(sock, msg):
    '''Sends a chat message through socket.'''

    sock.send(f'PRIVMSG {cfg.CHAN} :{msg}\r\n'.encode('utf-8'))


def ban(sock, user):
    '''Bans the specified user from chat.'''

    chat(sock, f'.ban {user}')


def timeout(sock, user, secs=600):
    '''Time out a user for set period of time.'''

    chat(sock, f'.timeout {user} {secs}')


class UpdatePoints(threading.Thread):
    '''Update viewer points every minute.'''

    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def run(self):
        while not self.event.wait(60):
            point_db.update_viewers(api.get_viewers())
            point_db.clean_challenges()


def main():
    s = socket.socket()
    s.settimeout(0.5)
    s.connect((cfg.HOST,cfg.PORT))
    s.send(f'PASS {cfg.PASS}\r\n'.encode('utf-8'))
    s.send(f'NICK {cfg.NICK}\r\n'.encode('utf-8'))
    s.send(f'JOIN {cfg.CHAN}\r\n'.encode('utf-8'))

    pts = UpdatePoints()
    pts.daemon = True
    pts.start()

    def signal_handler(signal, frame):
        pts.event.set()
        close_dbs()
        print('\nkilling bot')
        s.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            response = s.recv(1024).decode('utf-8')
        except socket.timeout:
            continue
        if response == 'PING :tmi.twitch.tv\r\n':
            s.send('PONG :tmi.twitch.tv\r\n'.encode('utf-8'))
        else:
            print(response, end='')
            commands.handle_command(s, response)


def close_dbs():
    command_db.db.close()
    point_db.db.close()
    chat_db.db.close()

if __name__ ==  '__main__':
    main()
