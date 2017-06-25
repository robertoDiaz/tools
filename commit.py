#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# author Roberto Díaz
#
# Requires  gitpython. To install it run "sudo pip install gitpython"

import sys

from git import Repo

def commit(message):
	repo = Repo('.')

	repo.index.commit("%s %s" %(branchName, message))

if __name__ == "__main__":
	if len(sys.argv) == 2:
		message = sys.argv[1]

		brachName = repo.active_branch.name

		if branchName == 'master':
			raise Exception('Do not commit in master branch')

		preffix = branchName
	elif if len(sys.argv) == 3:
		message = sys.argv[1]
		preffix = sys.argv[2]
	else :
		raise Exception('Wrong parameters')

	commit(message, preffix)