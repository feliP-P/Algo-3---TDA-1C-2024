def trading_cost(n,list):
    costo = 0
    for i in range(n-1):
        costo += abs(list[i])
        list[i+1] += list[i]
    return costo

def main():
    n = int(input())
    while n!=0:
        l = list(map(int, input().split()))
        print(trading_cost(n, l))
        n = int(input())

if __name__ == "__main__":
    main()