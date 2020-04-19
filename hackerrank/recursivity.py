res = 0
def fibonacci(n, who_call_me):
    print(f"{n} :{who_call_me}")
    if(n == 0 or n == 1):
        print("stop")
        return n
    return fibonacci(n-1, "left") + fibonacci(n-2, "rigth")







def fatorial(n):
    if(n == 0 or n == 1):
        return n
    return n * fatorial(n-1)



if __name__ == "__main__":
    n = 5
    result = fibonacci(n, "main")
    print("Fibonacci de {}={}".format(n, result))
    # ft = fatorial(5)
    # print("Fatorial de {}={}".format(5, ft))