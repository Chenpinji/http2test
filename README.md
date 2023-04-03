# http2test
# 如何使用
(1)需要将deployment文件夹中的docker-compose.yaml里的volume挂在路径修改为自己的。

(2)启动容器

docker-compose up -d

(3)进入源站容器
docker exec -it caddy_origin_1 /bin/sh

查看是否启动tcpdump抓包和echo_server

(4)发送异常请求

python3 test_demo.py

# TODO
(1)添加no-tls环境

(2)添加自动化启动容器和发送异常请求的脚步

(3)添加对其他字段的测试
