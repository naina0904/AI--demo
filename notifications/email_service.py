def send_email(user, subject):
    return {
        "sent": True,
        "user": user,
        "subject": subject
    }
# TODO: retry failed notifications
def retry_notification():
    return True
def monitor_notification_failures():
    return "monitoring-enabled"