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
# Requires 1 parameter, the remote branch. Has a second parameter optional that allows
# set the local branch name. If not used, the remote branch name will be used as
# local branch name. The third parameter is also optional and allows use this script
# in 6.2 since we use tags in this branch. Examples:
#
# FOR DXP : python checkout.py fix-pack-de-39-7010 fix-pack-de-39-local false
# For 6.2 : python checkout.py fix-pack-fix-71134663 rama-local true
#			python checkout.py fix-pack-fix-71134663 rama-local
#

import os
import sys

from git import Repo
from git import Remote
    

def checkout(remoteBranch, localBranch, tag):
	repo = Repo('.')

	print('Fetching ' + remoteBranch)

	if tag:
		Remote(repo, 'upstream').fetch('refs/tags/' + remoteBranch)
	else :
		Remote(repo, 'upstream').fetch(remoteBranch)

	print('Creating and checking out ' + localBranch)

	repo.create_head(localBranch, 'FETCH_HEAD').checkout()

if __name__ == "__main__":
	if len(sys.argv) == 2:
		remoteBranch = sys.argv[1]
		localBranch = sys.argv[1]
		tag = true
	elif len(sys.argv) == 3:
		remoteBranch = sys.argv[1]
		localBranch = sys.argv[2]
		tag = true
	elif len(sys.argv) == 4:
		remoteBranch = sys.argv[1]
		localBranch = sys.argv[2]
		tag = sys.argv[3]
	else :
		raise Exception('Wrong parameters')

	checkout(remoteBranch, localBranch, tag)
