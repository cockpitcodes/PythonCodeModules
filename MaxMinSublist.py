user_list=[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
len_user_list=len(user_list)
new_list=[]

for element in range(len_user_list):
    sublist_container=user_list[element]
    sublist_sum=sum(sublist_container)
    new_list.append(sublist_sum)

for  element2 in range(len_user_list):
    if(sum(user_list[element2]))==max(new_list):
        print(f"List With Maximum Sum: ",user_list[element2])
    if (sum(user_list[element2])==min(new_list)):
        print(f"List With Minimum Sum: ",user_list[element2])
