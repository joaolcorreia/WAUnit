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

import urlparse
from waunit_utils import *

def parse_google_analytics_url(url):
    """
    Parse Google Analytics URL
    """
    unit_test_data={}
    parsed = urlparse.urlparse(url)
    queryparams = urlparse.parse_qs(parsed.query)
    cacheBuster = to_string(queryparams.get('z'))       # Cache buster
    hitType = to_string(queryparams.get('t'))         # Pageview or event
    pageTitle = to_string(queryparams.get('dt'))        # pageTitle
    pageUrl = to_string(queryparams.get('dl'))          # Full URL
    propertyId = to_string(queryparams.get('tid'))      # UA-XXXXXX-X
    eventLabel = to_string(queryparams.get('el'))       # Event Label
    eventAction = to_string(queryparams.get('ea'))      # Event Action
    eventCategory = to_string(queryparams.get('ec'))    # Event Category

    # To uniquely identify each test we add a query param utid=
    # and read it from the document location.
    parsed = urlparse.urlparse(pageUrl)
    queryparams = urlparse.parse_qs(parsed.query)
    # Unit Test ID
    utid = to_string(queryparams.get('utid'))
    unit_test_data[utid] = {'hitType': hitType,
                    'pageTitle': pageTitle,
                    'pageUrl' : pageUrl,
                    'eventCategory' : eventCategory,
                    'eventAction' : eventAction,
                    'eventLabel' : eventLabel,
                    'propertyId':propertyId
                    }
    return unit_test_data



