def to_string(list):
    """
    Convert list to string. If empty it is set to (not set)
    """
    if list:
      return ''.join(list)
    else:
      return '(not set)'



def verify_spec(spec_utid, proxy_utid):
  """
  For a specific unit test id (utid) compares the spec with the proxy
  """
  results=''
  for key in spec_utid:
    results += '%s: spec=%s, proxy=%s (%s) *** ' % (key,spec_utid[key],proxy_utid[key],(spec_utid.get(key)==proxy_utid.get(key)))
  return results

