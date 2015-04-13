# Matches

Matches is a small library for extracting function parameters from
nested data structures.

## Quick Example

Given a function that needs two fields from a more complex dictionary,
instead of writing the code that navigates through the nested
dictionaries, the `@match` decorator can be used to extract only the
needed fields:

```python
>>> import matches
>>> @matches.match({"message": {"headers": {"title": str}, "body": str}})
... def on_message_received(title=None, body=None):
...     return title, body
```

Here are a few cases and how matches works for each of them:

```python
>>> on_message_received({})
(None, None)
>>> on_message_received({"message": {"headers": {"title": "Test"}}})
("Test", None)
>>> on_message_received({"message": {"body": "My message"}})
(None, "My message")
>>> on_message_received({"message": {"headers": {"title": "Name"}, "body": "Content"}})
("Name", "Content")
```

## License

The MIT License (MIT)

Copyright (c) 2015 Lincoln Clarete

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
