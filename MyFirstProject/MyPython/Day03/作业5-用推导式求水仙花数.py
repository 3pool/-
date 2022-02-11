# 五、用推导式求水仙花数（所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。）
list1 = [num for num in range(100,1000) if (num//100)**3+((num%100)//10)**3+(num%10)**3 == num]
print(list1)