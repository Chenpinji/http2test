from gen_te import  *
from gen_cl import *
from gen_all_req import *
from h2client import H2Client
import time 
import os
import datetime

def check_file(check_file_name):
    # check_file_name = "cl_attack_data.json"
    dir_path = "."
    # for file in os.listdir(dir_path):
    if check_file_name in os.listdir(dir_path):
        print("data exist")
    else:
        if check_file_name.startswith('cl'):
            print("gen all cl attack data")
            cl_attack_req_list = gen_all_cl_req(cl_list = gen_all_cl())
            save_mutated_data(attack_type="cl",attack_req_list=cl_attack_req_list)
        elif check_file_name.startswith('te'):
            print("gen all te attack data")
            te_attack_req_list = gen_all_te_req(te_list = gen_all_te())
            save_mutated_data(attack_type="te",attack_req_list=te_attack_req_list)
    
def test_normal_req(dn, port, attack_file_name):
    # 用于测试正常的te和cl能否发给后端
    h2client = H2Client(verbose=True)
    req_list = h2client.gen_all_frames(file_name=attack_file_name)
    for req in req_list:
        time.sleep(0.5)
        temp_h2client = H2Client(verbose=True)
        temp_h2client.send(dn=dn, port=port, frames=req)

def test(dn, port, attack_file_name):
    start_time = time.time()
    start_time_human = datetime.datetime.now()

    # 格式化输出时间 
    print("程序开始时间为：", start_time_human.strftime("%Y-%m-%d %H:%M:%S"))
    # print("程序开始时间为：", start_time)

    h2client = H2Client(verbose=False)
    req_list = h2client.gen_all_frames(file_name=attack_file_name)
    i = 0
    for req in req_list:
        i += 1
        print(f"reqid={i}")
        time.sleep(0.1)
        temp_h2client = H2Client(verbose=False)
        temp_h2client.send(dn=dn, port=port, frames=req)
    end_time = time.time()
    end_time_human = datetime.datetime.now()

    # 格式化输出时间
    print("程序结束时间为：", end_time_human.strftime("%Y-%m-%d %H:%M:%S"))
    # print("程序结束时间为：", end_time)
    elapsed_time = datetime.timedelta(seconds=end_time - start_time)
    print("程序运行时间为：", elapsed_time)

if __name__ == '__main__':

    check_file("cl_attack_data.json")
    check_file("te_attack_data.json")
    test(dn='127.0.0.1', port=443, attack_file_name='cl_attack_data.json')
    test(dn='127.0.0.1', port=443, attack_file_name='te_attack_data.json')

