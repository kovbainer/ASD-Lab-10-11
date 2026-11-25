import sys

BASE = 10000
WIDTH = 4


def to_limbs(s):
    limbs = []
    for end in range(len(s), 0, -WIDTH):
        limbs.append(int(s[max(0, end - WIDTH):end]))
    return limbs


def add(a, b):
    if len(a) < len(b):
        a, b = b, a
    res = a[:]
    for i in range(len(b)):
        res[i] += b[i]
    return res


def sub(a, b):
    res = a[:]
    for i in range(len(b)):
        res[i] -= b[i]
    return res


def school(a, b):
    res = [0] * (len(a) + len(b))
    for i in range(len(a)):
        ai = a[i]
        if ai:
            for j in range(len(b)):
                res[i + j] += ai * b[j]
    return res


def karatsuba(a, b):
    n = max(len(a), len(b))
    if len(a) <= 32 or len(b) <= 32:
        return school(a, b)
    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))
    h = n // 2
    a0, a1 = a[:h], a[h:]
    b0, b1 = b[:h], b[h:]
    z0 = karatsuba(a0, b0)
    z2 = karatsuba(a1, b1)
    z1 = sub(sub(karatsuba(add(a0, a1), add(b0, b1)), z0), z2)
    res = [0] * (2 * n)
    for i in range(len(z0)):
        res[i] += z0[i]
    for i in range(len(z1)):
        res[i + h] += z1[i]
    for i in range(len(z2)):
        res[i + 2 * h] += z2[i]
    return res


def normalize(limbs):
    carry = 0
    for i in range(len(limbs)):
        v = limbs[i] + carry
        carry = v // BASE
        limbs[i] = v % BASE
    while carry:
        limbs.append(carry % BASE)
        carry //= BASE
    while len(limbs) > 1 and limbs[-1] == 0:
        limbs.pop()
    return limbs


def main():
    a_str, b_str = sys.stdin.read().split()
    res = normalize(karatsuba(to_limbs(a_str), to_limbs(b_str)))
    parts = [str(res[-1])] + ["%04d" % x for x in reversed(res[:-1])]
    sys.stdout.write("".join(parts) + "\n")


main()
