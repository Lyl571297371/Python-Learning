#coding:gb2312
#�ֵ��ѧϰ1 
print("�ֵ�ֵ�ķ��ʺ�ʹ�ã�\n")
alien_0 = {'color':'green','points':'5'} #�ֵ��÷��ڻ�����{}�е�һϵ�м�-ֵ�Ա�ʾ�����Խ��κ�python���������ֵ��ֵ
print("�����ɱ��������ɫΪ��"+alien_0['color'])       
#new_points=alien_0['points']            #���ֵ��ȡ��point�������ֵ�����䴢�浽�µı���new_points��
print("��һ�÷���: "+alien_0['points'])     #Ҫ�����ֵ�ֻ��Ҫָ���ֵ����ͷ������ڵļ�


#��Ӽ�-ֵ��
print("\n\n�ֵ���Ӽ�-ֵ�ԣ�\n")
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=250
print(alien_0)      #��-ֵ�Ե�����˳�������˳��ͬ��python�����ļ�-ֵ�Ե����˳��ֻ���ļ���ֵ֮��Ĺ�����ϵ


#�ֵ���޸�
#����1
print("\n\n����1���ֵ���޸�")            #�������޸�
alien_1={}
alien_1['color']='red'
alien_1['points']=10
alien_1['x_position']=50
alien_1['y_position']=300
print("ԭʼ�ֵ��ǣ�")
print(alien_1)
alien_1['color']='yellow'
print("�޸ĺ����������ɫ�����ǣ� "+alien_1['color']+".")
print("���ڵ��ֵ��ǣ�")
print(alien_1)           

#����2
print("\n\n����2���ֵ���޸�")
alien_2={'x_position':0,'y_position':25,'speed':'slow'}
print("Original x_position: "+str(alien_2['x_position']))  #�����б���һ�ٱ�str()
if alien_2['speed']=='slow':
	x_increment = 1 
elif alien_2['speed']=='medium':
	x_increment = 2
else:
	x_increment = 3
alien_2['x_position']=alien_2['x_position']+x_increment
print("Now x_position is: "+str(alien_2['x_position']))

#�ֵ�ļ�-ֵ��ɾ��
print("\n\n�ֵ��ɾ����")
print("\nԭʼ�ֵ���:")
print(alien_1)
print("\nɾ����ɫ�ͷ�������ֵ�:")
del alien_1['color']
del alien_1['points']     #ɾ���ļ�-ֵ������Զɾ��
print(alien_1)

#�����ƶ�����ɵ��ֵ�
languages={
	'lyl':'python',
	'ljy':'go',
	'cys':'R',
	}
print("\n\nLjy's favorite language is "+languages['ljy'].title()+".")
