# -*- coding: utf-8 -*-

"""
    pugdebug - a standalone PHP debugger
    =========================
    copyright: (c) 2015 Robert Basic
    license: GNU GPL v3, see LICENSE for more details
"""

__author__="robertbasic"

import socket

class PugdebugDebugger():

    sock = None
    address = None

    is_running = False

    def __init__(self):
        pass

    def start_debug(self):
        if self.is_running:
            print('already running')
            return

        self.is_running = True

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.settimeout(None)

        try:
            server.bind(('', 9000))
            self.init_connection(server)
        except OSError:
            self.is_running = False
            print("Socket bind failed")
        finally:
            server.close()

    def stop_debug(self):
        print('stop')

    def step_over(self):
        print('over')

    def step_in(self):
        print('in')

    def step_out(self):
        print('out')

    def init_connection(self, server):
        server.listen(5)

        print('Waiting for connection ...')

        self.sock, self.address = server.accept()
        self.sock.settimeout(None)
        self.read_init_message()

    def read_init_message(self):
        print(self.sock.recv(1024))
