howmany_students=int(input()) #讀入幾個學生
student_lists={}
studentsgrade_lists=[]

#for迴圈讀度學生名字以及學生成績
for i in range(0,howmany_students):
	student_name=input()
	student_grade=float(input())
	student_lists[student_name]=student_grade
	studentsgrade_lists.append(student_grade)

studentsgrade_lists.sort()
tmp = studentsgrade_lists[1]
index = 1
while tmp == studentsgrade_lists[index-1]:
	index = index+1
	tmp = studentsgrade_lists[index]
	if index == howmany_students:
		break

answer_lists=[]
for item in student_lists:
	if student_lists[item] == tmp:
		answer_lists.append(item)

answer_lists.sort()
for name in answer_lists:
	print (name)