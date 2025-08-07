from utils import log_step

@log_step
def extract_user_data():
    return [
        (" alice  ", 25, "ALICE@example.COM", True),
        ("Bob", 17, "bob@example.com", True),
        ("Clara", 30, "clara@EXAMPLE.com", False),
        ("dan", 45, "dan@domain.com", True),
    ]