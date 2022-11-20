
def upate_count(letters, counts_d):
    for c in letters:
        if c in counts_d:
            counts_d[c]=counts_d[c]+1
        else:
            counts_d[c]=1
    return counts_d


counts_ds={"a":2,"b":3}
print(upate_count("aaab",counts_ds))
print(counts_ds['a'])
print(counts_ds['b'])

counts_ds={}
print(upate_count("aaab",counts_ds))
print(counts_ds['a'])
print(counts_ds['b'])


counts_ds={'c':4}
print(upate_count("aaabc",counts_ds))
print(counts_ds['a'])
print(counts_ds['b'])
print(counts_ds['c'])