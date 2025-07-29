# Closure functions are functions which makes use of the outer function arguments like this

def naa_outer_function_da(hi_sollu_mame):
    def naa_inner_function_da():
        return f"The message is: {hi_sollu_mame}"
    return naa_inner_function_da
say_hi=naa_outer_function_da("Vanakkam da mapla!")
print(say_hi())