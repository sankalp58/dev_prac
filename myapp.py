#myapp.py

import logging
import mylib


def main():

    logging.basicConfig(filename='myapp.log',level=logging.INFO)
    logging.info('Started')
    mylib.do_some()
    logging.info('Finished')


if __name__ == '__main__':

    main()
