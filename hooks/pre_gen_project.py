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
from urllib.parse import urlparse

# init array of errors, must init with 0
errors = [0]

# conigure python logger
logger = logging.getLogger('pre_gen_project.py')
logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s')

# check {{ cookiecutter.git_base_url}}
def check_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

git_base_url = '{{ cookiecutter.git_base_url}}'
if (not check_url(git_base_url)):
    message = ("'{}' is not a valid URL! ".format(git_base_url) +
               "Please, check the 'git_base_url' input")
    logger.error(message)
    errors.append(1)

# check {{ cookiecutter.__repo_name }}
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
repo_name = '{{ cookiecutter.__repo_name }}'
if (not re.match(MODULE_REGEX, repo_name) or
    len(repo_name) < 2):
    message = ("'{}' is not a valid Python module name! ".format(repo_name) +
               "Please, check the 'project_name' input")
    logger.error(message)
    errors.append(1)

print(F"errors: {errors}")
if sum(errors) > 0:
    sys.exit(1)
