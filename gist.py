#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Gistpy. """


import json
import sys
import urllib2
import base64
import subprocess

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--description",
                  dest="description",
                  default="Gist uploaded with gist.py\
https://github.com/aseba/GistPy",
                  help="Description",
                  metavar="DESC")

parser.add_option("-n", "--name",
                  dest="name",
                  help="File Name",
                  default="",
                  metavar="NAME")

parser.add_option("-p", "--private",
                  action='store_false',
                  dest="public",
                  default=True,
                  help="Set Gist as private")

parser.add_option("-o", "--open",
                  action='store_true',
                  dest="open",
                  default=False,
                  help="Open html url using command 'open' when finished")

parser.add_option("-U", "--username",
                  dest="username",
                  default=None,
                  help="Sets username to login at github.com")

parser.add_option("-P", "--password",
                  dest="password",
                  default=None,
                  help="Sets password to login at github.com")

(options, args) = parser.parse_args()

try:
    content = "".join([line for line in sys.stdin])
except:
    print "Something went wrong reading from STDIN"
    sys.exit(1)

if not content.strip():
    print "Content was empty"
    sys.exit(1)

payload = {"description": options.description,
           "public": options.public,
           "files": {options.name: {"content": content}}
           }

url = 'https://api.github.com/gists'

request = urllib2.Request(url)

if options.username and options.password:
    base64string = base64.encodestring(
        '%s:%s' % (options.username, options.password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)

try:
    raw_result = urllib2.urlopen(request, json.dumps(payload))
except urllib2.HTTPError, error:
    print "Something went wrong when talking with github: " % error.read()
    sys.exit(1)

try:
    result = json.loads(raw_result.read())
    if 'html_url' in result:
        if options.open:
            subprocess.call(['open', result['html_url']])
        else:
            print result['html_url']
    else:
        print "Github said: %s" % result

except ValueError, error:
    print "Something went wrong when talking with github: %s" % error.read()
    sys.exit(1)
