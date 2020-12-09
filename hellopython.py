import itertools
##pyhton 中可随时修改变量的值 但是python始终记录最新的值
##python 运行发生错误时 会提供一个traceback 来指出发生错误的地方

if __name__ == "__main__":
    print("hello ,python!")
#**题目:**有四个数字:1、2、3、4，能组成多少个互不相同且无重复数字的三位数?各是多少?
numberlist=[1,2,3,4]
total =0
for i in numberlist:
    for j in numberlist:
        for k in numberlist:
            if((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k)
                total+=1
print (total)
## 使用itertools  的permutations即可
for i in itertools.permutations(numberlist,3):
    print(i)
##题目:**企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提 10%;
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元 的部分，可提成7.5%;
# 20万到40万之间时，高于20万元的部分，可提成5%;
# 40万到 60万之间时高于40万元的部分，可提成3%;
# 60万到100万之间时，高于60万元的部 分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月 利润I，求应发放奖金总数?
##profit=int(input('show me your money:'))
profit=100
commision=0
saliarylist =[100000,100000,200000,200000,400000]
commisionrate =[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(saliarylist)):
    if profit<=saliarylist[i]:
        commision+=profit*commisionrate[i]
        profit =0
        break
    else:
        commision +=saliarylist[i]*commisionrate[i]
        profit-=saliarylist[i]
commision+=profit*commisionrate[-1]
print(commision)
##一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少?
n=0
while (n+1)**2 -n*n<=168:
    n+=1
print(n+1)

##输入某年某月某日，判断这一天是这一年的第几天?
'''
def isLeapYear(y):
    return (y%400==0 or (y%4==0 and y%100!=0))
DofM=[0,31,28,31,30,31,30,31,31,30,31,30] 
res=0
year=int(input('Year:')) 
month=int(input('Month:')) 
day=int(input('day:'))
if isLeapYear(year): 
    DofM[2]+=1
for i in range(month): 
    res+=DofM[i]
print(res+day)
'''
## 排序 sorted 函数
sortlist =[1,3,5,6,3,7,21,78,32,45,56,44,66,78,90,21]
strtest='qwer1234'
print(sorted(sortlist))
print(''.join(reversed(strtest)))

##斐波那契数列
'''
target=int(input())
a,b=1,1
for i in range(target-1):
    a,b=b,a+b
print(a)
'''

## copy 函数
import copy
a = [1,2,3,4,['a','b']]

b = a					# 赋值
c = a[:]				# 浅拷贝
d = copy.copy(a)		# 浅拷贝
e = copy.deepcopy(a)	# 深拷贝

a.append(5)
a[4].append('c')

print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)
print('e=',e)

##实例：九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2ld '%(i,j,i*j),end='')
    print()

##实例：暂停一秒输出
import time
for i in range(4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)