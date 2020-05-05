def mail_user(mail):
    if mail: #ignore emty strings
        try:
            username = mail[0:mail.index("@")]
            return username
        except Exception:
            return mail
    else: return mail


def mailpass_userpass(line):
    if line: # Ignore emtpy lines
        try:
            mail = line.split(":")[0]
            passswd = line.split(":")[1]
            convmail = mail_user(mail) #converted email
            if mail != convmail: return f"{convmail}:{passswd}"
            else: return line
        except Exception:
            return line
    else: return line


def user_mail(user, domain):
    if user: return f"{user}@{domain}"
    else: return user


def userpass_mailpass(line, domain):
    if line:
        try:
            user = line.split(":")[0]
            passswd = line.split(":")[1]
            convuser = user_mail(user,domain)
            return f"{convuser}:{passswd}"
        except Exception:
            return line
    else: return line
