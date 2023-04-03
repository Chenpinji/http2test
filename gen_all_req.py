from gen_te import  *
from gen_cl import *
import json
def gen_header_frame(id):
    # TODO: 对:authority、:method、:scheme修改
    head_frame =  {"<headers-frame>": {":method": "POST", ":scheme": "https", ":authority": "127.0.0.1", "flags": []}}
    head_frame["<headers-frame>"][':path'] = "/reqid=%s" %id
    return head_frame
def gen_continue_frame(header_name, header_value):
    continue_frame =  {"<continuation-frame>": {"flags": ["EH"]}}
    continue_frame["<continuation-frame>"][header_name] = header_value
    return continue_frame
def gen_data_frame(header_name, header_value):
    data_frame = {"<data-frame>": {"flags": ["ES"]}}
    data_frame["<data-frame>"][header_name] = header_value
    return data_frame

def gen_req(frames_list):
    req = {}
    # head_frame1 = gen_header_frame(1)
    # continue_frame1 = gen_continue_frame(temp[0], temp[1])
    # data_frame1 = gen_data_frame('data', 'a')
    req["<headers-frame>"] = frames_list[0]["<headers-frame>"]
    req["<continuation-frame>"] = frames_list[1]["<continuation-frame>"]
    req["<data-frame>"] = frames_list[2]["<data-frame>"]
    return req

def gen_all_te_req(te_list):
    i = 1
    req_list = []
    for te in te_list:
        req = {}
        head_frame = gen_header_frame(i)
        i+=1
        # Transfer-Encoding: chunked
        hdr_name, hdr_value = te[0], te[1]
        continue_frame = gen_continue_frame(hdr_name, hdr_value)
        data_frame = gen_data_frame('data', '5\r\nBBBBB\r\n0\r\n\r\n')
        req["<headers-frame>"] = head_frame["<headers-frame>"]
        req["<continuation-frame>"] = continue_frame["<continuation-frame>"]
        req["<data-frame>"] = data_frame["<data-frame>"]
        req_list.append(req)
    return req_list

def gen_all_cl_req(cl_list):
    i = 1
    req_list = []
    for cl in cl_list:
        req = {}
        head_frame = gen_header_frame(i)
        i+=1
        # Transfer-Encoding: chunked
        # hdr_name, hdr_value = cl.split(":")
        hdr_name, hdr_value = cl[0], cl[1]
        continue_frame = gen_continue_frame(hdr_name, hdr_value)
        #这种才是对的吗？ "\r\n1\r\n\r\n"
        data_frame = gen_data_frame('data', 'BBBBB')
        req["<headers-frame>"] = head_frame["<headers-frame>"]
        req["<continuation-frame>"] = continue_frame["<continuation-frame>"]
        req["<data-frame>"] = data_frame["<data-frame>"]
        req_list.append(req)
    return req_list

# 生产所有TE的可能情况
def gen_all_te():
    te = []
    te.extend(gen_te1())
    te.extend(gen_te2())
    # te.extend(gen_te3())
    # te.extend(gen_te4())
    # te.extend(gen_te6())
    # te.extend(gen_te6())
    return te

def gen_all_cl():
    cl = []
    cl.extend(gen_cl1())
    cl.extend(gen_cl2())
    # cl.extend(gen_cl3())
    # cl.extend(gen_cl4())
    # cl.extend(gen_cl5())
    # cl.extend(gen_cl6())
    return cl
def save_mutated_data(attack_type,attack_req_list):
    
    tmp_dict = {}
    # for i in range(len(anamaly_names)):
    #     tmp_dict[anamaly_names[i]] = anamaly_frames[i]
    i = 0
    for req in attack_req_list:
        i += 1
        tmp_dict['reqid_%s' %i] = req
    file_name = str(attack_type) + '_attack_data.json'
    with open(file_name, 'w') as f:
        json_str = json.dumps(tmp_dict, indent=0)
        f.write(json_str)
        f.write('\n')

if __name__ == "__main__":
    # req_list = gen_all_te_req(te_list = gen_te1())
    # print(len(req_list))
    # print(req_list[:2])
    
    req_list = gen_all_cl_req(cl_list = gen_all_cl())
    print(len(req_list))
    # print(req_list)
    save_mutated_data(attack_type="cl",attack_req_list=req_list)

    # req_list = gen_all_te_req(te_list = gen_all_te())
    # print(len(req_list))
    # print(req_list)
    # save_mutated_data(attack_type="te",attack_req_list=req_list)
    # te_list = gen_te1()
    # print(len(te_list))

    