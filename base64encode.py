def base64encob(binary): #BASE64编码，进二进制，出bytes
    base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                   'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
    n = ''
    sy = []
    ans = ''
    v = binary
    for i in range(len(v)): #八位补零，进入大字符串
        n += '{:08}'.format(int(str(bin(v[i])).replace('0b','')))
    
    for i in range(0,len(n),6): #六位一切割
        sy.append('{:<06}'.format(n[i:i+6]))
    for i in sy: #查表
        ans += base64_list[int(i,2)]
    if len(v)%3 == 2:  #查看是否需要补=
        ans += '='
        
    elif len(v)%3 == 1:
        ans += '=='

    return ans.encode('utf-8') 
