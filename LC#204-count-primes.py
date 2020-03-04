# refer this algorithm:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

class Solution:

    def isprimes(self, n: int) -> int:

        if n <= 2:
            return 0

        primes_list = [True]*n
        primes_list[0] = False
        primes_list[1] = False

        for i in range(2, int(n**0.5)+1):
            if primes_list[i]:
                for j in range(i*i, n, i):
                    primes_list[j] = False
        return primes_list.count(True)


    def countPrimes(self, n: int) -> int:

        return self.isprimes(n)

#         output = 0
#         for i in range(1, n):
#             primes_flag = 1
#             if i==2:
#                 output += 1
#                 continue
#             if i==1 or i%2==0:
#                 primes_flag = 0
#                 continue
#             j = 3
#             while j<=i-1:
#                 if i % j==0:
#                     primes_flag = 0
#                     break
#                 j += 1
#             if primes_flag==1:
#                 output += 1

#         return output
