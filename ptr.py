import sys

def simple_interest(p, r, t):
    return (p * r * t) / 100

if __name__ == "__main__":
    p = float(sys.argv[1])
    r = float(sys.argv[2])
    t = float(sys.argv[3])

    si = simple_interest(p, r, t)
    print("Simple Interest:", si)