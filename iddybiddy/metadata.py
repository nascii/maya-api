# -*- coding: utf-8 -*-


import os

MODULE_ROOT = os.path.dirname(os.path.realpath(__file__))
VERSION = open(os.path.join(MODULE_ROOT, "VERSION")).read().strip()
SERVICE_BANNER = "IddyBiddy {0}".format(VERSION)
