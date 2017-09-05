### Ubuntu16.04 docker安装

#### 脚本自动安装

1. 官方脚本

   `curl -sSL https://get.docker.com/ | sh`


2. 阿里云安装脚本

   `curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -`

3. DaoCloud安装脚本

   `curl -sSL https://get.daocloud.io/docker | sh`

#### 手动安装

略

#### 启动Docker引擎

```shell
$ sudo systemctl enable docker
$ sudo systemctl start docker
```

#### 建立docker用户组

1. 建立docker组（一般默认会自己建立）
2. 将当期用户加入到docker组（`sudo usermod -aG docker $USER`）



### 镜像加速器

https://cr.console.aliyun.com/#/accelerator

https://www.daocloud.io/mirror#accelerator-doc

http://docs.alauda.cn/feature/accelerator.html