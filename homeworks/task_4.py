def main(n):
    if not n:
        return -0.16
    elif n >= 1:
        prev = main(n - 1)
        return prev ** 3 - 1 - prev


# --- cut this out when submitting to robot ---
f = main(4)
print(f"{f:.2e}")