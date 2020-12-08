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
