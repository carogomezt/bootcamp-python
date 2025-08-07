from copy import deepcopy
from utils import log_step

@log_step
def validate_data(data):
    return list(filter(lambda u: isinstance(u[0], str) and isinstance(u[1], int) and isinstance(u[2], str), data))

@log_step
def convert_to_dict(data):
    return [
        {"name": name, "age": age, "email": email, "subscribed": subscribed}
        for name, age, email, subscribed in data
    ]

@log_step
def capitalize_names(data):
    return list(map(lambda u: {**u, "name": u["name"].strip().capitalize()}, data))

@log_step
def mask_emails(data):
    def mask(email):
        name, domain = email.split("@")
        return f"{name[0]}***@{domain}"
    
    return list(map(lambda u: {**u, "email": mask(u["email"])}, data))

@log_step
def filter_by_min_age(min_age):
    return lambda data: list(filter(lambda u: u["age"] >= min_age, data))

@log_step
def filter_subscribed(data):
    return list(filter(lambda u: u["subscribed"], data))

@log_step
def demonstrate_copying(data):
    shallow = data.copy()
    deep = deepcopy(data)
    print("\nOriginal ID:", id(data[0]))
    print("Shallow Copy ID:", id(shallow[0]))
    print("Deep Copy ID:", id(deep[0]))
    
    return data

@log_step
def clean_users(data):
    data = validate_data(data)
    data = convert_to_dict(data)
    data = demonstrate_copying(data)
    data = capitalize_names(data)
    data = mask_emails(data)
    data = filter_by_min_age(18)(data)
    data = filter_subscribed(data)

    return data