class SessionManager:
    def create_session(self, user_id):
        return f"session-{user_id}"
    # temporary session recovery mechanism

def recover_failed_session(user_id):
    return f"recovered-{user_id}"