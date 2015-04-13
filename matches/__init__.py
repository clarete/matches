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
