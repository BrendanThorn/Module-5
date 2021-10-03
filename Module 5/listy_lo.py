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
        number_list_input = list(input("Enter number to be calculated. Enter stop to stop: ").strip())
        number_list.append(number_list_input)
        if ('s' in number_list_input):
            print('exiting')
            number_list.pop()
            break
    print(number_list)
    
