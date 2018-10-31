x=[[1],[1],[1]]
w=[[-1],[-3],[2]]
t=[[1]]
lr=0.3

def y_in(x,w):
	return x*w

def sign(val):
	if val<0:
		return 0
	else:
		return 1
def SSE(val):
	val=(t[0][0]-val)**2
	if(val>0.1):
		return True
	else:
		return False

def updateBobot(S):
	global w
	for i in range(0,len(x)):
		for j in range(0,len(x[0])):
			w[i][j]=round(w[i][j]+(x[i][j]*lr*(t[0][0]-S)),6)
	
def S():
	Sj=0
	for i in range(0,len(x)):
		for j in range(0,len(x[0])):
			Sj+=y_in(x[i][j],w[i][j])
	return sign(Sj)

def hitung():
	i=0
	Sj=S()
	while SSE(Sj)==True:
		print(f'->IT[{i}] perubahan bobot\n')
		print("b = ",w[0][0])
		print("w1 = ",w[1][0])
		print("w2 = ",w[2][0])
		updateBobot(Sj)
		Sj=S()
		i+=1

	
print("\n# Aplikasi perceptron #\n ")
hitung()
print("sedang memproses ....")
print("\n->data hasil perceptron : ")
print("b akhir = ",w[0][0])
print("w1 akhir = ",w[1][0])
print("w2 akhir = ",w[2][0])