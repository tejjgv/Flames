first_name = input("Enter The 1st Name : " ).lower()
second_name = input("Enter The 2nd Name : " ).lower()
# sad_list1 = '''Friends'''
# sad_list2 = '''Siblings'''
sad_list = ["Friends" , "Lovers" , "Affection" , "Marriage" , "Enemies" , "Siblings"]
print(f'''
Finding Flames For {first_name} and {second_name} ... ❤❤❤❤❤️ ''')
first_name = first_name.replace(" ","")
second_name = second_name.replace(" ","")

for i in first_name :
    for j in second_name :
        if i == j :
            first_name = first_name.replace(i,"",1)
            second_name = second_name.replace(j,"",1)
            break

count = len(first_name + second_name)

if count > 0 :
    list1 = ["Friends" , "Lovers" , "Affection" , "Marriage" , "Enemies" , "Siblings"]
    while len(list1) > 1 :
        c  =count%len(list1)
        s_index = c-1
        if s_index>=0 :
            left = list1[:s_index]
            right = list1[s_index+1:]
            list1 = right+left
        else :
            list1 = list1[:len(list1)-1]
else :
    print("The Names Are Same Try With Diffrent Names")
    
list2 = (','.join(list1))

if str(list2) == str(sad_list[0]) :
    print(f'''
Better Luck Next Time And The Relationship is : {list2}''')
elif str(list2) == str(sad_list[1]) :
    print(f'''
Better Luck Next Time And The Relationship is : {list2}''')
else :
    print('''
The Relationship is : ''',list2)

print('''
Copyright Desrves To Ajay Ganesh.

This Is For Joke Only Dont Try To Take It Serious And In Serious Dont Call To Python Owner ☠️☠️☠️☠️☠ .''')
