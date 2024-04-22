#amigo quede 1 en el leaderboard de python :O
def monocarp1(n,s,t):
    a_index = []
    b_index =[]

    for i in range(n):  #O(n)
            if s[i] != t[i]:
                if s[i] == "a":
                    a_index.append(i+1)
                else:
                    b_index.append(i+1)

    a = len(a_index)
    b = len(b_index)

    if (a+b)%2 == 1:
        print(-1)

    else:
        #cantidad de operaciones
        if a%2==0:
            print((a+b)//2)
        else:
            print((a+b)//2 + 1)
        #operaciones
        i=0
        j=0
        while i<a-1:
            print(f"{a_index[i]} {a_index[i+1]}")
            i+=2
        while j<b-1:
            print(f"{b_index[j]} {b_index[j+1]}")
            j+=2
        if i <a and j<b:
            print(f"{a_index[i]} {a_index[i]}")
            print(f"{a_index[i]} {b_index[j]}")

def main():
    n = int(input())
    s = input()
    t = input()
    monocarp1(n,s,t)

if __name__ == "__main__":
    main()