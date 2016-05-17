#!/usr/bin/env python
import os
import subprocess
import sys
import urllib2


USER = os.environ.get('GITHUB_USER')
ENDPOINT = 'https://api.github.com/repos/%s/dnsdock/releases' % USER
RELEASE = os.environ.get('REFS')



def exit(reason=None):
    print('Something went wrong exiting...')
    if reason is not None:
        print(reason)
    sys.exit(1)

def generate_repo():
    import pdb; pdb.set_trace()



if __name__ == '__main__':
    endpoint = urlize(GITHUB_URL, release) % user

    popen = subprocess.Popen(['git', 'checkout', 'tags/%s' % release],
                             stderr=subprocess.PIPE)

    _, err = popen.communicate()
    if popen.returncode:
        exit(err)
    try:
        res = urllib2.urlopen(endpoint)
    except urllib2.HTTPError as err:
        if err.code == 404:
            res = generate_repo()
        else:
            exit('%s: %s' % (err.code, err.reason))






#git checkout "$REFS"
#
#RELEASE=$(git describe --tags)
#
#[[ "$RELEASE" == *"-"* ]] && echo "Not on a tag exiting..." && exit 1
#
#curl "https://api.github.com/repos/$GITHUB_USER/dnsdock/releases"
