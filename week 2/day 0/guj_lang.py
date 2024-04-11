chalu = 0
sankhyas = {}

def bhasa(string):
    global chalu, sankhyas  # Declare chalu and sankhyas as global variables
    if string == "Ram Ram" and chalu == 1:
        print("Already Started")
        return False

    elif string == "Ram Ram":
        chalu = 1
        return

    if "chapo" in string and chalu == 1:
        string = string.replace("chapo", "")
        if '@' in string:
            string = string.replace("@", "")
            print(string.format(**sankhyas))
            return
        else:
            print(string)
            return

    if "sankhya" in string and chalu == 1:
        string = string.replace("sankhya", "")
        # Remove white spaces and split the string by '='
        key, value = map(str.strip, string.split('='))
        try:
            value = int(value)
            sankhyas[key] = value
        except ValueError:
            print("Sankhya Sarkhi Lakho")
        print(sankhyas)
        return

    if string == "Jay Mataji" and chalu == 1:
        print("here")
        chalu = 0
        return True

    elif string == "Jay Mataji" and chalu == 0:
        print("Please Start")
        return

    print("Syntax Sarkho Lakh")

print("Welcome to Het's Language\n $ Currently only supports printing\n $ Start with Ram Ram\n $ End with Jay Mataji\n $ Write chapo and then your text to print\n $ e.g., Chapo hello World\n   output: hello World\n**************************** ")    

while True:
    if bhasa(input("$--:")):
        print("done")
        break
 