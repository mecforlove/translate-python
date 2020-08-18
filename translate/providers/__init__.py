#!/usr/bin/env python
# encoding: utf-8

from .mymemory_translated import MyMemoryProvider  # noqa
from .microsoft import MicrosoftProvider  # noqa
from .youdao import YoudaoProvider

__all__ = ['MyMemoryProvider', 'MicrosoftProvider', 'YoudaoProvider']
