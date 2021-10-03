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
        number_list = list(map(float, input("Enter the list numbers separated by space ").strip().split()))
        if ('stop' in number_list):
            print('exiting')
            break
    print(number_list)
