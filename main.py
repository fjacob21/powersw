#!/usr/bin/python3

import argparse
from flask import Flask
import os
import threading
import time

application = Flask(__name__)

@application.route('/')
def root():
    return 'Power manager service v1.0'

@application.route('/poweroff')
def poweroff_req():
    threading.Thread(target=poweroff).start()
    return 'poweroff device'

@application.route('/reboot')
def reboot_req():
    threading.Thread(target=reboot).start()
    return 'reboot device'
 
def poweroff():
    time.sleep(1)
    print('Poweroff')
    os.system('poweroff')

def reboot():
    time.sleep(1)
    print('reboot')
    os.system('reboot')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Service to control the device power')
    parser.add_argument('-p', '--port', metavar='port', default='8888', nargs='?',
                        help='The port to listen to')

    args = parser.parse_args()
    application.run(debug=True, host='0.0.0.0', port=args.port)