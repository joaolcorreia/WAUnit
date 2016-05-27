# Copyright (c) 2016 Joao Correia. All rights reserved.
#
# This program is licensed to you under the Apache License Version 2.0,
# and you may not use this file except in compliance with the Apache License Version 2.0.
# You may obtain a copy of the Apache License Version 2.0 at http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the Apache License Version 2.0 is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Apache License Version 2.0 for the specific language governing permissions and limitations there under.
#
# Version:     0.1.0
# URL:         -
#
# Authors:     Joao Correia <joao.correia@gmail.com> https://joaocorreia.io
# Copyright:   Copyright (c) 2016 Joao Correia
# License:     Apache License Version 2.0

#!/usr/bin/env python

"""
    mitmproxy Proxy
"""

from WAUnit import *

from mitmproxy import flow
from mitmproxy.proxy import ProxyServer, ProxyConfig
import shelve
import ConfigParser

#config = ConfigParser.RawConfigParser()
#config.read('wunit.cfg')

import os.path

# Save Parsed Files
import argparse
parser = argparse.ArgumentParser(description='Run the Web Analytics Unit Proxy')
parser.add_argument('--config', dest='config_file',
                       help='specified the configuration file')
args = parser.parse_args()

global config
config = ConfigParser.RawConfigParser()
config.read(args.config_file)

def MainProxy():
    """
    The Proxy called by waunitproxy
    """
    # Configuration file
    if(os.path.isfile(args.config_file)):
    #use ~/.mitmproxy/mitmproxy-ca.pem as default CA file.
        proxyconfig = ProxyConfig(port = config.getint('Proxy', 'port'),
        cadir = "~/.mitmproxy/")
        state = flow.State()
        server = ProxyServer(proxyconfig)
        try:
            m = GoogleAnalyticsUniversal(server, state)
            m.run()
        except (KeyboardInterrupt):
            pass
    else:
        print "Invalid config file. Use --config to specify the configuration file (e.g. --config waunit.cfg)"


class GoogleAnalyticsUniversal(flow.FlowMaster):


    def run(self):
        try:
            print "Running..."
            flow.FlowMaster.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_request(self, f):
        f = flow.FlowMaster.handle_request(self, f)
        if f:
            f.reply()
        return f

    def handle_response(self, f):
        f = flow.FlowMaster.handle_response(self, f)
        if f:
            f.reply()
        if "collect" in f.request.path:
            d = shelve.open(config.get('Proxy', 'hitsdb'))
            url = "%s://%s%s" % (f.request.scheme, f.request.host, f.request.path)
            ut = parse_google_analytics_url(url)
            print '\n'
            print ut
            d[to_string(ut.keys())] = ut[to_string(ut.keys())]
            d.close()
        return f



