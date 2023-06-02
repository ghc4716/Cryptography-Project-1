import re

def splitevenodd(string):
   evenlist = []
   oddlist = []
   for i in range(len(string)):
      if (i % 2 == 0):
         evenlist.append(string[i])
      else:
         oddlist.append(string[i])
   return([evenlist,oddlist])

def combine(sub,shift):
    combined=[]
    length=max(len(sub),len(shift))
    try:
        for a in range(length):
            combined.append(sub[a])
            combined.append(shift[a])
    except Exception as e:
        print("")
    return combined


def encryption(plain):
    plain=str.upper(plain)
    result=splitevenodd(plain)
    even, odd= result[0], result[1]
    sub=substitution(even)
    shift=caesar(odd, even)
    final_result=combine(sub,shift)
    final_result=''.join(final_result)
    return final_result

def decryption(cipher):
    cipher=cipher.upper()
    result=splitevenodd(cipher)
    even, odd = result[0], result[1]
    dec_sub=decryption_substitution(even)
    dec_shift=decryption_caesar(odd,even)
    final_result = combine(dec_sub, dec_shift)
    final_result = ''.join(final_result)
    return final_result



def substitution(plain):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', " ", "-", "_", ".", "&", "?", "!", "@", "#", "/"]
    sub_alphabets = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', " ", "-", "_", ".", "&", "?", "!", "@", "#", "/"]
    resultStr = []
    lenght= len(plain)
    alphalenght=len(alphabets)
    for i in range(lenght):
        for j in range (alphalenght):
            if (plain[i] == alphabets[j]):
                resultStr.append(sub_alphabets[j])
    return resultStr

def decryption_substitution(even):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U','V', 'W', 'X', 'Y', 'Z'," ", "-", "_", ".", "&", "?", "!", "@", "#", "/"]
    sub_alphabets = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                     'H','I', 'J', 'K', 'L', 'M'," ", "-", "_", ".", "&", "?", "!", "@", "#", "/"]
    resultStr = []
    lenght = len(even)
    alphalenght = len(alphabets)
    for i in range(lenght):
        for j in range(alphalenght):
            if (even[i] == sub_alphabets[j]):
                resultStr.append(alphabets[j])
    return resultStr

def decryption_caesar(odd, even):
    result = []
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    punc = [" ", "-", "_", ".", "&", "?", "!", "@", "#", "/"]
    for i in range(len(odd)):
        char = even[i]
        cchar = odd[i]
        if (cchar in punc):
            result.append(cchar)
        else:
            prev_letter = alphabets.index(char) + 1
            current_letter = alphabets.index(odd[i])
            current_letter -= prev_letter +13
            current_letter = (current_letter) % 26
            letter = alphabets[current_letter]
            result.append(letter)
    return result

def caesar(plain,shift):
    result = []
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    punc=[" ", "-", "_", ".", "&", "?", "!", "@", "#", "/"]
    for i in range(len(plain)):
        char = shift[i]
        cchar= plain[i]
        if (cchar in punc):
            result.append(cchar)
        else:
            prev_letter = alphabets.index(char)+1
            current_letter= alphabets.index(plain[i])
            current_letter+=prev_letter
            current_letter= (current_letter) % 26
            letter=alphabets[current_letter]
            result.append(letter)
    return result

def seperate(text):
    punc = [",","-", "_", ".","'", "&", "?", "!", "@", "#", "/",'',"(",")",":" ]
    lis= re.split('(\W)', text)
    result=[]
    for i in lis:
        if (i in punc):
            result.append(i)
        else:
            result.append(encryption(i))

    new = ""
    for x in result:
        new += x
    return new

def deseperate(text):
    punc = [",","-", "_", ".","'", "&", "?", "!", "@", "#", "/",'',"(",")",":" ]
    lis= re.split('(\W)', text)
    result=[]
    for i in lis:
        if (i in punc):
            result.append(i)
        else:
            result.append(decryption(i))

    new = ""
    for x in result:
        new += x
    return new

#TYRJA PDE is desired result for green car
print(encryption("already"))
print(decryption("NMEWNEL"))



