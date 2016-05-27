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


import unittest
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy,ProxyType
from selenium.webdriver.common.keys import Keys

import time
import shelve

import ConfigParser
config = ConfigParser.RawConfigParser()

# Insert the path to your configuration file
config.read('waunit.cfg')


from WAUnit import *


class WAUnitDemo(unittest.TestCase):

    def setUp(self):
        myProxy = config.get('Proxy', 'host')+':'+config.get('Proxy', 'port')

        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': myProxy,
            'ftpProxy': myProxy,
            'sslProxy': myProxy,
            'noProxy': '' # set this value as desired
            })

        self.driver = webdriver.Firefox(proxy=proxy)
        self.driver.set_window_size(920, 860)
        #self.driver = WebDriver('firefox', proxy=proxy, reuse_browser=True)

    def test1_google_store_buy_now_click(self):
        """
        The test external link verifies if external tracking is working
        """
        utid = '001'

        driver = self.driver
        driver.get("https://store.google.com/product/nexus_6p?utid="+utid)

        # Click Button Buy From $499
        driver.find_element_by_class_name('transaction').click()
        time.sleep(2)

        driver.close()

        d = shelve.open(config.get('Proxy', 'hitsdb'))
        proxy_utid = d[utid]
        d.close()

        spec_utid = {}
        spec_utid = { 'hitType' : 'event',
                      'eventAction' : 'Buy Now',
                      'eventCategory' : 'Checkout Funnel',
                      'eventLabel' : 'nexus_6p'}

        verification = verify_spec(spec_utid, proxy_utid)

        self.assertNotIn('False',verification)



    def test2_google_store_2add_to_cart(self):
        """
        The test external link verifies if external tracking is working
        """
        utid = '002'

        driver = self.driver
        driver.get("https://store.google.com/product/nexus_6p?utid="+utid)

        # Click Button Buy From $499
        driver.find_element_by_class_name('transaction').click()

        # Select the 32GB
        driver.find_element_by_xpath("//button[@data-variation-id='32']").click()
        time.sleep(2)

        # Scroll all the way down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Add to Cart
        driver.find_element_by_xpath("//button[@data-backend-docid='_nexus_6p_aluminium_32gb_lte']").click()
        time.sleep(2)

        d = shelve.open(config.get('Proxy', 'hitsdb'))
        proxy_utid = d[utid]
        d.close()

        spec_utid = {}
        spec_utid = { 'hitType' : 'event',
                      'eventAction' : 'Add to Cart',
                      'eventCategory' : 'Checkout Funnel',
                      'eventLabel' : 'nexus_6p'}
        verification = verify_spec(spec_utid, proxy_utid)

        self.assertNotIn('False',verification)


    def tearDown(self):
        driver = self.driver
        driver.quit()


suite = unittest.TestLoader().loadTestsFromTestCase(WAUnitDemo)
unittest.TextTestRunner(verbosity=2).run(suite)




