def is_isomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
