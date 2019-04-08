#!/usr/bin/python3
"""
generates .tgz archive from web_static/ using do_pack
"""
from fabric.api import *
import datetime


def do_pack():
    """
    packs content of web_static/ into a tgz archive
    """
    now = datetime.datetime.now()
    tgz_path = 'versions/web_static_' + now.strftime('%Y%m%d%H%M%S') + '.tgz'
    tgz_cmd = 'tar -czpvf ' + tgz_path + ' web_static'
    local('sudo mkdir -p versions')

    if local(tgz_cmd).succeeded:
        return tgz_path
    return None
