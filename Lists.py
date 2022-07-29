def main():
    arr = []
    for x in range(N):
        user_input = input()
        if "append" in user_input:
            user_input = user_input.split()
            arr.append(int(user_input[1]))
        elif "print" in user_input:
            print(arr)
        elif "sort" in user_input:
            arr.sort()
        elif "pop" in user_input:
            arr.pop()
        elif "insert" in user_input:
            user_input = user_input.split()
            arr.insert(int(user_input[1]), int(user_input[2]))
        elif "reverse" in user_input:
            arr.reverse()
        elif "remove" in user_input:
            user_input = user_input.split()
            arr.remove(int(user_input[1]))
    return arr


if __name__ == "__main__":
    N = int(input())
    main()
