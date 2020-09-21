import sys
from textwrap import wrap

def main():
    content = getContent()
    binaryConvert(content, 7)
    binaryConvert(content, 8)


def getContent():
    for line in sys.stdin:
        return line.rstrip()

    
def binaryConvert(content, length):
    text = ""

    if (len(content) % length) == 0: 

        wrapped_content = wrap(content, length)

        # print(wrapped_content)


        for character in wrapped_content:

            int_content = int(character, 2)
            #byte_number = int_content.bit_length() + 6
            #binary_array = int_content.to_bytes(byte_number, "big")
            #ascii_text = binary_array.decode()
            #ascii_text = ascii_text.strip().strip('\x00')
            #if (ascii_text == ""):
                #ascii_text = " "
            text += chr(int)
            

            #print(chr(int_content))
            #print(int_content)
            #print(byte_number)
            #print(binary_array)
            # print(ascii_text)   

        print("=============================================")
        print("Solution : " + text)
        print("=============================================")
    
main()