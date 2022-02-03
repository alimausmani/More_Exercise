




# def encrypt():
#     message = input("Enter the message you want to decrypt")
#     ascii_message = [ord(char) for char in message]
#     decrypt_message = [ chr(char) for char in ascii_message]  
#     print (''.join(decrypt_message))

# flag = True
# while flag == True:
#     choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
#     if choice == 'e':    
#         print()  
#     else:
#         choice = 'd'   
#         play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
#     if play_again == 'Y':
#         continue
#     else:
#         play_again == 'N'
#     break



# def encrypt():
#     message = input("Enter the message you want to decrypt")
#     ascii_message = [ord(char) for char in message]
#     decrypt_message = [ chr(char) for char in ascii_message]  
#     print (''.join(decrypt_message))

flag = True
while flag ==True:
 def encrypt():    
    choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
    if choice == 'e':    
        message = input("Enter the message you want to decrypt")
        ascii_message = [ord(char) for char in message]
        decrypt_message = [ chr(char) for char in ascii_message]  
        print (''.join(decrypt_message))
    else:
        choice = 'd'
 def decrypt():
    message = input("Enter the message you want to decrypt")
    ascii_message = [ord(char) for char in message]
    decrypt_message = [ chr(char) for char in ascii_message]  
    print (''.join(decrypt_message))
    play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
    if play_again == 'Y':
       print()
       continue
    else:
        play_again == 'N'
    break
