# coding=utf-8

import time
import os
import sys
import requests
from bs4 import BeautifulSoup
import gitlab
import subprocess
from gitlab import Gitlab


def get_pods_list(page_num=5):
    
    gitlab_url = "http://gitlab.***.domain"
    gl = gitlab.Gitlab(gitlab_url, "private-key")
    # projects = gl.projects.list(all=True)

    projects_list = gl.projects.list(search="projectName",page=1,per_page=100)

    # tmp_pro = gl.projects.get(projects_list[2].id,statistics=1)
    # print tmp_pro.name
    # print tmp_pro
    for tmp_pro in projects_list:
        obj = gl.projects.get(tmp_pro.id,statistics=1)
        storage_size = obj.statistics["storage_size"]
        respository_size = obj.statistics["repository_size"]
        print "{name}  {size1} | {size2}".format(name=obj.name, size1=storage_size, size2=respository_size)
        ksize = long(storage_size) / 1024.0 
    
        if ksize <= 1024:
            print "%s, size=%.2f K" % (obj.name,ksize)
        else:
            # msize = ksize >> 10
            msize = ksize/ 1024.0
            if msize <= 1024:
                print "%s, size=%.2f M" % (obj.name,msize)
            else:
                # gsize = msize >> 10
                gsize = msize/ 1024.0
                if gsize <= 1024:
                    print "%s, size=%.2f G" % (obj.name,gsize)
                else:
                    print str(gsize)
        if storage_size != respository_size:
            print "not equal"+obj.name
    
if __name__ == "__main__":
    # get_pods_list()

   