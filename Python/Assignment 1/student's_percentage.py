#If the marks obtained by a student in five different subjects are input through the keyboard, 
# find out the aggregate marks and percentage marks obtained by the student. Assume that the 
# maximum marks that can be obtained by a student in each subject is 100. 
computer = float(input("Enter marks obtained in Computer: "));
maths = float(input("Enter marks obtained in Mathematics: "));
science = float(input("Enter marks obtained in Science: "));
nepali = float(input("Enter marks obtained in English: "));
AI = float(input("Enter marks obtained in Economics(100 marks): "));

aggregate_marks = computer + maths + science + nepali + AI;
print(f"Total marks obtained by the student : {aggregate_marks}")

percentage = (aggregate_marks / 500) * 100;
print(f"Percentage scored by the student: {percentage}");