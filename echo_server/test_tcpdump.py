import os
import time
import uuid

time.sleep(120)
# 生成随机文件名
filename = "/pcap/" + str(uuid.uuid4()) + ".pcap"

# 运行tcpdump命令并将输出保存到文件中 在7200s后停止
os.system("timeout  7200 tcpdump -w " + filename)

