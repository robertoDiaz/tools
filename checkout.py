#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# author Roberto Díaz
#
# Requires  gitpython.
#
# To install it run "sudo pip install gitpython"
#
# Instructions:
# 
# Requires 1 parameter, the remote branch or tag. Has a second optional that allows
# set the local branch name. If not used, the remote branch name will be used as
# local branch name.

import os
import sys

from git import Repo
from git import Remote
    

def checkout(remoteBranch, localBranch):
	repo = Repo('.')

	print('Fetching ' + remoteBranch)

	Remote(repo, 'upstream').fetch('refs/tags/' + remoteBranch)

	print('Creating  and checking out ' + localBranch)

	repo.create_head(localBranch, 'FETCH_HEAD').checkout()

if __name__ == "__main__":
	if len(sys.argv) == 2:
		remoteBranch = sys.argv[1]
		localBranch = sys.argv[1]
	elif len(sys.argv) == 3:
		remoteBranch = sys.argv[1]
		localBranch = sys.argv[2]
	else :
		raise Exception('Wrong parameters')

	checkout(remoteBranch, localBranch)
