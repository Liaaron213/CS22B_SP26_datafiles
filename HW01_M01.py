### CS 22B Module 01 - Homework 1
### Name: Aaron Li 

### This template is for Homework #01 reviewing the material we covered in Module 01 Essentials for CS 22B.

### root folder if applicable
# root='/path/to/folder/'

##### Problem 1: Trim adapter reads and validate bases
## 1. Write a script that reads in adapter_reads.txt line by line and remove the first 14 base pair (characters) that are the adapters. 
## 2. Validate if the read is valid by ensuring that all the characters are in {A,T,C,G}. ie., Not another character eg N.
## 3. Write the valid trimmed reads to a new file, clean_reads.txt, and the invalid reads in another new file, bad_reads.txt. 
## 4. Print as output, the number of valid and invalid reads. 

def valid_seq(seq):
    valid_bases = {"A", "T", "C", "G"}
    return all (base in valid_bases for base in seq)

with open("adapter_reads.txt", "r") as infile:
    sequence = infile.read().strip()

trimmed_sequence = sequence[14:]


print ("Is valid? :", valid_seq(trimmed_sequence))
if valid_seq(trimmed_sequence) is True:
    print ("Yes")
    fileopen1 = open ("clean_reads.txt", "w")
    fileopen1.write (trimmed_sequence)
    fileopen1.close()
if valid_seq(trimmed_sequence) is False:
    print ("No")
    fileopen2 = open("bad_reads.txt", "w")
    fileopen2.write (trimmed_sequence)
    fileopen2.close()


##### Problem 2: List comprehension statistic
## 1. Using the valid trimmed reads from problem 1, create a list comprehension command that returns the length of each valid read. 
## 2. Create a second list comprehension command that returns the GC% of each valid read (ie., GC.count/length). 
## 3. Print as output, the minimum length, max length, and average length of your valid trimmed reads. Additionally, print the average GC% rounded to 3 decimals.

with open("clean_reads.txt", "r") as infile:
    reads = [line.strip() for line in infile if line.strip()]
length = [len(read) for read in reads]
print (length)

gc_percents = [(read.count("G") + read.count("C")) / len(read) for read in reads]
print (gc_percents)

min_length = min(length)
max_length = max(length)
avg_length = sum(length)/len(length)

avgGC = sum(gc_percents) / len(gc_percents)

print("Minimum length:", min_length)
print("Maximum length:", max_length)
print("Average length:", avg_length)
print("Average GC%:", round(avgGC, 3))

##### Problem 3: Dictionary
## 1. Using the valid trimmed reads from problem 1, build a dictionary called 'base_counts' that has the total counts of A, T, C, G across all valid reads. 
## 2. Use a loop that iterates over the dictionary and compute and print the product of the four counts (A*C*T*G).
base_counts = {
    "A": 0,
    "T": 0,
    "C": 0,
    "G": 0,
}

for i in trimmed_sequence:
    if i in base_counts:
        base_counts[i] += 1
        
product = 1

for count in base_counts.values():
    product *= count

print("Base counts:", base_counts)
print("Product:", product)

#### Problem 4: Function and asserts
## 1. Write a function that returns the percentage of any nt (A,T,C,G) in a sequence, rounded to 2 significant figure. 
## 2. Include 3 asserts to test your code including a known case (eg "AATT" with "A" returning 50.00) and a case with 0%.

def percent_of_nt(sequence, nt):
    nt = nt.upper()
    sequence = sequence.upper()
    
    count = sequence.count(nt)
    percentage = (count / len(sequence)) * 100
    
    return round(percentage, 2)

assert percent_of_nt("AATT", "A") == 50.00
assert percent_of_nt("GGTG", "T") == 25.00
assert percent_of_nt("TATA", "C") == 0.00
print ("Tests passed")

## Use this sequence as your test sequence
# sequence = TTATAAGCCGATTATAAGCCCGTAACCGGTTAG


