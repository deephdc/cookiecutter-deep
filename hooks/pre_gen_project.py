#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 - 2023 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file

"""
    Pre-hook script
    Checks that {{ cookiecutter.__repo_name }}:
    1. is not too short (has to be more than one character)
    2. has valid characters
"""

import logging
import re
import sys

# conigure python logger
logger = logging.getLogger('__name__')

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

repo_name = '{{ cookiecutter.__repo_name }}'

if (not re.match(MODULE_REGEX, repo_name) or
    len(repo_name) < 2):
    message = ("'{}' is not a valid Python module name! ".format(repo_name) +
               "Please, check the 'project_name' input")
    logger.exception(message)
    #raise ValueError(message)
    sys.exit(1)
