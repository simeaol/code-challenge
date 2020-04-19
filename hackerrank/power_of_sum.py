def total(X, N, num, space, whoCalledMe):
    if num**N < X:
        # print(num**N)
        
        # print(" "*space)

        print("*"*space + " " + whoCalledMe + "-> total({}, {}, {}) + total({}, {}, {})" .format(X, N, num+1, X - num**N, N, num+1))
        left = total(X, N, num+1, space+2, "left")
        rigth = total(X - num**N, N, num+1, space+2, "right")
        return  left + rigth
    elif num**N == X:
        print("*"*space + " " + whoCalledMe + "-> found a solution")
        return 1
    else:
        print("*"*space + " " + whoCalledMe + "-> Invalid value")
        return 0

if __name__ == "__main__":
    X = 10
    N = 2  
    num = 1
    print("total({}, {}, {})" .format(X, N, num))
    result = total(X, N, num, 2, "main")
    print("{}".format(result))

