def lha(text):
    import base64
    strin = text

    def is_num(str):
        try:
            int(str)
            return True
        except:
            return False





    def Hash(text: str):
        hash = 0
        for ch in text:
            hash = (hash * 281 ^ ord(ch) * 99768554684859657) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        return hash
    


    strin = str(Hash(strin))





    a = str(base64.b16encode(bytes(strin, 'utf-8')))
    b = str(base64.b32encode(bytes(strin, 'utf-8')))
    c = str(base64.b64encode(bytes(strin, 'utf-8')))
    d = str(base64.b85encode(bytes(strin, 'utf-8')))

    

    def num(text):
        a = 1
        b = 0
        number = ""

        for i in range(len(text)):
            txt = text[:a]
            txt2 = txt[b:]
            txt3 = ord(txt2)

            number = number + str(txt3)
            a += 1
            b += 1
        return int(number)

    def num2(text):
        a = 1
        b = 0
        number2 = 0

        for i in range(len(text)):
            txt = text[:a]
            txt2 = txt[b:]
            txt3 = ord(txt2)

            number2 = number2 + txt3
            a += 1
            b += 1
        return int(number2)

    x0 = num(strin)
    x1 = num(a)
    x2 = num(b)
    x3 = num(c)
    x4 = num(d)
    x5 = num2(strin)
    x6 = num2(a)
    x7 = num2(b)
    x8 = num2(c)
    x9 = num2(d)

    zwh = str(hex(x0^x1^x8^x2^x3^x9^x4^x7^x5^x6))

    if ".5" in str(len(zwh) / 2):
        zwh += "f"

    cut = len(zwh)
    cut_zwh = int(cut / 2)
    
    zwh1 = zwh[:cut_zwh]
    zwh2 = zwh[cut_zwh:]
    
    num_zwh1 = num(zwh1)
    num_zwh2 = num(zwh2)
    
    num_zwh1_rev = num(zwh1[::-1])
    num_zwh2_rev = num(zwh2[::-1])
    
    zhh = num_zwh1_rev^num_zwh1
    zhh2 = num_zwh2_rev^num_zwh2
    
    zhh3 = zhh^zhh2
    zhh4 = zhh3
    
    zhh5 = zhh4^int(str(Hash(strin)**25))
    zhh6 = zhh5^19165316278338047141665660496286470744
    
    line = str(zhh6)
    n = 25
    x = [line[i:i+n] for i in range(0, len(line), n)]
    
    a=int(x[0])
    b=int(x[1])
    
    c=int(x[2])
    d=int(x[3])
    
    e=int(x[4])
    f=int(x[5])
    
    g=int(x[6])
    h=int(x[7])
    
    zhh7 = a^b
    zhh8 = c^d
    
    zhh9 = e^f
    zhh10 = g^h
    
    zhh11 = zhh7^zhh9
    zhh12 = zhh8^zhh10
    
    zhh13 = zhh11^zhh12
    return str(hex(zhh13**4))[2:][:64]
