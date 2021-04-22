# input -> "Hello wolrd"
# output -> "drlow olleH"

phrase = input("Enter your phrase:")
phrase_reversed = ""

phrase_length = len(phrase)
for i in range(phrase_length + 1):
    phrase_reversed += phrase[-i] # phrase_reversed = phrase_reverse + phrase[-1]

print(f"Reversed phrase is : '{phrase_reversed}'")
print(f"Integrated phyton solutions: '{phrase[::-1]}'")

iter_len = int(len(phrase) / 2)
for i in range(iter_len):

