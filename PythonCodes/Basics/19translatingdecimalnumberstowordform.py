import "20Emoji_conversion_using_dictionary"


def num_translation():
    translation = {    # number translation list
        '1' : "One",
        '2' : "Two",
        '3' : "Three",
        '4' : "Four",
        '5' : "Five",
        '6' : "Six",
        '7' : "Seven",
        '8' : "Eight",
        '9' : "Nine",
        '0' : "Zero",

    }
    input_no = list(input("Number: "))            #converting input number to string list
    #input_no = list
    #print(input_no[4])
    #input_no = [6,2,0,3,6,1,4,2,0,0]
    #print(translation[input_no])                 #this won't work dictionary only excepts one value not a list
    output = ''                                   #defining a empty string variable 
    for ind_no in input_no:                       #for range for individual elements
        output += (translation[ind_no]) + ' '     #mapping the corresponding ind_no value to translation and storing their individual value together with space in output
    return(output)
print(num_translation())