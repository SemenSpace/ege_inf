for N in range(20024, 20025):
    kon = []
    for i in range(len(str(N)) - 2):
        kon.append(int(str(N)[i:i+3]))
    R = max(kon) - min(kon)
    """if R == 415:
        """
    print(N, R)