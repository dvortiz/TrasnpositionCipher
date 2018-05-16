#transposition cipher encrypt

def main():
    myMessage = 'Common sense is not so common.'
    mykey = 8

    ciphertext = encryptMessage(mykey, myMessage)

    # print encrypted string in cyphertext to the string,
    #with a | after it in case there are spaces at the end of the encrypted message
    print(cyphertext + '|')

def encryptMessage(key, message):
    #each string in cyphertext represents a column in the grid
    ciphertext = [''] * key
    #loop through each colum in chphertexts:
    for column in range(key):
        currentIndex = column

        #keep looping till currentIndex goes past the message lengh
        while currentIndex < len(message):
            # Place the character at current index in message at the end of the current column in the ciphertext list:
            ciphertext[column] += message [currentIndex]

            #move currentIndex over:
            currentIndex += key

    #convert the ciphertext list into a single string value and return it:
    return ''.join(ciphertext)

#if transpostion.encrypt.py is run(insead as a modlue) call the main function
if_name_ == '_main_':
 main()
        
    
