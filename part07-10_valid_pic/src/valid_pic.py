from datetime import datetime

def is_it_valid(pic: str):
    check_marker = True
    check_date = True
    check_control = True
    
# Validating length of PIC
    if len(pic) != 11:
        return False    

# Extracting the date in datetime format and validating the marker (+, = or A)
    try:
        if pic[6] == "+":
            date = datetime(1800 + int(pic[4:6]), int(pic[2:4]), int(pic[0:2]))
        elif pic[6] == "-":
            date = datetime(1900 + int(pic[4:6]), int(pic[2:4]), int(pic[0:2]))
        elif pic[6] == "A":
            date = datetime(2000 + int(pic[4:6]), int(pic[2:4]), int(pic[0:2]))
        else:
            check_marker = False
    except:
        return False

# Validating the date (from 1800 till now)
    date_low = datetime(1800, 1, 1)
    date_now = datetime.now()
    if date < date_low and date >= date_now:
        return False
    
# Validating the control character (last digit)
    control_str = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    control_char = control_str[int(pic[0:6] + pic[7:10]) % 31]
    if control_char != pic[10]:
        return False
    return True
        
if __name__ == "__main__":
    a = is_it_valid("081842-720N")
    b = is_it_valid("120488+246L")
    c = is_it_valid("310823A9877")
    d = is_it_valid("080842-720N")
    print(f"This code (081842-720N) is {a}")
    print(f"This code (120488+246L) is {b}")
    print(f"This code (310823A9877) is {c}")
    print(f"This code (080842-720N) is {d}")