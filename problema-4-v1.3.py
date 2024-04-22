#https://vjudge.net/problem/CodeForces-559B
def ordenar(a):
    l = len(a)
    if l%2 == 1: #este ej me rompio un poco la cabeza porque estaba pensando que len(a) era 2**n, osea el caso base era de 2 y se podia hacer de forma iterativa, pero puede ser de "longitud = cualquier numero primo*2", y el caso base es un numero primo != 2 :p
        return a
    else:
        a1 = ordenar(a[l//2:])
        b1 = ordenar(a[:l//2])
        return max(a1,b1) + min(a1,b1)

def equivalent(a,b):
    if a == b:
        return True
    else:
        return ordenar(a) == ordenar(b)
    
def main():
    a = input()
    b = input()
    
    if equivalent(a,b):
        print("YES")
    else:
        print("NO")	 

if __name__ == "__main__":
    main()	
