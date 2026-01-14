def alph(S):
    vowels = "aeiouAEIOU"
    v = c = 0
    for char in S:
        if char.isalpha():
            if char in vowels:
                v += 1
            else:
                c += 1    
        
        
    return v,c
print (alph("bipasha"))       
           