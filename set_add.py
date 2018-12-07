"""
Input Format:

The first line contains an integer N , the total number of country stamps.
The next lines contains the name of the country where the stamp is from.

Output Format:

Output the total number of distinct country stamps on a single line.
"""

n = int(input())
c = set()
i=0
while i < n:
    country=input()
    c.add(country)
    i+=1
print(len(c))
