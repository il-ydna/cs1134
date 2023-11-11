def e_approx(n):
    factorial = 1
    total = 1
    for i in range(1, n+1):
        factorial *= i
        total += 1/factorial
    return total


def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)

main()