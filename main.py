def encode(original_pass):
    ls_pass = list(original_pass)
    enc_pass = ""
    for i in (ls_pass):
        updated_pass = int(i) + 3
        string = str(updated_pass)
        enc_pass += string
    return enc_pass

def decode(password):
    password_lst = []
    decoded_password = ""

    try:

        for i in password:
            password_lst.append(i)

        for digit in password_lst:
            digit = int(digit)
            digit -= 3
            digit = str(digit)
            decoded_password += digit

        return decoded_password

    except TypeError as exc:
        print(exc)
