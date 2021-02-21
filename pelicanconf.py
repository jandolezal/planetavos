#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

AUTHOR = 'Jan Doležal'
SITENAME = 'Planeta vos'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'Europe/Prague'
LOCALE = 'cs_CZ'
DEFAULT_LANG = 'cs'

DELETE_OUTPUT_DIRECTORY = True

THEME = 'theme'
DEFAULT_DATE_FORMAT = '%d. %B %Y'

# Links
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}.html'
ARTICLE_URL = 'posts/{date:%Y}/{slug}.html'
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAG_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
