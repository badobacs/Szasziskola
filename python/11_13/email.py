def email_olvas():
    email=input()
    if not "@" in email:
        raise Exception("Nem valid emai cím")
    return email

asd=""
try:
    asd = email_olvas()
except Exception as e:
    print(e)

print(asd)
