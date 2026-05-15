def send_email(user, subject):
    return {
        "sent": True,
        "user": user,
        "subject": subject
    }
# TODO: retry failed notifications