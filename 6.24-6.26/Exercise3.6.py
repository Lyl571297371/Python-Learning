#coding:gb2312
#��3.5����Ļ����ϣ���insert���һ����������ͬλ�ã�append���һ����ĩβ����ӡ��Ϣ�������롣
names=[]
#print(names)
names.append('lyl')
names.append('cys')
#print(names)
names.insert(0,'hl')
names.insert(1,'fjy')
#print(names)               #����Printȥ��ע�ͷ��ſ�����ȷ�۲쵽�б�ӿյ��洢��ǰ��ı仯
message=", "+"Would You Like To Have Dinner With Me"+"?"
print(names[0].title()+message)
print(names[1].title()+message)
print(names[2].title()+message)
print(names[-1].title()+message)
