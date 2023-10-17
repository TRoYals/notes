---
title: docker中文教程
date: 2023-08-28 17:43
article: false
tags: 
---
# 资源

[前言 - Docker — 从入门到实践](https://yeasy.gitbook.io/docker_practice/)

## 使用镜像
### 查看系统使用情况

`docker system df`

### 列出镜像

`docker image ls`

`docker image ls --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}"`

### 删除镜像

像其它可以承接多个实体的命令一样，可以使用 `docker image ls -q` 来配合使用 `docker image rm`，这样可以成批的删除希望删除的镜像。我们在“镜像列表”章节介绍过很多过滤镜像列表的方式都可以拿过来使用。

比如，我们需要删除所有仓库名为 `redis` 的镜像：

`$ docker image rm $(docker image ls -q redis)`

或者删除所有在 `mongo:3.2` 之前的镜像：

`$ docker image rm $(docker image ls -q -f before=mongo:3.2)`

充分利用你的想象力和 Linux 命令行的强大，你可以完成很多非常赞的功能。

### 利用 commit 理解镜像

先跳过  
[利用 commit 理解镜像构成 - Docker — 从入门到实践](https://yeasy.gitbook.io/docker_practice/image/commit)

### 使用 Dockerfile 定制镜像

```
sudo yum-config-manager \

--add-repo \

https://download.docker.com/linux/centos/docker-ce.repo
```