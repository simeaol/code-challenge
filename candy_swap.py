def fairCandySwap(A, B):
    Asum = sum(A)
    Bsum = sum(B)

    delta = (Asum - Bsum) // 2
    print("Asum={0}, Bsum={1} and delta={2}".format(Asum, Bsum, delta))

    Aset = set(A)

    for number in B:
        if number + delta in A:
            return [number+delta, number]

if __name__ == "__main__":
    result = fairCandySwap([2], [1,3])
    print("The result is ={0}".format(result))