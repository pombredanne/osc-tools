#!/usr/bin/env python

from optparse import OptionParser
import sys
import json
from OSC import OSCMessage, OSCClient

parser = OptionParser()

parser.add_option("-H", "--host", dest="host", default='0.0.0.0')
parser.add_option("-p", "--port", dest="port", default=8000)
parser.add_option("-t", "--target", dest="target", default='/1/xy')
parser.add_option("-m", "--message", dest="message", default='')

(options, args) = parser.parse_args()

client = OSCClient()
client.connect((options.host, options.port))

msg = OSCMessage(options.target)
if options.message:
    msg += json.loads(options.message)

if len(sys.argv) < 2:
    print "You need some arguments, try -h"
else:
    client.send(msg)
