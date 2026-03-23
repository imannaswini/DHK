def generate_keys(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)

    key_A = pow(B, a, p)
    key_B = pow(A, b, p)

    return A, B, key_A, key_B