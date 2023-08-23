---
title: Untitled
date: 2023-08-22 00:17
article: false
tags: 
---

MUST:  
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/openssl/lib

[centos 解决python3.7 安装时No module named \_ssl 亲测有效\_reg183的技术博客\_51CTO博客](https://blog.51cto.com/u_13646572/5361025)

(SCCCI-py3.10)  
/root/.cache/pypoetry/virtualenvs/sccci-Kp8eaCK1-py3.10/bin/python

[root@iZt4ninltrgkgfbi1o78ywZ SCCCI]# echo $PATH

/root/.cargo/bin:/home/jdk/jdk1.8.0_321/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/Py310/bin:/root/bin

[root@iZt4ninltrgkgfbi1o78ywZ SCCCI]#

normal  
(sccci-py3.10) [root@iZt4ninltrgkgfbi1o78ywZ SCCCI]# echo $LD_LIBRARY_PATH

:/root/openssl/lib

screen
