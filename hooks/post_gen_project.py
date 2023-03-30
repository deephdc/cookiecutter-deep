#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 - 2019 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file

"""
    Post-hook script:
    1. Moves DEEP-OC-{{ cookiecutter.__repo_name }} directory one level up.
    2. Initialized Git repositories
    3. Creates 'master', 'test' branches
    4. Switches back to 'master'

    NB: Check for the correct repo_name happens in "pre_gen_project.py" hook!
"""
import logging
import os
import shutil
import subprocess as subp
import sys

# conigure python logger
logger = logging.getLogger('pre_gen_project.py')
logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s')

repo_name = '{{ cookiecutter.__repo_name }}'
deep_oc = 'DEEP-OC-{{ cookiecutter.__repo_name }}'
deep_oc_dir = os.path.join("../", deep_oc)
src = os.path.join("../", repo_name, deep_oc)


def git_ini(repo):
    """ Function
        Initializes Git repository
    """
    gitrepo = os.path.join('{{ cookiecutter.git_base_url }}',
                           repo + '.git')
    try:
        os.chdir("../" + repo)
        subp.call(["git", "init"])
        subp.call(["git", "add", "."])
        subp.call(["git", "commit", "-m", "initial commit"])
        subp.call(["git", "remote", "add", "origin", gitrepo])

        # create test branch automatically
        subp.call(["git", "checkout", "-b", "test"])
        # adjust [Build Status] for the test branch
        readme_content=[]
        with open("README.md") as f_old:
            for line in f_old:
                if "[![Build Status]" in line:
                    line = line.replace("/master)", "/test)")
                readme_content.append(line)

        with open("README.md", "w") as f_new:
            for line in readme_content:
                f_new.write(line)

        subp.call(["git", "commit", "-a", "-m", "update README.md for the BuildStatus"])

        # switch back to master
        subp.call(["git", "checkout", "master"])
    except OSError as os_error:
        message = ("Creating git repository failed " +
                   "for {} ! ({})".format(repo, os_error))
        logger.exception(message)
        return "Error"
    else:
        return gitrepo


try:
    # move DEEP-OC-{{ cookiecutter.__repo_name }} one level up
    shutil.move(src, deep_oc_dir)

    # initialized both git repositories
    git_user_app = git_ini(repo_name)
    git_deep_oc = git_ini(deep_oc)

    if "Error" not in git_user_app and "Error" not in git_deep_oc:
        message = F"""
[Info] {repo_name} was created successfully,
       Don't forget to create corresponding remote repository: {git_user_app}
       then you can do 'git push origin --all'")

[Info] {deep_oc} was created successfully,
       Don't forget to create corresponding remote repository: {git_deep_oc}
       then you can do 'git push origin --all'"""
        print(message)
    sys.exit(0)
except OSError as os_error:
    message = ("While attempting to move {} and create ".format(src) +
               "git repository an error ({}) occurred!".format(os_error))
    logger.exception(message)
    sys.exit(1)
