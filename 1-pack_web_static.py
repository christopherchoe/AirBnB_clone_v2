#!/usr/bin/python3
"""
generates .tgz archive from /data/web_static/ using do_pack
"""
from fabric.api import *
import datetime


env.hosts = ['34.73.105.249']

def do_pack():
    """
    packs content of /data/web_static/ into a tgz archive
    """
    now = datetime.datetime.now()
    tgz_path = 'web_static_' + now.strftime('%y%m%d%H%M%S')
    tgz_cmd = 'tar -czpvf versions/' + tgz_path + ' /data/web_static'
    local('sudo mkdir -p versions')

    if local(tgz_cmd).succeeded:
        return tgz_path
    return None
