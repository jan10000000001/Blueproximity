# -*- coding: utf-8 -*-
import argparse
import os.path

from xdg import BaseDirectory

from blueproximity import APP_NAME, config, init_logging, run_gui


def cli():
    parser = argparse.ArgumentParser(prog='blueproximity', description='''
        Unlock your computer as soon as a bluetooth-device is in range
    ''')
    parser.add_argument('--gui', help='Start GUI', action='store_true')
    parser.add_argument('-c', '--config', help='Path to configfile', type=str)
    return parser.parse_args()


def main():
    # cli-args
    args = cli()

    # load config
    if args.config:
        config_path = args.config
    else:
        config_path = os.path.join(
            BaseDirectory.save_config_path(APP_NAME), 'config.ini')
    if args.gui:
        run_gui()
    configuration = config.load(config_path, validate=True)
    # initiate logging
    init_logging(configuration)


if __name__ == '__main__':
    main()
