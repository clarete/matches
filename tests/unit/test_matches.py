import matches
from mock import Mock


def test_matches_scan_dict():
    "matches.extract_from_pattern() Should find matches in a dictionary"

    # Try to match against an empty object
    matches.extract_from_pattern(
        # pattern
        {"message": {"headers": dict}},
        # data
        {}
    ).should.equal({})

    # Try to match against a wrong type
    matches.extract_from_pattern(
        # pattern
        {"message": {"headers": dict}},
        # data
        {"message": "test"}
    ).should.equal({})

    # Try to match against a wrong type
    matches.extract_from_pattern(
        # pattern
        {"message": {"headers": {"message_id": str}}},
        # data
        {"message": {"headers": {"message_id": "My ID"}}}
    ).should.equal({"message_id": "My ID"})

    # Try to match multiple keys and fail
    matches.extract_from_pattern(
        # pattern
        {"message": {"headers": {"message_id": str}, "body": str}},
        # data
        {"message": {"headers": {"message_id": "The ID"}}}
    ).should.equal({"message_id": "The ID"})

    # Try to match multiple keys and succeed
    matches.extract_from_pattern(
        # pattern
        {"message": {"headers": {"message_id": str}}, "body": str},
        # data
        {"message": {"headers": {"message_id": "The ID"}}, "body": "Message"}
    ).should.equal({"message_id": "The ID", "body": "Message"})


def test_matches_decorator():
    "@matches.match() Should wrap a function and call it with the output of the pattern match"

    # Given the following callback
    callback = Mock()

    # And a decorated version of this callback
    decorated = matches.match({"a": {"b": bool}})(callback)

    # When I call the decorated callback with data that matches the
    # pattern
    decorated({"a": {"b": True}})

    # Then I see the callback was called with the right parameter
    callback.assert_called_once_with(b=True)
