def header():
    title = "**Lucky Numbers**"
    print("*" * len(title)) # created a header design
    print(title)
    print("*" * len(title))

def modifyArray():
    """\x1b[35mMenu:\x1b[00m 
            \x1b[32m\x1b[1m1\x1b[00m -> \x1b[4m\x1b[36mAdd a number.\x1b[00m 
            \x1b[32m\x1b[1m2\x1b[00m -> \x1b[4m\x1b[36mInsert a number.\x1b[00m 
            \x1b[32m\x1b[1m3\x1b[00m -> \x1b[4m\x1b[36mModify a number.\x1b[00m
            \x1b[32m\x1b[1m4\x1b[00m -> \x1b[4m\x1b[36mDelete a number.\x1b[00m 
            \x1b[32m\x1b[1m5\x1b[00m -> \x1b[4m\x1b[36mArrange in ascending order.\x1b[00m  
            \x1b[32m\x1b[1m6\x1b[00m -> \x1b[4m\x1b[36mArrange in descending order.\x1b[00m 
    """
    try:
        askUser = int(input('\x1b[31mWhat do you want to do (Enter 1-6)?\x1b[00m \n >\x1b[34m '))
    except ValueError:
        print('\x1b[00m\x1b[32mThe entered option is not among the choices.\x1b[00m')










    



