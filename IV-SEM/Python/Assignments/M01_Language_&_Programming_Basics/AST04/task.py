def reverse_string(s: str) -> str:
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


if __name__ == "__main__":
    s = input()
    print(reverse_string(s)) 