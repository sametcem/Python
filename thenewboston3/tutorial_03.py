def add_numbers(*args):
    total=0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(3,32)
add_numbers(3,43,5453,354234,463463)


def health_calculator(age,apple_ate,cigs_smoked):
    answer =(100-age) + (apple_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

bucky_data = [27,20,0]

health_calculator(bucky_data[0],bucky_data[1],bucky_data[2])
health_calculator(*bucky_data) #Unpacking argument list