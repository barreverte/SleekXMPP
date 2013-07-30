# -*- coding: utf-8 -*-
"""
    sleekxmpp.xmlstream.tostring
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module converts XML objects into Unicode strings and
    intelligently includes namespaces only when necessary to
    keep the output readable.

    Part of SleekXMPP: The Sleek XMPP Library

    :copyright: (c) 2011 Nathanael C. Fritz
    :license: MIT, see LICENSE for more details
"""

from xml.etree import cElementTree as ET

def tostring(xml=None, xmlns='', stream=None,
             outbuffer='', top_level=False, open_only=False):
    return ET.tostring(xml)
