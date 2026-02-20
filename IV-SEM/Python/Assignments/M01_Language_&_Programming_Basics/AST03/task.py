def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    average = (n1 + n2 + n3) / 3
    
    if average >= 40:   # Assuming pass mark is 40
        status = "Pass"
    else:
        status = "Fail"
    
    return f"Average grade: {average:.2f}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = list(map(int, input().split()))
    print(Student_Grade_System(name, n1, n2, n3))
