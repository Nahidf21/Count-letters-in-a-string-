def update_count(letters,counts_d):
    for c in letters:
        if c in counts_d:
            counts_d[c]=counts_d[c]+1
        else:
            counts_d[c]=1
    return counts_d 

counts= {"a":0,"b":0}

x=update_count("atyacker",counts)
print(x)