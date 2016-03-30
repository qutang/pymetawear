#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`exceptions`
=======================

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2016-03-30, 10:11

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import


class PyMetawearException(Exception):
    """Main exception."""
    pass


class PyMetawearConnectionTimeout(PyMetawearException):
    """Connection could not be established in time."""
    pass
