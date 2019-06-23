from functools import reduce
import re

CN_UNIT = {
    '个' : 1,
    '元' : 1,
    '圆' : 1,
    '十' : 10,
    '拾' : 10,
    '百' : 100,
    '佰' : 100,
    '千' : 1000,
    '仟' : 1000,
    '万' : 10000,
    '萬' : 10000,
    '亿' : 100000000,
    '億' : 100000000,
    '兆' : 1000000000000,
}


intab = '零一二三四五六七八九壹贰叁肆伍陆柒捌玖'
outtab ='0123456789123456789'
def convertDigit(string):
    transtab = str.maketrans(intab,outtab,'零')
    string = string.translate(transtab)
    lt = list(reversed(re.split(r'[亿万]',string))) #以亿、万为单位作第一次切分
    lt = [('0' if lt[i]=='' else lt[i]) for i in range(len(lt))] #如果lt中某一项为空则补0
    lt = [(lt[i]+'个' if lt[i][-1].isdigit() else lt[i]) for i in range(len(lt))] #如果lt中某一项以数字结尾则补个

    res = []
    for i in range(len(lt)):
        patten=re.compile(r'\d?[\u4E00-\u9FA5]')
        l = re.findall(patten,lt[i]) #将string按照“数值+单位”切分
        l = [(l[j] if len(l[j])==2 else 1+l[i]) for j in range(len(l))] #如果l中某一项只有单位则在前面补1
        l = [int(l[k][0])*CN_UNIT.get(y) for k in range(len(l)) for y in l[k] if y in CN_UNIT] #将单位换算为数值
        m = reduce(lambda x,y:x+y,l)
        res.append(m)

    res =[ res[i]*(10000**i) for i in range(len(res))]
    result = reduce(lambda x,y:x+y,res)
    return result

while True:
    string = input('请输入需要转换的大写整数数字，空格退出：').strip()
    if not string:
        break
    print(convertDigit(string))
