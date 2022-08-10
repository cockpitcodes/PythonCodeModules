UserInputList=[]
NumOfElements=int(input("How Many Elements Would You Like To Have? : "))
for InputLoop in range(NumOfElements):
    UserInputElement=int(input("Enter Elements: "))
    UserInputList.append(UserInputElement)
print("*"*40)
print(f"Your Input List Is: {UserInputList}")
UserInputList[0],UserInputList[(NumOfElements-1)]=UserInputList[(NumOfElements-1)],UserInputList[0]
print(f"Your Swapped Input List Is: {UserInputList}")




