"""Write a Python program to get the index of the first element which is greater than a specified element. Go to the editor
Original list:
[12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]"""

orig_list=[12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
i=0
len_orig_list=len(orig_list)
orig_list.sort()
orig_list.reverse()
print(orig_list)
user_input=int(input("Enter A Number: "))
for element in range(len_orig_list):
    if user_input<orig_list[element]:
        t_list=[]
        t_list.append(orig_list[element])
        min_t_list=[t_list]
print(t_list)