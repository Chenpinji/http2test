
from test_demo import test
import argparse  # 1、导入argpase包
import time 
import datetime

def parse_args():
    parse = argparse.ArgumentParser(description='Test HTTP/2')  # 2、创建参数对象
    parse.add_argument('-f', '--file', default='cl_attack_data.json', type=str, help='Filename of attack data')  # 3、往参数对象添加参数
    parse.add_argument('-dn', '--destnation', default="127.0.0.1", type=str, help='IP of reverse proxy')
    parse.add_argument('-p', '--port', default=443, type=int, help='Port of reverse proxy')
    parse.add_argument('-v', '--verbose', default=False, type=bool, help='print')
    args = parse.parse_args()  # 4、解析参数对象获得解析对象
    return args




if __name__ == '__main__':
    args = parse_args()
    start_time = time.time()
    start_time_human = datetime.datetime.now()

    # 格式化输出时间 
    print("程序开始时间为：", start_time_human.strftime("%Y-%m-%d %H:%M:%S"))
    test(dn=args.destnation, port=args.port, attack_file_name=args.file,verbose=args.verbose)
    end_time = time.time()
    end_time_human = datetime.datetime.now()
    # 格式化输出时间
    print("程序结束时间为：", end_time_human.strftime("%Y-%m-%d %H:%M:%S"))
    # print("程序结束时间为：", end_time)
    elapsed_time = datetime.timedelta(seconds=end_time - start_time)
    print("程序运行时间为：", elapsed_time)