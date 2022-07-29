def main():
    output = [x for x in range(1, n + 1)]
    output = "".join(map(str, output))
    print(output)


if __name__ == "__main__":
    n = int(input())
    main()
