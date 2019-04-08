#!/usr/bin/python3
"""
generates .tgz archive and deploys
"""
from fabric.api import *
from fabric.contrib.files import exists
import datetime
import os


env.hosts = ['35.196.70.29', '34.73.105.249']


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


def do_deploy(archive_path):
    """
    uploads archive, uncompresses, and creates new symbolic links
    """
    if not os.path.isfile(archive_path):
        return False
    put(archive_path, "/tmp/")
    splitpath = archive_path.split('/')
    cp_path = ' /data/web_static/releases/' + (splitpath[-1])[:-4]
    tmp_path = '/tmp/' + splitpath[-1]
    if sudo('mkdir -p ' + cp_path).failed:
        return False
    if sudo("tar -xvf " + tmp_path + ' -C' + cp_path).failed:
        return False
    if sudo('mv ' + cp_path + '/web_static/* ' + cp_path).failed:
        return False
    if sudo('rm -rf ' + cp_path + '/web_static').failed:
        return False
    if sudo('rm -rf /data/web_static/current').failed:
        return False
    if sudo('ln -s ' + cp_path + ' /data/web_static/current').failed:
        return False
    print('New version deployed!')
    return True
