#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''A module that helps bootstrap Rez onto Shotgun's Pipeline Configuration.'''

# IMPORT STANDARD LIBRARIES
import tempfile
import sys
import os

# IMPORT THIRD-PARTY LIBRARIES
_CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
_SHOTGUN_CONFIG_ROOT = os.path.dirname(_CURRENT_DIR)
_VENDORS_PATH = os.path.join(_SHOTGUN_CONFIG_ROOT, 'vendors')
# This sys.path.append adds `rezzurect` and any other third-party library that we need
sys.path.append(_VENDORS_PATH)
sys.path.append(os.path.join(_VENDORS_PATH, 'rez-2.23.1-py2.7'))

from rezzurect.utils import config_helper
import yaml


config_helper.init_custom_pythonpath()


def _get_config_root_directory():
    '''str: Get the absolute path of this Shotgun Pipeline configuration.'''
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def init_config():
    '''Get this Pipeline Configuration's Rez config file and add it.

    If the user has a REZ_CONFIG_FILE already defined then prefer it over
    this Configuration's .rezconfig file.

    Important:
        This is the linchpin that keeps Shotgun and Rez working together.
        Make changes to this function only if you know what you're doing.

    '''
    config_file = os.getenv('REZ_CONFIG_FILE')

    if config_file:
        return

    os.environ['REZ_CONFIG_FILE'] = get_config_path()


def get_config_path():
    '''str: Get the absolute path to this Pipeline Configuration's Rez config file.'''
    return os.path.join(_get_config_root_directory(), '.rezconfig')
