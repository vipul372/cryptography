def generate_key_matrix(key):
    result = list()
    #storing key letters
    for c in key: 
        if c not in result:
            if c =='J':
                result.append('I')
            else:
                result.append(c)
    #storing other character
    flag=0
    for i in range(65,91): 
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    #storing digits
    for i in range(0,10):
        result.append(i)
    result.append('@')
    #building key matrix
    key_matrix = []
    while result != []:
        key_matrix.append(result[:6])
        result = result[6:]
    return key_matrix


def locindex(c): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(key_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt(msg):
    msg=msg.upper()
    msg=msg.replace(" ", "") 
    output = []           
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            output.append(key_matrix[(loc[0]+1)%6][loc[1]])
            output.append(key_matrix[(loc1[0]+1)%6][loc1[1]])
        elif loc[0]==loc1[0]:
            output.append(key_matrix[loc[0]][(loc[1]+1)%6])
            output.append(key_matrix[loc1[0]][(loc1[1]+1)%6])
        else:
            output.append(key_matrix[loc[0]][loc1[1]])
            output.append(key_matrix[loc1[0]][loc[1]])
        i=i+2  
    return ''.join(str(e) for e in output)    
                 
def decrypt(msg):
    msg=msg.upper()
    msg=msg.replace(" ", "")
    output = []
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            output.append(key_matrix[(loc[0]-1)%6][loc[1]])
            output.append(key_matrix[(loc1[0]-1)%6][loc1[1]])
        elif loc[0]==loc1[0]:
            output.append(key_matrix[loc[0]][(loc[1]-1)%6])
            output.append(key_matrix[loc1[0]][(loc1[1]-1)%6])
        else:
            output.append(key_matrix[loc[0]][loc1[1]])
            output.append(key_matrix[loc1[0]][loc[1]])  
        i=i+2  
    return ''.join(str(e) for e in output) 

#testing

#Reading key from key.txt file
with open("key.txt") as f:
    key = f.read()
key=key.replace(" ", "")
key=key.upper()
#generating key matrix
key_matrix = generate_key_matrix(key)

def encryption_helper():
    #Reading input for encryption
    enc_if = open("enc_input.txt","r")
    enc_input_message = enc_if.read()
    enc_if.close()
    #encrypting the input msg
    enc_output_message = encrypt(enc_input_message)
    #writing the output of encryption method to the file enc_output.txt
    enc_of = open("enc_output.txt","w")
    enc_of.write(enc_output_message)
    enc_of.close()
    print("Encryption done! check the file enc_output.txt for the result.")

def decryption_helper():
    #Reading input for decryption
    dec_if = open("dec_input.txt","r")
    dec_input_message = dec_if.read()
    dec_if.close()
    #encrypting the input msg
    dec_output_message = decrypt(dec_input_message)
    #writing the output of encryption method to the file enc_output.txt
    dec_of = open("dec_output.txt","w")
    dec_of.write(dec_output_message)
    dec_of.close()
    print("Decryption done! check the file dec_output.txt for the result.")

while(1):
    choice = int(input("\n1. Encyption\n2. Decryption\n3. Exit\nEnter the choice: \n"))
    if choice == 1:
        encryption_helper()
    elif choice==2:
        decryption_helper()
    else:
        exit()
        