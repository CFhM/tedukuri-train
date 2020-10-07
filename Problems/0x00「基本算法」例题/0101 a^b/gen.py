import random


def main():
    with open('gen.in', 'w') as f:
        a = random.randint(1, 1e9)
        b = random.randint(1, 1e9)
        p = random.randint(1, 1e9)
        f.write('%d %d %d\n' % (a, b, p))


if __name__ == '__main__':
    main()
