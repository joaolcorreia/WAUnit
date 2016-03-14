Web Analytics Unit (WAUnit)
----------------------------

WAUnit is a testing framework for Google Analytics (other platforms coming soon).

When you setup custom tracking for a website you have to validate if the hits are correct, HitInspect automates the verification of tracking specifications.

Watch the Youtube video '`WAUnit Overview <https://www.youtube.com/watch?v=sWsPey1qBi0>`_'.

In a nutshell this is how it works:

.. image:: https://cloud.githubusercontent.com/assets/1695738/13732067/df23460a-e936-11e5-8dfe-64c628f59628.png

1. A python unittest using Selenium Webdriver is executed
2. A local proxy captures the Google Analytics hits
3. The unittest compares the specs with the proxy hit log and returns OK/FAIL for each test and detailed information on what doesn’t match.

Requirements
-------------
- Python 2.7
- Selenium
- mitmproxy

Installation
-------------
Install WAUnit using pip. Notice a core requirement is mitmproxy. Be sure to install `SSL certificates <http://mitmproxy.org/doc/certinstall.html>`_ for mitmproxy so the proxy can capture SSL traffic.

.. code::

   python pip install WAUnit

Quickstart
----------
If you are not familiar with Selenium read the `getting started <http://selenium-python.readthedocs.org/getting-started.html>`_ with Selenium Python Bindings. Watch the Youtube video '`Getting Started with WAUnit <https://www.youtube.com/watch?v=sWsPey1qBi0>`_'

1. Create a folder for the project
2. Create a configuration file: wunit.cfg
3. Start the proxy: *waunitproxy –config wunit.cfg*
4. A file named hitdata.db will be created in your home directory
5. Download [sample.py](#) to your project directory
6. Execute the sample with: python sample.py

**wunit.cfg**

.. code::

 [WAUnit]
 Only googleanalyticsuniversal is available right now
 parser = googleanalyticsuniversal

 [Proxy] host = 127.0.0.1
 port = 8080
 hitsdb = hitsdata

Questions? Comments?
--------------------
Drop me a line at `@joaocorreia <http://twitter.com/joaocorreia>`_



