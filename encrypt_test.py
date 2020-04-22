import encrypt as e
string="MAIN HU KHALLNAYAK @#! 123 ((())"
A=e.MYcrypt()
encrypted=A.encrypt(string,15)
print("Encrypted String\t: ",end="")
print(encrypted)
print("Decrypted String\t: ",end="")
decrypted=A.decrypt(encrypted,15)
print(decrypted)