### This template is for the class exercises covered in M02_L05_control-flow for CS 22B.

##### CL5.1 Boolean logic and evaluation
### Without running Python, determine the value (True or False) for each expression. What is your reasoning for each?
a = 4
b = 7
c = False

(a > 3 and b < 10) or c
#a>3 True, b<10 True → True and True = True → True or False = True

not (a == 4 and b != 7)
#a==4 True, b!=7 False → True and False = False → not False = True

(a >= 5) == (b <= 7)
#a>=5 False, b<=7 True → False == True = False

(not c and a < b) or (a == b)
#not c True, a<b True → True and True = True → True or (a==b False) = True


##### CL5.2 if-elif-else evaluation
### What will be the value of d? 9
val = 5
d = 1
if val != d:
    v = val/val-5
    d += val+3
elif -5 < d:
	y = 3+val+d
	y -= 3-val
else:
	x = 2
	d += 4+val
print(d)


##### CL5.3 if-elif-else 
### What is the value of result? "B"
### Will the if statement raise an exception? No error because x!=0 is False and the 'and' results in the code never evaluating y/x

x = 0
y = 10

if x != 0 and y / x > 2:
    result = "A"
else:
    result = "B"
print(result)


##### CL5.4: While loop 
### What is the final value of total and n? Adds 1-10 and sum=55, then n increments to 11. Loop body is executed 10 times

total = 0
n = 1

while total <= 50:
    total += n
    n += 1
print(total, n)

### Rewrite the loop so that it stops at exactly when total first exceeds 50
total2 = 0
n2 = 1

while True:
    total2 += n
    n2 += 1
    if total2 > 50:
        break
print("while loop rewritten", total, n)

##### CL5.5 Infinite loop
### This loop never terminates. 
## Why infinite? when s is even, 'continue' will skip s-=1 so s is stuck at 10

s = 10

#while s > 0:	
#    if s % 2 == 0:
#        continue
#    s -= 1

### Fix it so that the loop will terminate
## Fix attempt #1
s2 = 10
while s2 >0:
    if s2 % 2 ==0:
        s2 -= 1
        print("s2 while loop, ", s2)
        continue
    s2 -= 1
print("s2 exit while loop, ", s2)

## Better fix avoids using continue
s3 = 10
while s3 > 0:
    if s3 % 2 != 0:
        print("s3 while loop, ", s3)
        pass
    s3 -= 1
print("s3 exit while loop, ", s3)


##### CL5.6 Dictionary comprehension and boolean filtering
### Given the words list below, write a dictionary comprehension that maps each word to its length only if the word contains the letter 'o'.

words = ["data", "logic", "loop", "condition", "flow", "python"]

## Dict comp
d_words = {word: len(word) for word in words if "o" in word}
print(d_words)

