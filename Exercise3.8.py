#coding:gb2312
#组织列表，sort()和sorted()对列表进行排序
attractions=['Nine-village Valley','Suzhou Gardens','Tian anmen Square','Summer Palace','Palace of Heavenly Purity']#九寨沟，苏州园林，天安门，颐和园，乾清宫
print("列表原始顺序：")
print(attractions)
print("临时按字母顺序： ")
print(sorted(attractions))
print(attractions)#核实列表顺序未发生变化
print("临时与字母顺序相反")
print(sorted(attractions,reverse=True))
print(attractions)#sorted()是对列表进行临时排序，列表原来的顺序不会发生变化
attractions.reverse()#把当前列表顺序进行反转
print(attractions)
attractions.reverse()#再次反转即回到原来列表顺序
print(attractions)
print("永久按字母顺序：")
attractions.sort()
print(attractions)#sort()对列表进行永久性修改
print("永久与字母顺序相反：")
attractions.sort(reverse=True)
print(attractions)
print("一共打算去几个地方？")
print(len(attractions))
