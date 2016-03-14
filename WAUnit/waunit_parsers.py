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



