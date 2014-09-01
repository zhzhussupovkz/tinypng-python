#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# The MIT License (MIT)

# Copyright (c) 2014 Zhassulan Zhussupov

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from tinypng_api import TinypngApi
from optparse import OptionParser


usage = "%prog [options]\n\n"
usage += "Command-line tool for downloading shrink images by from https://www.tinypng.com\n"
usage += "Copyright (c) 2014 Zhussupov Zhassulan zhzhussupovkz@gmail.com\n"
usage += "While using this program, get API key from https://www.tinypng.com"
option_parser = OptionParser(usage=usage, version="%prog 1.0")
option_parser.add_option("-i", "--input", help = "input file", default = "python.png")
option_parser.add_option("-o", "--output", help = "output file", default = 'python-output.png')
(options, args) = option_parser.parse_args()

my_api_key = 'Your API key'
api = TinypngApi(my_api_key)
api.shrink(input = options.input, output = options.output)
