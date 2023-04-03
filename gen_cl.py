
# 用于生成所有content-length情况
CL_name_Pool = [" content-length", "\tcontent-length", "\vcontent-length", "\x00content-length", 
           "content-length ", "content-length\t", "content-length\v","content-length\x00",
           " content-length "," content-length\t", " content-length\v", " content-length\x00",
           "\tcontent-length ","\tcontent-length\t", "\tcontent-length\v", "\x00content-length\x00",
           "\vcontent-length ","\vcontent-length\t", "\vcontent-length\v", "\vcontent-length\x00",
           "\x00content-length ","\x00content-length\t", "\x00content-length\v", "\x00content-length\x00",
           " content_length", "\tcontent_length", "\vcontent_length", "\x00content_length", 
           "content_length ", "content_length\t", "content_length\v","content_length\x00",
           " content_length "," content_length\t", " content_length\v", " content_length\x00",
           "\tcontent_length ","\tcontent_length\t", "\tcontent_length\v", "\x00content_length\x00",
           "\vcontent_length ","\vcontent_length\t", "\vcontent_length\v", "\vcontent_length\x00",
           "\x00content_length ","\x00content_length\t", "\x00content_length\v", "\x00content_length\x00"
           ]
cl_value_Pool = ["1", "-1"]

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

def gen_cl2():
    cl2 = []
    for i in range(0x7F,0x100):
        cl2.append(["content-length","%c1"%(i)]) 
        cl2.append(["content-length","1%c"%(i)])
        cl2.append(["content-length%c"%(i),"2"])
        cl2.append(["%ccontent-length"%(i),"2"])

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
# 被上面包括 但是插入x的情况还没实验
def gen_cl3():
    cl3 = []
    for i in ["\r", "\r\n", "\n"]:
        # cl3.append(["content-length:%c1"%(i)))
       
        # cl3.append(["content-length%c: 1"%(i)))
       
        # cl3.append(["%ccontent-length: 1"%(i)))
       
        # cl3.append(["content-length: 1%c"%(i)))
       
        #这些情况根据:分割有问题
        cl3.append(["X: X%ccontent-length"%(i),"1"])
        cl3.append(["content-length", "1%cX: X"%(i)])
        cl3.append(["X: X%ccontent_length"%(i),"1"])
        cl3.append(["content_length", "1%cX: X"%(i)])
        # cl3.append(["X: X%ccontent-length: 1"%(i)))
       
        # cl3.append(["content-length: 1%cX: X"%(i)))
       
        # cl3.append(["X: X\r%ccontent-length: 1"%(i)))
       
        # cl3.append(["X: X%c\ncontent-length: 1"%(i)))
       
        # cl3.append(["content-length: 1\r%cX: X"%(i)))
       
        # cl3.append(["content-length: 1%c\nX: X"%(i)))
        return cl3
       

def gen_cl4():
    cl4 = [" content-length: 1", "content-length:\t1", "content-length\t:\t1","content length: 1",
       "content_length: 1", "content length:1","content-length : 1", "content-length:  1",
       "content-length:\u000B1", "content-length: 1, cow","content-length: cow, 1","Content-Length: 1",
       "content-length:\n 1","content-length: \"1\"","content-length: '1'","content-length: chunk",
       "content-length: 1", "content-length: 1", "content-length: 1\r", "content-length: 1\t",
        "content\r-length: 1","content-length: cow 1 bar","content-length:\xFF1",
       "content-length: ch\x96nked", "conten\x82t-length: 1"]
       #"content-length: cow\r\ncontent-length: 1","X:X\rcontent-length: 1","X:X\ncontent-length: 1"]
    return cl4

def gen_cl5():
    cl5 =[]
    for i in range(0x1,0x21):
        cl5.append(["%ccontent-length%c"%(i,i), "1"])
        cl5.append(["%ccontent-length"%(i),"%c1"%(i)])
        cl5.append(["%ccontent-length"%(i),"1%c"%(i)])
        cl5.append(["content-length%c"%(i),"%c1"%(i)])
        cl5.append(["content-length%c"%(i), "1%c"%(i)])
        cl5.append(["content-length","%c1%c"%(i,i)])
    return cl5

def gen_cl6():
    cl6 =[]
    for i in range(0x7F,0x100):
        cl6.append(["%ccontent-length%c"%(i,i), "1"])
        cl6.append(["%ccontent-length"%(i),"%c1"%(i)])
        cl6.append(["%ccontent-length"%(i),"1%c"%(i)])
        cl6.append(["content-length%c"%(i),"%c1"%(i)])
        cl6.append(["content-length%c"%(i), "1%c"%(i)])
        cl6.append(["content-length","%c1%c"%(i,i)])
    return cl6

if __name__ == "__main__":
    cl3 = gen_cl3()
    print(cl3)