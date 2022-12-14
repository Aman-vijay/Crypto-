
-------------------project by Ayush Sharma and Aman Vijay-------------------

we have made project on attacking Double-DES with meet-in-the-middle (MITM) concept

--------------------------overview on 2-DES and meet-in-the-middle attack---------------------------

The Double DES uses two example of DES cipher for encryption and two units of reverse DES cipher for decryption. Each unit of DES cipher needs multiple key for encryption which enhance the size of the key (112 bit) creating it more secure. But in the double DES can be destroyed by known plaintext attack known as meet-in-themiddle attack.
Given a plaintext P and two encryption keys K1 and K2, ciphertext C is produced as C = Ek2(Ek1, (m)) decryption needed that the keys be used in reverse order −
P = Dk1(Dk2, (C))

A Meet-in-the-Middle (MitM) Attack is a type of cryptanalytic attack where the attacker need some type of space or time tradeoff to support the attack. MITM attempt can decrease the amount of difficulty needed to perform the assault in its original state.

Cosnider a cryptanalyst have a previous pair of P and C then it can use all possible values (256) of K1 and record all values of M. Similarly for all values of K2 access all M and thus compare these M’s of K1 and K2 and discover a pair of K1 and K2 for which M is same.

If only one such pair occur then K1 and K2 are the desired keys. If more than one pair exists for which K1 and K2 are equal, another intercepted plaintext/ciphertext pair is utilized.

---------------------------------------------------------------------------------------------------------------

so here we have used MITM to solve a specific discrete problem square-root of the operations of the simplest brute force attack.

Given prime p
then Zp* = {1, 2, 3, ..., p-1}
let g and h be elements in Zp* such that
such that h mod p = g^x mod p where 0 < x < 2^40
find x given h, g, and p

-----------------------------------------Attack_Idea----------------------------------
step1----

        let B = 2^20 then B^2 = 2^40
        then x= xo * B + x1 where xo and x1 are in {0, 1, ..., B-1}
        Then smallest x is x = 0 * B + O = 0
        and the largest x is x = B * (B-1) + B - 1 = B^2 - B + B -1 = B^2 - 1 = 2^40 - 1
        Then:
        h = g^x
        h = g^(xo * B + x1)
        h = g^(xo * B) * g^(x1)
        h / g^(x1) = g^(xo*B)
        so we will try to Find xo and x1 given g, h, B

step2-----

        Building a hash table key: h / g^(x1), with value x1 for x1 in { 0, 1, 2, .., 2^20 - 1}
        For each value x0 in {0, 1, 2, ... 20^20 -1}, we will check if (g^B)^(x0) mod P is in hash table. 
        If it is then we have found x0 and x1
        finally we'll Return x = xo * B + x1

-------------------------------------------------------------------------------------------

We have observed that Work is 2^20 multiplications and 2^20 lookups in the worst case
If we attack it by bruteforce , we would do 2^40 multiplications
but our work is squareroot of brute force 

-------------------------------------END--------------------------------------------------



