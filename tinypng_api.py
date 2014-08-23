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

import urllib
import urllib2
import json
import base64
import os

class TinypngApi:

	def __init__(self, api_key):
		self.api_key = api_key
		self.api_url = 'https://api.tinypng.com/shrink'

	def shrink(self, input = 'python.png', output = 'python-output.png'):
		base64str = base64.encodestring('%s:%s' % ('api', self.api_key)).replace('\n', '')
		data = open(input, "rb")
		length = os.path.getsize(input)
		url = self.api_url
		req = urllib2.Request(url, data)
		req.add_header('Authorization', "Basic %s" % base64str)
		req.add_header('Host', 'api.tinypng.com')
		req.add_header('Content-Length', '%d' % length)
		req.add_header('Content-Type', 'image/png')
		resp = urllib2.urlopen(req)
		page = json.loads(resp.read())
		try:
			output_url = page.get('output').get('url')
			resp = urllib2.urlopen(output_url)
			f = open(output, "wb")
			f.write(resp.read())
			f.close()
			print "Image %s shrink: OK" % input
			print "Input image size: %s" % page.get('input').get('size')
			print "Output image size: %s" % page.get('output').get('size')
		except:
			print "Image %s shrink: NOT OK" % input