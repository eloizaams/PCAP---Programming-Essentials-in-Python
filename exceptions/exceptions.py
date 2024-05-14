def read_int(prompt, min, max):
    try:
        v = int(input(prompt))
        assert v >= -10 and v <= 10
    except ValueError:
        print ("Enter a integer value!")
        raise
    except AssertionError:
        print("The value must be from 10 to 10") 
        raise
    except:
        print("Ocurred an error")
        raise
    return v

try:
    v = read_int("Enter a number from -10 to 10: ", -10, 10) 
    print("The number is:", v)
except:
    print("")
    
