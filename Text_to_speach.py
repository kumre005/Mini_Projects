import os

if __name__ == '__main__':
    print("Wellcomem to Robospeacker")

    while True:
        x = input("Enter to convert : ")
        if x == "E":
            os.system("say ' hey... bye bye friend'")
            break
        
        command = f"say {x}"
        os.system(command)