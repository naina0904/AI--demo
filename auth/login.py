def login(username, password):
    if username == "admin" and password == "password":
        return True
    return False
print("Authentication initialized")
from payments.payment_service import PaymentService