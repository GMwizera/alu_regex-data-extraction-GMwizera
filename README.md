# ALU Regex Data Extraction

A Python tool that extracts structured data from text using regular expressions, designed for processing large volumes of API responses.

## Project Overview

This application uses regular expressions to identify and extract specific data patterns from JSON content:

- **Email addresses**: Extracts standard email formats like g.mwizera@alustudent.com
- **URLs**: Captures web addresses with various subdomains and paths
- **Phone numbers**: Detects multiple phone number formats including international codes
- **Hashtags**: Identifies social media hashtags
- **Time formats**: Recognizes both 12-hour (2:30 PM) and 24-hour (14:30) time notations
- **HTML tags**: Extracts HTML elements including those with attributes

## How It Works

The tool uses Python's `re` module to apply carefully crafted regex patterns against input text. Each pattern is optimized to handle common variations and edge cases found in real-world data.

```python
# Example regex pattern for Time extraction
r"(?:(?:0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9](?:\s?[AP]M)?|\d{1,2}:[0-5][0-9](?:\s?[AP]M))",
```

## Setup & Usage

1. Clone the repository:
```
git clone https://github.com/GMwizera/alu_regex-data-extraction-GMwizera.git
cd alu_regex-data-extraction-GMwizera

```

2. Place your JSON data file in the project directory (or use the provided test_data.json)

3. Run the script:
```
python main.py
```

The script outputs each type of extracted data, making it easy to view and analyze the results.

## Project Structure

- `main.py`: Main script with regex patterns and extraction logic
- `test_data.json`: Sample JSON data for testing the extraction
- `README.md`: Project documentation

## Author

[Mwizera Amen Gisele]  
[g.mwizera@alustudent.com]