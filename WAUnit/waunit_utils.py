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

