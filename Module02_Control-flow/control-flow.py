#### https://www.trprt.io/python-practice-problems-ifs-loops-control-flow
b = [".", "10", " ", " "]
v = "10"
if "o" not in v:
	c = [2, 1] + [int(v)/10] + [2, int(v)/10]*2
	v += b[0][:-1] + ","
else:
	a = ["200"] + b
	v = "10" + a[0]
v += "." + b.pop(1)[:5]
print(type(v))
### str v is 10,.10

x = "mary"
val = ["ann", "pat", "mary", "ann"]
if val[-1] != x:
	a = [len(val), len(val[-1])] + [len(val[-2])]
	x = "," + val[len(val)//2+1][0]
else:
	z = ["bob"*2, val[len(val)%3][1:]] + val
	val.sort()
x += "bob" + val[0]
print(x)

e = [",", ".", ",", ","]
b = [7, 1]
if len(e[-1]) >= b[-1]:
	b.sort()
b.append(5)
print(b[2]) 

a = "800"
x = ["800", ".", " "]
if "a" not in a:
	a += x.pop(-2).upper() + "90"
elif a.isalpha():
	a = "90" + x.pop(1)[0]*3
else:
	x[len(x)//4+1] = x[1]*2 + ","
x.insert(2, a.replace("0", "1000"))
print(len(x))

v = 1
e = [2, 8]
if e[-2] >= v:
	v += e[len(e)//2]+4
elif v < e[-1]:
	v = v-1
v += e[0]+4
print(v)

val = [6, 6, 2, 1]
x = [5, 8]
if x[0] < val[len(val)%2]:
	x[1] += 5//len(val)
x.pop(-1)
print(x[0])

y = [0, 5]
d = "cow"
if d.isalpha():
	d += "dog"*2 + "."
elif not " " == d:
	y.reverse()
elif d.isalnum():
	d += "dog" + "fox"
d += "." + "bat"
print(d)

x = 5
a = [".", "john", ","]
if not a[1].isalnum():
	b = "joe" + a[-1][-1]
else:
	a.sort()
a.insert(1, str(x)*3)
print(a[3])

x = "300"
v = [4, 7]
if " " != x:
	y = [5] + v[:4] + [v[1]]
	v.reverse()
elif v[-1] >= int(x[0]):
	a = ["2000"*2, "300"]
	x += a.pop(0)[0:-1] + "700"
elif "u" in x:
	b = [int(x)/10, v[-1]] + v
	x += "700" + "20"
v.append(1)
print(v[1])

e = 4
c = ["600", ",", "3000", "."]
if c[1] != " ":
	b = [2, e] + [2] + [len(c)]
	e = e%3
elif c[1].isdigit():
	b = [len(c[len(c)//3+1])] + [e] + [len(c[1]), 3]
	e -= 4+len(c[-1])
e += 4-len(c[-1])
print(e)

y = 1
a = ["bat", "cow"]
if "." == a[1]:
	y -= 1+len(a[0])
else:
	y += 5+len(a[1])
y += 2%len(a[1])
print(y)

b = 4
x = ["800", "."]
if x[len(x)//2] != " ":
	b -= len(x)+5
b -= len(x)+2
print(b)

a = "mary"
z = [2, 4]
if len(a) < z[-1]:
	a += "alice" + "."
elif a.isalpha():
	z[-1] -= len(a)**2
else:
	a = ","*3 + a[0]
z.sort()
print(z[1])

v = "7000"
y = [" ", ",", "7000", "7000"]
if y[-1].isalnum():
	y.pop()
y.insert(-2, y[-1][len(y)%4])
print(len(y))

c = 4
d = [6, 8]
if len(d) <= c:
	c += 2+d[0]
c += d[-1]/4
print(c)

v = ["mary", " ", "john", "alice"]
y = ["pat", "mary", " "]
if v[-1].isalnum():
	v.insert(1, v.pop(0)[1])
elif v[1].isdigit():
	y[-1] += "joe" + v.pop(-1)[:2]
v.append("alice")
print(len(v))

v = "cat"
y = [" "]
if "o" not in y[0]:
	v = v.replace("a", "dog") + "fox"
v += y[-1][len(y)//4-1] + " "
print(v)

v = "bob"
e = [5, 8]
if "o" in v:
	v = "." + v[-2]
else:
	v += "john" + "alice"
v += "alice" + "."
print(v)

y = ["ann", "bob", "mary"]
z = ","
if "e" not in y[1]:
	c = ["mary"] + y[2:5] + ["john"*2, y.pop(-1)[2:4]]
	c.pop(-2)
else:
	c = y + ["mary"]
	y.append("bob")
y[0] = "," + y[0][2:]
print(y[-1])

a = ["cat", "dog", "."]
c = "cow"
if a[0].isalpha():
	z = [4] + [2, 1]
	a.insert(2, c.replace("w", "cow"))
else:
	z = [" "] + a*3
	c += "," + z[0].upper()*3
a.sort()
print(a[3])

