#prase the aricle in the txt
import re
def prase(filename):
    sourse=[]
    #another way to solve this problem
    # with open(filename,'r') as f:
    #     lines=f.readlines()
    #     for line in lines:
    #         words=line.split(" ")
    #         for word in words:
    #             if word.isalpha():
    #                 sourse.append(word)
    with open(filename, 'r') as f:
        data=f.read()
        combineWord = re.findall(r"([\w]+)-([\w]+)", data)
        # print(len(combineWord))
        # while re.search(r"([\w]+)-([\w])+", data) is not None:
        #     combineWord = re.search(r"([\w]+)-([\w])+", data)
        #     data.replace(combineWord.group(),'')
        #     print(combineWord.group())
        index = 0
        while index <len(combineWord):
            sourse.append(str(combineWord[index][0])+'-'+str(combineWord[index][1]))
            index=index+1
        newData=re.sub(r"([\w]+)-([\w])+", "", data)
        words=re.split("[^\w]",newData)
        for word in words:
            if word is not '':
               sourse.append(word)
    f.close()
    print(sourse)
    return sourse

def wordCount(sourse):
    result={}
    for word in sourse:
        result[word]=sourse.count(word)
    print(result)

