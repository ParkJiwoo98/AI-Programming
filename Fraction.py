class Fraction:
    def GCD(m, n):
        while n != 0:
            t = n
            n = m % n
            m = t
        return m
