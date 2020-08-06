import sqlite3
import os

def add():
	v=[]
	ans = []
	v1=[]
	with open('list_b.txt','r') as input_str:
		t = input_str.read()
		
		v = t.split('\n')
		with open('not.txt','r') as ex:
			t1 = ex.read()
			v1 = t1.split(',')
			for i in v:
				if i in v1:
					v.remove(i)
			v.remove('1.51')
			v.remove('1.56')
			v.remove('3.226')
			v.remove('5.28')
			v.remove('5.34')
			v.remove('')
			v.remove('6.14')
	return v


v = add()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite3")
conn = sqlite3.connect(db_path)
with conn:
	cursor = conn.cursor()
	sql = 'INSERT INTO Main_zadachi VALUES(?,?,?,?,?,?,?)'
	t=4
	for i in v:
		cursor.execute(sql,(t,'70%','='+i+'=','-------','Belolip','Б'+i,'@'+i+'@'))
		t+=1
		print(i)
		
	
print(len(v))