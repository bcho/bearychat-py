# coding: utf-8

'''
    bearychat
    ~~~~~~~~~

    A simple package for interacting with `bearychat`_ API.

    .. _bearychat: http://bearychat.com/
'''

from __future__ import absolute_import

from .incoming import Incoming, InvalidPayloadError


__all__ = ['Incoming', 'InvalidPayloadError']
