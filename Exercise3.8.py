#coding:gb2312
#��֯�б�sort()��sorted()���б��������
attractions=['Nine-village Valley','Suzhou Gardens','Tian anmen Square','Summer Palace','Palace of Heavenly Purity']#��կ��������԰�֣��찲�ţ��ú�԰��Ǭ�幬
print("�б�ԭʼ˳��")
print(attractions)
print("��ʱ����ĸ˳�� ")
print(sorted(attractions))
print(attractions)#��ʵ�б�˳��δ�����仯
print("��ʱ����ĸ˳���෴")
print(sorted(attractions,reverse=True))
print(attractions)#sorted()�Ƕ��б������ʱ�����б�ԭ����˳�򲻻ᷢ���仯
attractions.reverse()#�ѵ�ǰ�б�˳����з�ת
print(attractions)
attractions.reverse()#�ٴη�ת���ص�ԭ���б�˳��
print(attractions)
print("���ð���ĸ˳��")
attractions.sort()
print(attractions)#sort()���б�����������޸�
print("��������ĸ˳���෴��")
attractions.sort(reverse=True)
print(attractions)
print("һ������ȥ�����ط���")
print(len(attractions))
