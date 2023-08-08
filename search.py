import os.path
import re
import sys
import os

path_1=sys.argv[1]

def step_1(a,panduan_1,b):
    wenjian=[]
    if panduan_1==" ": #or
        for parentdir, dirname, filenames in os.walk(path_1):
            for filename in filenames:
    #             print(filename)
                cunzai=0
                if os.path.splitext(filename)[1] == '.txt':
                    with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                        u=file.read()
                        file.close()
                        u=u.replace("\n"," ")
                        juzi=u.split(".")
                    for i in juzi:
                        if a in i or b in i:
                            list_2=i.split(" ")
                            if a in list_2 or b in list_2:
                                cunzai=1
                                break
                    if cunzai==1:
                        break
                    if cunzai:
                        filename=filename.strip(".txt")
                    
                        wenjian.append(filename)

    if "+" in panduan_1 or "/"in panduan_1 or panduan_1=="&": #+n/n+s/s&
        panduanci=panduan_1
        if "+" in panduanci:
            if "s" in panduanci:
#                 print("+s shuchu")
                diyige=a
                dierge=b
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
                        cunzai=0
                        if os.path.splitext(filename)[1] == '.txt':
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if diyige in i:
                                    if dierge in i:
                                        if " " in diyige:
                                            list_11=diyige.split(" ")
                                            diyige=list_11[0]
#                                         print(i)
                                        list_1=i.split(" ")
                                        if diyige in list_1 and dierge in list_1:
                                            jishu_1=int(list_1.index(diyige))
                                            jishu_2=int(list_1.index(dierge,jishu_1))
                                            if jishu_1<jishu_2:
                                                cunzai=1
                                                break
                            if cunzai:
                                 filename=filename.strip(".txt")
                                 wenjian.append(filename)
            else: #+n
#                 print("+n shuchu")
                diyige=a
                dierge=b
                juli=panduanci.replace("+","")
                juli=int(juli)
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
            #             print(filename)
                        cunzai=0
                        if os.path.splitext(filename)[1] == '.txt':
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if diyige in i and dierge in i:
                                    list_1=i.split(" ")
                                    if " " in diyige:
                                        list_11=diyige.split(" ")
                                        diyige=list_11[0]
                                    if diyige in list_1 and dierge in list_1:
                                        jishu_1=int(list_1.index(diyige))
                                        jishu_2=int(list_1.index(dierge))
                                        if jishu_1+juli>=jishu_2:
                                            cunzai=1
                                            break
                            if cunzai:
                                filename=filename.strip(".txt")
                                wenjian.append(filename)
        if "/" in panduanci:
            if "s" in panduanci:
#                 print("/s shuchu")
                diyige=a
                dierge=b
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
                        cunzai=0
                        if os.path.splitext(filename)[1] == '.txt':
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if diyige in i and dierge in i:
                                    list_1=i.split(" ")
                                    if diyige in list_1 and dierge in list_1:
                                        cunzai=1
                                        break
                            if cunzai:
                                filename=filename.strip(".txt")
                                wenjian.append(filename)

            else:
#                 print("/n shuchu")
                diyige=a
                dierge=b
                juli=panduanci.replace("/","")
                juli=int(juli)
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
            #             print(filename)
                        cunzai=0
                        if os.path.splitext(filename)[1] == '.txt':
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if diyige in i and dierge in i:
                                    list_1=i.split(" ")
                                    if " " in diyige:
                                        list_11=diyige.split(" ")
                                        diyige=list_11[0]
                                    if diyige in list_1 and dierge in list_1:
                                        jishu_1=int(list_1.index(diyige))
                                        jishu_2=int(list_1.index(dierge))
                                        if jishu_1+juli>=jishu_2 or jishu_1-juli<=jishu_2:
                                            cunzai=1
                                            break
                            if cunzai:
                                filename=filename.strip(".txt")
                                wenjian.append(filename)
        if "&" in panduanci:
#             print("& shuchu")
            diyige=a
            dierge=b
            for parentdir, dirname, filenames in os.walk(path_1):
                for filename in filenames:
                    cunzai=0
                    if os.path.splitext(filename)[1] == '.txt':
                        with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                            u=file.read()
                            file.close()
                            u=u.replace("\n"," ")
                            juzi=u.split(".")
                        diyige_11=0
                        dierge_12=0
                        if " " in diyige:
                            list_11=diyige.split(" ")
                            diyige=list_11[0]
                        for i in juzi:
                            list_1=i.split(" ")
                            if diyige in list_1:
                                diyige_11=1
                            if dierge in list_1:
                                dierge_12=1
                        if diyige_11==1 and dierge_12==1:
                            cunzai=1
                        if cunzai:
                             filename=filename.strip(".txt")
                             wenjian.append(filename)
    return wenjian


def step_2(a,b,panduan_2,diyi_1):
    wenjian_1=[]
    if panduan_2==" ": #or
        for parentdir, dirname, filenames in os.walk(path_1):
            for filename in filenames:
                cunzai=0
                if filename in diyi_1:
                        with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                            u=file.read()
                            file.close()
                            u=u.replace("\n"," ")
                            juzi=u.split(".")
                        for i in juzi:
                            if a in i or b in i:
                                list_1=i.split("")
                                if diyige in list_1 and dierge in list_1:
                                    cunzai=1
                                    break
                        if cunzai==1:
                            break
                        if cunzai:
                            filename=filename.strip(".txt")
                            wenjian_1.append(filename)

    if "+" in panduan_2 or "/"in panduan_2 or panduan_2=="&": #+n/n+s/s&
        panduanci=panduan_2
        if "+" in panduanci:
            if "s" in panduanci:
#                 print("+s shuchu")
                diyige=a
                dierge=b
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
                        cunzai=0
                        if filename in diyi_1:
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if diyige in i:
                                    if dierge in i:
                                        print(i)
                                        list_1=i.split(" ")
                                        if diyige in list_1 and dierge in list_1:
                                            jishu_1=int(list_1.index(diyige))
                                            jishu_2=int(list_1.index(dierge,jishu_1))
                                            if jishu_1<jishu_2:
                                                cunzai=1
                                                break
                            if cunzai:
                                filename=filename.strip(".txt")
                                wenjian_1.append(filename)
            else: #+n
#                 print("+n shuchu")
                diyige=a
                dierge=b
                juli=panduanci.replace("+","")
                juli=int(juli)
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
            #             print(filename)
                        cunzai=0
                        if filename in diyi_1:
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if diyige in i and dierge in i:
                                    list_1=i.split(" ")
                                    if diyige in list_1 and dierge in list_1:
                                        jishu_1=int(list_1.index(diyige))
                                        jishu_2=int(list_1.index(dierge))
                                        if jishu_1+juli>=jishu_2:
                                            cunzai=1
                                            break
                            if cunzai:
                                filename=filename.strip(".txt")
                                wenjian_1.append(filename)
        if "/" in panduanci:
            if "s" in panduanci:
#                 print("/s shuchu")
                diyige=a
                dierge=b
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
                        cunzai=0
                        if filename in diyi_1:
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if diyige in i and dierge in i:
                                    list_1=i.split(" ")
                                    if diyige in list_1 and dierge in list_1:
                                        cunzai=1
                                        break
                            if cunzai:
                                filename=filename.strip(".txt")
                                wenjian_1.append(filename)

            else:
#                 print("/n shuchu")
                diyige=a
                dierge=b
                juli=panduanci.replace("/","")
                juli=int(juli)
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
            #             print(filename)
                        cunzai=0
                        if filename in diyi_1:
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if diyige in i and dierge in i:
                                    list_1=i.split(" ")
                                    if diyige in list_1 and dierge in list_1:
                                        jishu_1=int(list_1.index(diyige))
                                        jishu_2=int(list_1.index(dierge))
                                        if jishu_1+juli>=jishu_2 or jishu_1-juli<=jishu_2:
                                            cunzai=1
                                            break
                            if cunzai:
                                filename=filename.strip(".txt")
                                wenjian_1.append(filename)
        if "&" in panduanci:
#             print("& shuchu")
            diyige=a
            dierge=b
            for parentdir, dirname, filenames in os.walk(path_1):
                for filename in filenames:
                    cunzai=0
                    if filename in diyi_1:
                        with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                            u=file.read()
                            file.close()
                            u=u.replace("\n"," ")
                            juzi=u.split(".")
                        diyige_21=0
                        dierge_22=0
                        for i in juzi:
                            list_1=i.split(" ")
                            if diyige in list_1:
                                diyige_21=1
                            if dierge in list_1:
                                dierge_22=1
                        if diyige_21==1 and dierge_22==1:
                            cunzai=1
                        if cunzai:
                            filename=filename.strip(".txt")
                            wenjian_1.append(filename)
    return wenjian_1
    
def step_3(a,b,panduan_2,diyi_1):
    wenjian_2=[]
    if panduan_2==" ": #or
        for parentdir, dirname, filenames in os.walk(path_1):
            for filename in filenames:
                cunzai=0
                if filename in diyi_1:
                        with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                            u=file.read()
                            file.close()
                            u=u.replace("\n"," ")
                            juzi=u.split(".")
                        for i in juzi:
                            list_1=i.split(" ")
                            if a in i or b in list_1:
                                cunzai=1
                                break
                        if cunzai==1:
                            break
                        if cunzai:
                            filename=filename.strip(".txt")
                            wenjian_2.append(filename)

    if "+" in panduan_2 or "/"in panduan_2 or panduan_2=="&": #+n/n+s/s&
        panduanci=panduan_2
        if "+" in panduanci:
            if "s" in panduanci:
#                 print("+s shuchu")
                diyige=a
                dierge=b
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
                        cunzai=0
                        if filename in diyi_1:
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if diyige in i:
                                    if dierge in i:
                                        print(i)
                                        list_1=i.split(" ")
                                        if diyige in list_1 and dierge in list_1:
                                            jishu_1=int(list_1.index(diyige))
                                            jishu_2=int(list_1.index(dierge,jishu_1))
                                            if jishu_1<jishu_2:
                                                cunzai=1
                                                break
                            if cunzai:
                                filename=filename.strip(".txt")
                                wenjian_2.append(filename)
            else: #+n
#                 print("+n shuchu")
                diyige=a
                dierge=b
                juli=panduanci.replace("+","")
                juli=int(juli)
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
            #             print(filename)
                        cunzai=0
                        if filename in diyi_1:
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if diyige in i and dierge in i:
                                    list_1=i.split(" ")
                                    if diyige in list_1 and dierge in list_1:
                                        jishu_1=int(list_1.index(diyige))
                                        jishu_2=int(list_1.index(dierge))
                                        if jishu_1+juli>=jishu_2:
                                            cunzai=1
                                            break
                            if cunzai:
                                filename=filename.strip(".txt")
                                wenjian_2.append(filename)
        if "/" in panduanci:
            if "s" in panduanci:
#                 print("/s shuchu")
                diyige=a
                dierge=b
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
                        cunzai=0
                        if filename in diyi_1:
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                list_1=i.split(" ")
                                if diyige in list_1 and dierge in list_1:
                                    cunzai=1
                                    break
                            if cunzai:
                                filename=filename.strip(".txt")
                                wenjian_2.append(filename)

            else:
#                 print("/n shuchu")
                diyige=a
                dierge=b
                juli=panduanci.replace("/","")
                juli=int(juli)
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
            #             print(filename)
                        cunzai=0
                        if filename in diyi_1:
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if diyige in i and dierge in i:
                                    list_1=i.split(" ")
                                    if diyige in list_1 and dierge in list_1:
                                        jishu_1=int(list_1.index(diyige))
                                        jishu_2=int(list_1.index(dierge))
                                        if jishu_1+juli>=jishu_2 or jishu_1-juli<=jishu_2:
                                            cunzai=1
                                            break
                            if cunzai:
                                filename=filename.strip(".txt")
                                wenjian_2.append(filename)
        if "&" in panduanci:
#             print("& shuchu")
            diyige=a
            dierge=b
            for parentdir, dirname, filenames in os.walk(path_1):
                for filename in filenames:
                    cunzai=0
                    if filename in diyi_1:
                        with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                            u=file.read()
                            file.close()
                            u=u.replace("\n"," ")
                            juzi=u.split(".")
                        diyige_31=0
                        dierge_32=0
                        for i in juzi:
                            list_1=i.split(" ")
                            if diyige in list_1:
                                diyige_31=1
                            if dierge in list_1:
                                dierge_32=1
                        if diyige_31==1 and dierge_32==1:
                            cunzai=1
                        if cunzai:
                            filename=filename.strip(".txt")
                            wenjian_2.append(filename)
    return wenjian_2


while True:
    try:
        chaxun=input()
        chaxun=chaxun.lower()
        chaxun=chaxun.replace("(","")
        chaxun=chaxun.replace(")","")
        teshu=0
        kongge=0
        for i in chaxun:
            if i=="/" or i=="&" or i=="+":
                teshu+=1
        for i in chaxun:
            if i==" ":
                kongge+=1
        if (teshu==1 and kongge%2==0)or teshu==0:
    #         print("danyi")
            chaxun_n=2
            kongge_n=0
            for i in chaxun:
                if i=="\"":
                    chaxun_n+=1
                if chaxun_n%2==0:
                    if i==" ":
                        kongge_n+=1
            if chaxun[0]=="\"" and chaxun[-1]=="\"" and chaxun_n==4:
                chaxun=chaxun.replace("\"","")
                list_111=[]
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
            #             print(filename)
                        cunzai=0
                        if os.path.splitext(filename)[1] == '.txt':
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                if chaxun in i:
                                    cunzai=1
                                    break
                            if cunzai:
                                jieguo=filename.strip(".txt")
                                jieguo=int(jieguo)
                                list_111.append(jieguo)
                list_1111=sorted(list_111)
                for i in list_1111:
                    print(i)
            if kongge_n==0: #single
                list_111=[]
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
            #             print(filename)
                        cunzai=0
                        if os.path.splitext(filename)[1] == '.txt':
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for i in juzi:
                                list_1=i.split(" ")
                                if chaxun in list_1:
                                    cunzai=1
                                    break
                            if cunzai:
                                jieguo=filename.strip(".txt")
                                jieguo=int(jieguo)
                                list_111.append(jieguo)
                list_1111=sorted(list_111)
                for i in list_1111:
                    print(i)
            if kongge_n==1: #or
                list_111=[]
                chaxun_o=chaxun.split(" ")
                for parentdir, dirname, filenames in os.walk(path_1):
                    for filename in filenames:
            #             print(filename)
                        cunzai=0
                        if os.path.splitext(filename)[1] == '.txt':
                            with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                u=file.read()
                                file.close()
                                u=u.replace("\n"," ")
                                juzi=u.split(".")
                            for danci in chaxun_o:
                                for i in juzi:
                                    list_1=i.split(" ")
                                    if danci in list_1:
                                        cunzai=1
                                        break
                                if cunzai==1:
                                    break
                            if cunzai:
                                jieguo=filename.strip(".txt")
                                jieguo=int(jieguo)
                                list_111.append(jieguo)
                list_1111=sorted(list_111)
                for i in list_1111:
                    print(i)

            if kongge_n==2: #+n/n+s/s&
                chaxun_o=chaxun.split(" ")
                panduanci=chaxun_o[1]
                if "+" in panduanci:
                    if "s" in panduanci:
    #                    print("+s shuchu")
                        list_111=[]
                        diyige=chaxun_o[0]
                        dierge=chaxun_o[2]
                        for parentdir, dirname, filenames in os.walk(path_1):
                            for filename in filenames:
                    #             print(filename)
                                cunzai=0
                                if os.path.splitext(filename)[1] == '.txt':
                                    with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                        u=file.read()
                                        file.close()
                                        u=u.replace("\n"," ")
                                        juzi=u.split(".")
                                    for i in juzi:
                                        if diyige in i:
                                            if dierge in i:
    #                                                print(i)
                                                list_1=i.split(" ")
                                                if diyige in list_1 and dierge in list_1:
                                                    jishu_1=int(list_1.index(diyige))
                                                    jishu_2=int(list_1.index(dierge))
                                                    if jishu_1<jishu_2:
                                                        cunzai=1
                                                        break
                                    if cunzai:
                                        jieguo=filename.strip(".txt")
                                        jieguo=int(jieguo)
                                        list_111.append(jieguo)
                        list_1111=sorted(list_111)
                        for i in list_1111:
                            print(i)
                    else: #+n
    #                    print("+n shuchu")
                        diyige=chaxun_o[0]
                        dierge=chaxun_o[2]
                        juli=panduanci.replace("+","")
                        juli=int(juli)
                        list_111=[]
                        for parentdir, dirname, filenames in os.walk(path_1):
                            for filename in filenames:
                                cunzai=0
                                if os.path.splitext(filename)[1] == '.txt':
                                    with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                        u=file.read()
                                        file.close()
                                        u=u.replace("\n"," ")
                                        juzi=u.split(".")
                                    for i in juzi:
                                        if diyige in i and dierge in i:
                                            list_1=i.split(" ")
                                            if diyige in list_1 and dierge in list_1:
                                                jishu_1=int(list_1.index(diyige))
                                                jishu_2=int(list_1.index(dierge))
                                                if jishu_1+juli>=jishu_2:
                                                    cunzai=1
                                                    break
                                    if cunzai:
                                        jieguo=filename.strip(".txt")
                                        jieguo=int(jieguo)
                                        list_111.append(jieguo)
                        list_1111=sorted(list_111)
                        for i in list_1111:
                            print(i)
                if "/" in panduanci:
                    chaxun_o=chaxun.split(" ")
                    panduanci=chaxun_o[1]
                    if "s" in panduanci:
    #                    print("/s shuchu")
                        diyige=chaxun_o[0]
                        dierge=chaxun_o[2]
                        list_111=[]
                        for parentdir, dirname, filenames in os.walk(path_1):
                            for filename in filenames:
                                cunzai=0
                                if os.path.splitext(filename)[1] == '.txt':
                                    with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                        u=file.read()
                                        file.close()
                                        u=u.replace("\n"," ")
                                        juzi=u.split(".")
                                    for i in juzi:
                                        list_1=i.split(" ")
                                        if diyige in list_1 and dierge in list_1:
                                            cunzai=1
                                            break
                                    if cunzai:
                                        jieguo=filename.strip(".txt")
                                        jieguo=int(jieguo)
                                        list_111.append(jieguo)
                        list_1111=sorted(list_111)
                        for i in list_1111:
                            print(i)

                    else:
    #                    print("/n shuchu")
                        diyige=chaxun_o[0]
                        dierge=chaxun_o[2]
                        juli=panduanci.replace("/","")
                        juli=int(juli)
                        list_111=[]
                        for parentdir, dirname, filenames in os.walk(path_1):
                            for filename in filenames:
                    #             print(filename)
                                cunzai=0
                                if os.path.splitext(filename)[1] == '.txt':
                                    with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                        u=file.read()
                                        file.close()
                                        u=u.replace("\n"," ")
                                        juzi=u.split(".")
                                    for i in juzi:
                                        if diyige in i:
                                            list_1=i.split(" ")
                                            if diyige in list_1 and dierge in list_1:
                                                jishu_1=int(list_1.index(diyige))
                                                jishu_2=int(list_1.index(dierge))
                                                if jishu_1+juli>=jishu_2 or jishu_1-juli<=jishu_2:
                                                    cunzai=1
                                                    break
                                    if cunzai:
                                        jieguo=filename.strip(".txt")
                                        jieguo=int(jieguo)
                                        list_111.append(jieguo)
                        list_1111=sorted(list_111)
                        for i in list_1111:
                            print(i)
                if "&" in panduanci:
    #                print("& shuchu")
                    diyige=chaxun_o[0]
                    dierge=chaxun_o[2]
                    list_111=[]
                    for parentdir, dirname, filenames in os.walk(path_1):
                        for filename in filenames:
        #                     print(filename)
                            cunzai=0
                            if os.path.splitext(filename)[1] == '.txt':
                                with open(path_1+'/'+filename,'r',encoding='utf-8') as file:
                                    u=file.read()
                                    file.close()
                                    u=u.replace("\n"," ")
                                    juzi=u.split(".")
                                diyige_1=0
                                dierge_2=0
                                for i in juzi:
    #                                print(i)
                                    list_1=i.split(" ")
                                    if diyige in list_1:
                                        diyige_1=1
                                    if dierge in list_1:
                                        dierge_2=1
                                if diyige_1==1 and dierge_2==1:
                                    cunzai=1
                                if cunzai:
                                    jieguo=filename.strip(".txt")
                                    jieguo=int(jieguo)
                                    list_111.append(jieguo)
                    list_1111=sorted(list_111)
                    for i in list_1111:
                        print(i)
            if len(list_1111)==0:
                print("Format Error or No File")
        else: #chaxun=a /n b /s c or chaxun="a b" & c or c & "a b "
            if "\"" in chaxun:
                if chaxun[0]=="\"": #"a b" & c
    #                 print(1111)
                    chaxun=chaxun.replace("\"","") #a b /n c
                    chaxun_1=chaxun.split(" ")
                    a=chaxun_1[0]
                    b=chaxun_1[1]
                    panduan_3=chaxun_1[2]
                    c=chaxun_1[3]
                    d=a+" "+b
                    chaxun_1=chaxun.split(" ")
                    diyi_1=step_1(d,panduan_3,c)
                    diyi_11=sorted(diyi_1)
                    zuiz_z=[]
                    for i in diyi_11:
                        m=i.strip(".txt")
                        n=int(m)
                        zuiz_z.append(n)
                    zuiz_z.sort()
                    for i in zuiz_z:
                        print(i)
                else:
    #                 print(111)
                    chaxun=chaxun.replace("\"","") #c & "a b" & c
                    chaxun_1=chaxun.split(" ")
                    a=chaxun_1[2]
                    b=chaxun_1[3]
                    panduan_3=chaxun_1[1]
                    c=chaxun_1[0]
                    d=a+" "+b
                    chaxun_1=chaxun.split(" ")
                    diyi_1=step_1(d,panduan_3,c)
                    diyi_11=sorted(diyi_1)
                    zuiz_z=[]
                    for i in diyi_11:
                        m=i.strip(".txt")
                        n=int(m)
                        zuiz_z.append(n)
                    zuiz_z.sort()
                    for i in zuiz_z:
                        print(i)
            elif teshu==2: #chaxun=a /n b /s c
                list_2=chaxun.split(" ")
                a=list_2[0]
                b=list_2[2]
                panduan_1=list_2[1]
                panduan_2=list_2[3]
                c=list_2[4]
                diyi_1=step_1(a,panduan_1,b)
                list_s=[]
                for i in diyi_1:
                    n=i+".txt"
                    list_s.append(n)
                jieguo_1=step_2(a,c,panduan_2,list_s)
                jieguo_2=step_3(b,c,panduan_2,list_s)
                jieguo_z=sorted(jieguo_1+jieguo_2)
                jieguo_zz=set(jieguo_z)
                zuiz_z=[]
                for i in jieguo_zz:
                    m=i.strip(".txt")
                    n=int(m)
                    zuiz_z.append(n)
                zuiz_z.sort()
                for i in zuiz_z:
                    print(i)
            else:#a b & c or c & a b
                chaxun_2=chaxun.split(" ")
                panduanfu=["/","+","&"]
                panduanfu_1=0
                for i in panduanfu:
                    if i in chaxun_2[2]:
                        panduanfu_1=1
                if panduanfu_1==1: #a b & c
                    a=chaxun_2[0]
                    b=chaxun_2[1]
                    c=chaxun_2[3]
                    panduan_3=chaxun_2[2]
                    jieguo_1=step_1(a,panduan_3,c)
                    jieguo_2=step_1(b,panduan_3,c)
                    jieguo_z=set(jieguo_1+jieguo_2)
                    jieguo_zz=list(jieguo_z)
                    zuiz_z=[]
                    for i in jieguo_zz:
                        m=i.strip(".txt")
                        n=int(m)
                        zuiz_z.append(n)
                    zuiz_z.sort()
                    for i in zuiz_z:
                        print(i)
                        
                else: #a & b c
                    c=chaxun_2[0]
                    panduan_3=chaxun_2[1]
                    a=chaxun_2[2]
                    b=chaxun_2[3]
                    jieguo_1=step_1(a,panduan_3,c)
                    jieguo_2=step_1(b,panduan_3,c)
                    jieguo_z=sorted(jieguo_1+jieguo_2)
                    jieguo_zz=set(jieguo_z)
                    zuiz_z=[]
                    for i in jieguo_zz:
                        m=i.strip(".txt")
                        n=int(m)
                        zuiz_z.append(n)
                    zuiz_z.sort()
                    for i in zuiz_z:
                        print(i)
            if len(zuiz_z)==0:
                print("Format Error or No File")
    except EOFError:
        break
