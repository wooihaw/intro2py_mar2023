# Write a Python script to find the frequency of occurance for each alphabet in a string.
astring = 'The quick brown fox jumps over the lazy dog.'

# Clean and normalize the sentence
alist = [c.lower() for c in astring if c.isalpha()]  
print(alist)

freq = {}
for c in sorted(set(alist)):
    freq[c] = alist.count(c)
print(f"{freq=}")
