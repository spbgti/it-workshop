#!/usr/bin/env python

""" Stockbrokers API server

Usage:
    stockbrokers.py run (dev|prod|test) [-v] [--bind=<ip>] [--port=<port>]
    stockbrokers.py (-h|--help)

Options:
    -h --help           Display this help message.
    --version           Show server version.
    -v --verbose        Show debug information while working.
    -b --bind=<ip>      IP address for the server to bind to. Defaults to 0.0.0.0.
    -p --port=<port>    Port for the server to listen on. Defaults to 5050.
"""

from docopt import docopt
from workshop.app import create_app


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.4a')
    
    debug = arguments['--verbose']
    host = arguments['--bind'] or '0.0.0.0'
    port = arguments['--port'] or 5050
    if arguments['dev'] is True:
        mode = 'dev'
    elif arguments['test'] is True:
        mode = 'test'
    else:
        mode = 'prod'
    
    # Creating the app with parameters given
    app = create_app(mode)
    app.run(host, port, debug)
