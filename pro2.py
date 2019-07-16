import sys, string, math
def reduceN( a, k) :
	if k <= 0 : return a

	if a == 0 : return 10	# Fail
	p1 = reduceN(a//10, k)*10 + a%10
	p2 = reduceN(a//10, k-1)
	if p1 < p2 :
		return p1
	else :
		return p2

a,k = input().split()
a,k = int(a),int(k)
print(reduceN(a,k))
