#coding:gb2312
#ϰ��1
print("ϰ��1��")
def make_shirt(size,logo):
	print("�ù˿Ͷ��Ƶ�T�������ǣ�"+size+".")
	print("�ù˿�T��Ҫ�����ʽ�ǣ�"+logo+"."+"\n\n")
make_shirt('M','pure white')   #λ��ʵ�ε��ú���
make_shirt(logo='pure blank',size='L')  #�ؼ��ֵ��ú���


#ϰ��2
print("\n\nϰ��2:")
def make_shirt(size,logo='i love python'):
	print("�ù˿Ͷ��Ƶ�T��Ҫ���ǣ�")
	print("size:"+size+"  logo:"+logo+"\n\n")
make_shirt('M')
make_shirt('L')
make_shirt('XL','ADC')


#ϰ��3
print("\n\nϰ��3:")
def describe_city(name,country='China'):
	 print(name.title()+" belongs to "+country+".")
describe_city('Yanan')
describe_city('Beijing')
describe_city('Newyork','American')
