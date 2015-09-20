def main():

    from random import randint
    
    print ("I'm thinking of a number between 1 and 100... ")

    secretnum = randint(1,100)       #Computer generates number
 
    counter = 1
    x = 0

    while (x != secretnum):
        x = input ('\n' + 'Please guess a number: ')

        x = int(x)
        
        if (x > secretnum):
            print (str(x) + ' is too high. Try another number. \n')
            counter += 1
        elif (x < secretnum):
            print (str(x) + ' is too low. Try another number.\n')
            counter += 1
        else:
            print ('Hooray! ' + str(x) + ' is the correct number!!! \n')
            print ('You completed the game in: ' + str(counter) + ' guess(es) \n')
    input ('Press ENTER to exit program.')
    return 0

main()

    

