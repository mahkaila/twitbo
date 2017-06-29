#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

MAIN_PAGE_HTML = """\
<html>
  <head>
    <title>FuzzBeed</title>
  </head>
  <body>
    <h3>FuzzBeed</h3>
    <p><a href="https://www.youtube.com/watch?v=9pzm1lQX0qU&t=2s">Clicko 4 Micko</a></p>
  </body>
</html>
"""

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
