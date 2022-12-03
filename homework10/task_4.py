#class Cipher:

#encode_letter = ['A','B','C','D','E','F','G','H','I','J','']



class Cipher:
    def encode(self, string):
        encode_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        decode_letter = "CRYPTOABDEFGHIJKLMNQSUVWXZ"
        encode_dict = dict(zip(encode_letter, decode_letter))
        string = string.upper()

        tbl = string.maketrans(encode_dict)
        new_string = string.translate(tbl)
        new_string = new_string.capitalize()
        
        print(new_string)
    
    def decode(self, string):
        encode_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        decode_letter = "CRYPTOABDEFGHIJKLMNQSUVWXZ"
        decode_dict = dict(zip(decode_letter, encode_letter))
        string = string.upper()

        tbl = string.maketrans(decode_dict)
        new_string = string.translate(tbl)
        new_string = new_string.capitalize()

        print(new_string)

cipher = Cipher()
cipher.encode('Hello world')
cipher.decode('Fjedhc dn atidsn')