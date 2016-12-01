import sys

n = 3
m = 5
mode = "dir"
index = 0

def write(w,x):
	global index
	if x>m: return
	if mode == "undir":
		if ((x+1)%3==m%3) or (m%3!=2 and x==0):
			print ("  "*x) + str(w)
			index = index + 1
	elif mode == "dir":
		if (x+1)%2==m%2 or x==0:
			print ("  "*x) + str(w)
			index = index + 1
	else:
		print (("  "*x) + str(w))
		index = index + 1
	w.pop(0)
	w.append(0)
	for i in range(n):
		if x==0 and i==0: continue
		w[len(w)-1]=i
		write(list(w),x+1)

if len(sys.argv)<4:
	print "Hasznalat: domset.exe n (= szimbolumok szama) m (= szo hossza) iranyitottsag: {dir, undir, all}"
	print "Futtatas alapertelemezett ertekekre: 3 5 dir"
else:
	n=int(sys.argv[1])
	m=int(sys.argv[2])
	mode=(sys.argv[3])

write(m*[0],0)
print "A dominalo elemek szama: " + str(index)