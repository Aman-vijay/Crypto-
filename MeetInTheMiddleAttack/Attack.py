
#----gmpy2 is an optimized, C-coded Python extension module that supports fast multiple-precision arithmetic.
from gmpy2 import mpz
from gmpy2 import t_mod, invert, powmod, add, mul, is_prime
import textwrap


#Given prime p
#then Zp* = {1, 2, 3, ..., p-1}
#let g and h be elements in Zp* such that
#such that h mod p = g^x mod p where 0 < x < 2^40
#We have to find x and given h, g, and p



#----so here we have initialized p,g,h strings with any random values
p_string = '13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171'
g_string = '11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568'
h_string = '3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333'



def printing(x):
    x = textwrap.wrap(x, width=32)
    for i in x:
        print(" ",i)
    print()

#---------------------------attack idea------------------------------
#let us take B = 2^20 then B^2 = 2^40
#then x= xo * B + x1 where xo and x1 are in {0, 1, ..., B-1}
#Then smallest x is x = 0 * B + O = 0
#and the largest x is x = B * (B-1) + B - 1 = B^2 - B + B -1 = B^2 - 1 = 2^40 - 1
#so,
#h = g^x
#h = g^(xo * B + x1)
#h = g^(xo * B) * g^(x1)
#h / g^(x1) = g^(xo*B)
#so will try to find xo and x1
#---------------------------------------------------------------------



#------here we have Build a hash table key: h / g^(x1), with value x1 for x1 in { 0, 1, 2, .., 2^20 - 1}

def build_table(h, g, p, B):
    table, z = {}, h
    g_inverse = invert(g, p)
    table[h] = 0
    for x1 in range(1, B):
        z = t_mod(mul(z, g_inverse), p)
        table[z] = x1
    return table



#-------function which For each value x0 in {0, 1, 2, ... 20^20 -1} will check if (g^B)^(x0) mod P is in hash table.
#-------If it is then found x0 and x1 and function will return it

def lookup(table, g, p, B):
    gB, z = powmod(g, B, p), 1
    for x0 in range(B):
        if z in table:
            x1 = table[z]
            return x0, x1
        z = t_mod(mul(z, gB), p)
    return None, None


# -------function in which If we found xo and x1 then we will Return x, where x = xo * B + x1

def find_x(h, g, p, B):
    table = build_table(h, g, p, B)
    x0, x1 = lookup(table, g, p, B)
    # assert x0 != None and x1 != None
    Bx0 = mul(x0, B)
    x = add(Bx0, x1)
    # print(x0, x1)
    return x


def run(p_string, g_string, h_string):

    p = mpz(p_string)
    g = mpz(g_string)
    h = mpz(h_string)
    B = mpz(2) ** mpz(20)

    assert is_prime(p)
    assert g < p
    assert h < p

    x = find_x(h, g, p, B)

    assert h == powmod(g, x, p)
    return x


if __name__=="__main__":

    print()
    print("here p is prime, and both g and h is less than p")
    print("here we are finding x such that g^x mod p = h", end="")
    print("where g^x is g raised to the power of x \n")

    print()
    print("p = ")
    printing(p_string)

    print("g = ")
    printing(g_string)

    print("h = ")
    printing(h_string)

    print("finding x...")

    x = run(p_string, g_string, h_string)

    print("x = ", x)
    print()