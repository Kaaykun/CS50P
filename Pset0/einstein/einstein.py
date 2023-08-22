def main():
    m = int(input("m: "))
    c = int(300000000)
    E = int(m * square(c))
    print(f"E: {E}")

def square(n):
    return n * n

main()