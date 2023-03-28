#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 - 2023 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file

"""
    Pre-hook script
    Checks that {{ cookiecutter.__repo_name }}:
    1. is not too short
    2. has valid characters
"""

import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

repo_name = '{{ cookiecutter.__repo_name }}'

if (not re.match(MODULE_REGEX, repo_name) or
    len(repo_name) < 2):
    raise ValueError('%s is not a valid Python module name!\
Please, check the \"project_name\" input' % repo_name)
#    print('%s is not a valid Python module name!\
#Please, check the \"project_name\" input' % repo_name)
#    sys.exit(1)

