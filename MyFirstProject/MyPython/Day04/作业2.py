grades={'jane':[('INFO303',3.00),('INFO201',2.75),('MGMT375',3.75),('MGMT555',3.50), ('MKT325',2.75),('MGMT325','WD'),('MGMT313',3.5),('MGMT551',2.00)],'sally':[('FIN360',3.75),('INFO302',3.00),('MGMT325',4.00),('MGMT450',3.50), ('MGMT331',4.00),('MKT325',2.75),('FIN325',3.25),('MGMT313','WD'),('MGMT325','I'),('INFO303',2.75),('MGMT391',3.25),('MGMT319','WD'), ('MGMT561',3.25)],'tom':[('INFO301',3.75),('INFO201',3.50),('MGMT375',3.75),('INFO303',3.75), ('MKT325',2.75),('MGMT325','WD'),('MGMT313',3.5),('MGMT551',2.00), ('INFO302',3.25)]}

def cal_avg_mgmt():
        num = 0
        sum = 0
        for i in grades.keys():
                for j in grades[i]:
                        if j[0][0:4] == 'MGMT' and isinstance(j[1],float):
                                sum += j[1]
                                num += 1
        avg = sum/num
        print(round(avg,2))

cal_avg_mgmt()


