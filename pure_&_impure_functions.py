# Impure functions

naa_veliya_irukken_da=0

def yaaru_saami_nee(unna_maathiten_da):
    global naa_veliya_irukken_da
    naa_veliya_irukken_da += unna_maathiten_da
    return naa_veliya_irukken_da

def maja_akkov_idhu():
    return naa_veliya_irukken_da 

print(yaaru_saami_nee(2))
print(maja_akkov_idhu())

# This is an example of impure function because the function yaaru_saami_nee access naa_veliya_irukken_da
# as global variable and it updates the value.
# In the function maja_akkov_idhu, we find that the value of naa_veliya_irukken_da is updated. This was
# done by the yaaru_saami_nee. - This function is called impure function
# maja_akkov_idhu is a pure function.