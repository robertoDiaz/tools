import os
import sys
from git import Repo
from git import Remote
    
if len(sys.argv) == 2:
	remoteBranch = sys.argv[1]
	localBranch = sys.argv[1]
elif len(sys.argv) == 3:
	remoteBranch = sys.argv[1]
	localBranch = sys.argv[2]
else :
	raise Exception('Wrong parameters')

repo = Repo('.')
remote = Remote(repo, 'upstream')

print('Fetching ' + remoteBranch)

remote.fetch('refs/tags/' + remoteBranch)

print('Creating  and checking out ' + localBranch)

repo.create_head(localBranch, 'FETCH_HEAD').checkout()