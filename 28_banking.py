import os


def get_number(one_line):
    return one_line.split()[0]


def get_balance(one_line):
    return float(one_line.split()[1])


def get_name(one_line):
    return " ".join(one_line.split()[2:])


def equal_floats(x_flt, y_flt):
    return abs(x_flt - y_flt) < 1.0e-8


def process_bank_records(prefix):
    old_file_name = f"{prefix}.old.txt"
    new_file_name = f"{prefix}.new.txt"
    if not os.path.exists(old_file_name):
        print("Error: Old master file cannot be opened.")
        return
    try:
        old_file = open(old_file_name, "r")
        new_file = open(new_file_name, "w")
    except:
        print("Error: Could not open one of the files.")
        return
    for line in old_file:
        line = line.strip()
        if line == "999999":
            new_file.write("999999\n")
            break
        account_number = get_number(line)
        balance = get_balance(line)
        name = get_name(line)
        print(f"\nAccount Number: {account_number}")
        print(f"Account Balance: ${balance:.2f}")
        print(f"Account Holder: {name}")
        while True:
            code = input("Enter transaction code (d/w/c/a): ").strip().lower()
            if code == "d":
                amount = float(input("Enter deposit amount: "))
                if balance + amount <= 9999999.99:
                    balance += amount
                    print(f"New Balance: ${balance:.2f}")
                else:
                    print("Error: Balance exceeds upper limit.")
            elif code == "w":
                amount = float(input("Enter withdrawal amount: "))
                if balance - amount >= 0.0:
                    balance -= amount
                    print(f"New Balance: ${balance:.2f}")
                else:
                    print("Error: Insufficient funds.")
            elif code == "c":
                if equal_floats(balance, 0.0):
                    print("Account closed.")
                    break
                else:
                    print("Error: Balance must be zero to close account.")
            elif code == "a":
                new_file.write(f"{account_number} {balance:010.2f} {name}\n")
                break
            else:
                print("Invalid code.")
    old_file.close()
    new_file.close()
    print(f"\nUpdated records written to {new_file_name}.")


process_bank_records("sample.master")
