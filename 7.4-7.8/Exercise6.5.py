#coding:gb2312
#�ֵ�-Ƕ��ѧϰ
#Ƕ�ף���һϵ���ֵ�洢���б��У����б���Ϊֵ�洢���ֵ��С�

#1.���ֵ�洢���б���
alien_0={'color':'green','points':'5',}
alien_1={'color':'red','points':'10'}
alien_2={'color':'yeloow','points':'15'}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)
	
#��ϰ
aliens=[]       #����һ���洢�����˵Ŀ��б�
for alien_number in range(30):  #�ظ�ѭ��30��
	new_alien = {'color':'green','points':'5','speed':'slow'}  #ÿѭ��һ�ζ�����һ�������ˣ���Щ����������һ��
	aliens.append(new_alien)          #����������������ӵ��б�ĩβ
for alien in aliens[:5]:     #ʹ����Ƭ���б��������ӡǰ���������
	print(alien)
print("********")
print("һ����"+str(len(aliens))+"��������"+".")  #��len()��ӡ�б��ȣ�˵�������˶��ٸ�������

