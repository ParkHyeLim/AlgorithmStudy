n = int(input())
students = []

for i in range(n):
    name, k, e, m = input().split()
    # 점수 환산(가중치)
    students.append((name, (100-int(k))*10000 + int(e) * 100 + (100-int(m))))

s_students = sorted(students, key=lambda x: (x[1], x[0]))
for s in s_students:
    print(s[0])
