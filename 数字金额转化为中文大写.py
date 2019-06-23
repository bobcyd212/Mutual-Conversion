import time
import re
def convert(num):
    dec_label = ['角', '分','厘']
    units =['', '拾', '佰', '仟', '万', '拾','佰','千','亿','拾','百','千','兆']
    transtab = str.maketrans('0123456789','零壹贰叁肆伍陆柒捌玖')

    if len(num) == 2:  #如果有小数部分
        decp,intp = num[1].translate(transtab),num[0][::-1].translate(transtab)
        dec_part = [(decp[i] if decp[i]!='零'else'') +(dec_label[i] if decp[i]!='零'else'') for i in range(len(decp))]#如果小数部分有零则数字和单位都要忽略
        int_part = [intp[i] +(units[i] if intp[i]!='零'else'') for i in range(len(intp))]#如果整数部分有零则单位忽略
        dec_tmp = ''.join(dec_part).rstrip('零')
        int_tmp = ''.join(reversed(int_part)).replace('零零零', '零').replace('零零', '零')
        result = '人民币'+dec_tmp if num[0] == '0' else '人民币'+int_tmp+dec_tmp if int_tmp.endswith('零') else '人民币'+int_tmp+'圆'+dec_tmp #整数部分是0则直接输出小数部分
    else:
        intp = num[0][::-1].translate(transtab)
        int_part = [intp[i] +(units[i] if intp[i]!='零'else'') for i in range(len(intp))]
        int_tmp = ''.join(reversed(int_part))
        int_tmp = int_tmp.rstrip('零').replace('零零零', '零').replace('零零', '零')
        result = '人民币'+int_tmp+'圆' 
    return result

while True:
    num = input('请输入要转化的金额，空格退出:').strip()
    verify = re.findall(r'[^\.\d]',num) #检查输入内容是否有数字或者'.'以外的字符
    if verify:
        print('有非法字符重新输入')
        continue
    n= num.split('.')
    if len(n) == 1 and n[0] == '':
        print('感谢使用!')
        break
    if len(n) == 2 and len(n[1])>2: #人民币最小到角
        print('小数点后只能两位!')
        continue
    
    a = convert(n)
    print(a)
