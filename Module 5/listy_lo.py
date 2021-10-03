if __name__ == '__main__':

#list
    food = ['rice', 'beans']

#Appending list
    food.append('broccoli')

#Extending the list
    added_food = ('bread', 'pizza')
    food.extend(added_food)

#printing the first two
    print(food[0:2])

#Printing the last item
    print(food[-1])
    
#splitting breakfast
    Breakfast = "eggs,fruit,orange juice"
    Split_breakfast = Breakfast.split(",")
    Breakfast = Split_breakfast 
    print(Breakfast)

#How long is breakfast
    print(len(Breakfast))

#Input fun
    number_list = []
    while True:
        number_list_input = input("Enter number to be calculated. Enter stop to stop: ")
        number_list.append(number_list_input)
        if ('s' in number_list_input):
            number_list.pop()
            break
    print(number_list)
    
    for x in range(0, len(number_list)):
        number_list[x] = int(number_list[x])
        
    print(type(number_list[0]))
    print(type(number_list[1]))
    print(type(number_list[2]))


    print(min(number_list))
    print(max(number_list))
    Num_sum = sum(number_list)
    Len_sum = len(number_list)
    print(Num_sum/Len_sum)

