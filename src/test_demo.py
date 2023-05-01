from gen_req import check_file
from h2client import H2Client
import time 
import os
import datetime
# 导入对应库
import ssl
# 全局关闭ssl验证



    
def test_normal_req(dn, port, attack_file_name):
    # 用于测试正常的te和cl能否发给后端
    h2client = H2Client(verbose=True)
    req_list = h2client.gen_all_frames(file_name=attack_file_name)
    for req in req_list:
        time.sleep(0.5)
        temp_h2client = H2Client(verbose=True)
        temp_h2client.send(dn=dn, port=port, frames=req)

def test(dn, port, attack_file_name,verbose=False):
    # 检查文件是否存在
    check_file(check_file_name=attack_file_name)
    start_time = time.time()
    start_time_human = datetime.datetime.now()

    # 格式化输出时间 
    print("程序开始时间为：", start_time_human.strftime("%Y-%m-%d %H:%M:%S"))
    # print("程序开始时间为：", start_time)

    h2client = H2Client(verbose=verbose)
    frames = h2client.gen_all_frames(file_name=attack_file_name)
    # print(frames)
    i = 0
    h2client.send(dn=dn, port=port, frames=frames)
    # for req in req_list:
    #     i += 1
    #     print(f"reqid={i}")
    #     time.sleep(0.1)
    #     temp_h2client = H2Client(verbose=verbose)
    #     temp_h2client.send(dn=dn, port=port, frames=req)
        # for i in range(max(temp_h2client._static_entries.keys()) + 1, max(temp_h2client._static_entries.keys()) + 1 + len(temp_h2client._dynamic_table)):
        #     print('Header: {} Value: {}'.format(temp_h2client[i].name(), temp_h2client[i].value()))
    end_time = time.time()
    end_time_human = datetime.datetime.now()
    # 格式化输出时间
    print("程序结束时间为：", end_time_human.strftime("%Y-%m-%d %H:%M:%S"))
    # print("程序结束时间为：", end_time)
    elapsed_time = datetime.timedelta(seconds=end_time - start_time)
    print("程序运行时间为：", elapsed_time)

if __name__ == '__main__':
    #ssl._create_default_https_context = ssl._create_unverified_context
    test(dn='chenpinji.freetls.fastly.net', port=443, attack_file_name='cl_attack_data.json',verbose=True)
    # test(dn='127.0.0.1', port=443, attack_file_name='te_attack_data.json')

