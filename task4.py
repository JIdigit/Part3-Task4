
my_list_length = int(input('How many number to insert: '))
my_list = list()

for i in range(0,my_list_length):
    number = int(input())
    my_list.append(number)
if max(my_list) < 0:
    print('Minimal Positive integer is 1')
    
else:
    my_list.sort()
    for i in range(0,len(my_list)):
        try:
            next_number = my_list[i+1]
        except:
            continue
        if my_list[i]+1 != next_number:
            print('Minimal positive integer is: ', my_list[i]+1)
            break
