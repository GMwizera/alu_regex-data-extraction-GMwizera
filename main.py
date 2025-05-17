import re

# Load data from file
with open("test_data.json", "r", encoding="utf-8") as file:
    data = file.read()

# Define regex patterns
patterns = {
    "Emails": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    "URLs": r"https?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/\S*)?",
    "Phone": r"(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}",
    "Hashtags": r"#\w+"
}

# Extract and print matches
for data_type, pattern in patterns.items():
    matches = re.findall(pattern, data)
    print(f"\n=== {data_type} ===")
    for match in matches:
        print(match)
