# coding: utf-8

import pytest

from bearychat import Incoming, InvalidPayloadError


@pytest.fixture
def incoming():
    return Incoming('http://example.org')


def test_text(incoming):
    expected_text = 'foobar'
    message = incoming \
        .reset() \
        .with_text(expected_text) \
        .build_message()
    assert message['text'] == expected_text
    assert message['markdown'] is False

    message = incoming \
        .reset() \
        .with_text(expected_text, markdown=True) \
        .build_message()
    assert message['text'] == expected_text
    assert message['markdown'] is True

    message = incoming \
        .reset() \
        .with_markdown(expected_text) \
        .build_message()
    assert message['text'] == expected_text
    assert message['markdown'] is True

    with pytest.raises(InvalidPayloadError):
        incoming.reset().build_message()


def test_to(incoming):
    message = incoming \
        .reset() \
        .with_text('foobar') \
        .build_message()
    assert 'channel' not in message

    expected_room = 'foobar'
    message = incoming \
        .reset() \
        .to(expected_room) \
        .with_text('foobar') \
        .build_message()
    assert message['channel'] == expected_room


def test_attachment(incoming):
    message = incoming \
        .reset() \
        .with_text('foobar') \
        .with_attachment(title='foobar') \
        .build_message()
    assert isinstance(message['attachments'], list)

    with pytest.raises(InvalidPayloadError):
        incoming \
            .reset() \
            .with_text('foobar') \
            .with_attachment(something_else='foobar') \
            .build_message()
