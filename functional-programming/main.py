from extract import extract_user_data
from transform import clean_users
from load import save_to_json
from utils import log_step

@log_step
def run_pipeline():
    # Extract step
    raw_data = extract_user_data()
    # Transform step
    cleaned_data = clean_users(raw_data)
    # Load step
    save_to_json(cleaned_data, "output.json")

if __name__ == "__main__":
    run_pipeline()