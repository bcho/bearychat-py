# coding: utf-8

'''
    incoming
    ~~~~~~~~

    Incoming robot api.
'''

__all__ = ['InvalidPayloadError', 'Incoming']


import requests


class InvalidPayloadError(ValueError):
    pass


class Incoming(object):
    '''Incoming api.

        resp = Incoming(hook_url) \
            .to('bearychat-dev') \
            .with_text('hello, world', markdown=False) \
            .with_attchment(title='pic', text='cool picture') \
            .push()

        resp = Incoming(hook_url) \
            .to('bearychat-dev') \
            .with_markdown('# hello, world\n## foobar') \
            .push()
    '''

    DEFAULT_CHANNEL = None

    def __init__(self, hook):
        # hook url
        self.hook = hook

        self.reset()

    def reset(self):
        '''Reset stream.'''
        self._text = None
        self._markdown = False
        self._channel = Incoming.DEFAULT_CHANNEL
        self._attachments = []

        return self

    def to(self, channel):
        '''Set destinate channel.

        :param channel: channel name.
        '''
        self._channel = channel

        return self

    def with_text(self, text, markdown=None):
        '''Set text content.

        :param text: text content.
        :param markdown: is markdown? Defaults to ``False``.
        '''
        self._text = text
        self._markdown = markdown or False

        return self

    def with_markdown(self, text):
        '''Set markdown content.

        :param text: markdown text content.
        '''
        return self.with_text(text, markdown=True)

    def with_attachment(self, **payload):
        '''Add an attachment.

        :param payload: attachment payload.
        '''
        self._attachments.append(payload)

        return self

    def build_message(self):
        '''Build a message.

        :raises InvalidPayloadError:
        '''
        if self._text is None:
            raise InvalidPayloadError('text is required')

        message = {
            'text': self._text,
            'markdown': self._markdown
        }

        if self._channel != Incoming.DEFAULT_CHANNEL:
            message['channel'] = self._channel

        if self._attachments:
            message['attachments'] = []
            for attachment in self._attachments:
                if 'title' not in attachment and 'text' not in attachment:
                    raise InvalidPayloadError('title or text is required')
                message['attachments'].append(attachment)

        return message

    def push(self):
        '''Deliver the message.'''
        message = self.build_message()
        return requests.post(self.hook, data=message)
