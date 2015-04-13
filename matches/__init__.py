# The MIT License (MIT)
#
# Copyright (c) 2015 Lincoln Clarete
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__version__ = '0.0.1'


def extract_from_pattern(pattern0, data0):

    def scan(pattern, data):
        if isinstance(data, dict):
            for key, value in pattern.items():
                if not key in data.keys():
                    raise KeyError(key, data)
                if isinstance(value, type):
                    yield {key: data[key]}
                if isinstance(value, dict):
                    ## Drain the decorator
                    for found in scan(value, data[key]):
                        yield found

    try:
        output = dict({x.items()[0] for x in scan(pattern0, data0)})
        return output or None
    except KeyError:
        return None


def match(pattern):

    def decorator(func):
        def wrapper(data):
            kwargs = extract_from_pattern(pattern, data)
            return func(**(kwargs or {}))
        return wrapper
    return decorator
