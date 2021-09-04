def base64decob(string):#base64 解码 进 出bytes
    sr = ''
    wds = []
    ans = ''
    string = string.decode('utf-8')
    s = list(string)
    ise = False

    while '=' in s:
        s.pop()
        ise = True
    string = ''.join(s)
    #im = string.encode('utf-8')
    base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                   'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
    for i in string: #查表索引，找到包含原文信息的数字
        num = base64_list.index(i)
        sr += '{:06}'.format(int(str(bin(num)).replace('0b','')))

    for j in range(0,len(sr),8): #八位切割
        wds.append(sr[j:j+8])
        
    for i in range(len(wds)): #十六进制字符串转换
        fo = wds[i]
        he = hex(int(fo,2))[2:]
        if len(he) == 1:
            he = '0' + he
        ans += he
    
    ans = bytes.fromhex(ans)  #一步转换成bytes字节码
    return ans















