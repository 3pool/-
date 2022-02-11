# 二、输出1+2+3+…+n=m，其中m是最接近100，且小于100的整数
m = 1
for n in range(2,100):
    m += n
    if m >= 100:
        break
print('1+2+3+...+%d=%d'%(n-1,m-n))


