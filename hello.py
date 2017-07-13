from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

import mxnet as mx


def main():
    # create a 1-dimensional array with a python list
    a = mx.nd.array([1, 2, 3])

    print(a)

    print('Hello, mxnet!')
    print('Python version: %s' % sys.version)

if __name__ == '__main__':
    main()
