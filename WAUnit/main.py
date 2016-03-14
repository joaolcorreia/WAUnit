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



