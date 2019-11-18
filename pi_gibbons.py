def pi_gibbons(base=10):
    """Gibbons spigot generator of digits of pi in given base."""
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            q, r, t, k, n, l = (base * q, base * (r - n * t), t, k,
                                (base * (3 * q + r)) // t - base * n, l)
        else:
            q, r, t, k, n, l = (q * k, (2 * q + r) * l, t * l, k + 1,
                                (q * (7 * k + 2) + r * l) // (t * l), l + 2)
print(pi_gibbons(1000))
