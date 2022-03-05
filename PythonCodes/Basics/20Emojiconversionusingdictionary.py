#message = input("> ")
#words = message.split(' ')   #Splits the message variable according to the specified delemeter
#emojis = {                   #Emoji dictionary
#    ':)' : '😀',
#    ':(' : '😟',
#}
#output = ''
#for word in words:
#    output += emojis.get(word,word) + ' '
#print(output)

#Converting the above code to function
def message_converter(string):
    words = string.split(' ')   #Splits the message variable according to the specified delemeter
    emojis = {                   #Emoji dictionary
        ':)' : '😀',
        ':(' : '😟',
    }
    output = ''
    for word in words:
        output += emojis.get(word,word) + ' '
    return(output)


message = input('> ')          #code from here dosen't belong to function
print(message_converter(message))