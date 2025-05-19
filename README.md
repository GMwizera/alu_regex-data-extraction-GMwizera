# ALU Regex Data Extraction

This project implements a data extraction system using Regular Expressions to identify and extract various types of data from text, including emails, URLs, phone numbers, and more.

## Features

- Email address extraction
- URL extraction
- Phone number extraction
- Credit card number extraction
- Time format extraction (12-hour and 24-hour)
- HTML tag extraction
- Hashtag extraction
- Currency amount extraction

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

### For Windows Users

1. Open Command Prompt or PowerShell
2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alu_regex-data-extraction-username.git
   cd alu_regex-data-extraction-username
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### For Mac Users

1. Open Terminal
2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alu_regex-data-extraction-username.git
   cd alu_regex-data-extraction-username
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

## Usage

1. Create a `test_data.json` file in the project root directory with your text data
2. Run the script:
   ```bash
   python main.py
   ```

## Example test_data.json

```json
{
  "text": "Contact us at user@example.com or visit https://www.example.com. Call us at (123) 456-7890. Payment: 1234-5678-9012-3456. Meeting at 2:30 PM. #coding #python"
}
```

## Output Format

The script will output extracted data in the following format:

```
=== Emails ===
user@example.com

=== URLs ===
https://www.example.com

=== Phone ===
(123) 456-7890

=== Credit_Cards ===
1234-5678-9012-3456

=== Time_12h ===
2:30 PM

=== Hashtags ===
#coding
#python
```

## Project Structure

```
alu_regex-data-extraction-username/
├── main.py              # Main script file
├── test_data.json      # Test data file
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Your Name
ALU Email: your.email@alustudent.com
