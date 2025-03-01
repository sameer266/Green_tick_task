# Security Scanner

A Django-based web application for scanning log files for suspicious activity and checking websites for security vulnerabilities.

## Features
- **Log File Scanner:** Detects suspicious patterns like failed login attempts.
- **Website Security Scanner:** Checks for missing security headers, outdated software, and insecure forms.

## Requirements
- Python 3.x
- Django
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/sameer266/Green_tick_task.git
    ```


3. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```
    
3. Navigate to the project directory:
    ```bash
    cd project
    ```


4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run database migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

## Usage
### **Log File Scanner**
1. Upload a log file via the web interface.
2. The system scans for suspicious activity and displays alerts.

### **Website Security Scanner**
1. Enter a URL to scan.
2. The system checks for missing headers, outdated software, and insecure forms.
3. A vulnerability report is displayed.

## Example Output
```
Alert: Unauthorized access attempt detected at 2025-03-01 12:30:45
Missing Security Headers: Strict-Transport-Security
Outdated Software Version Detected: Apache/2.2.0
Form without proper Method Attribute: /login
```

## Contributing
Pull requests are welcome! Please follow best coding practices and include relevant documentation.

## License
This project is open-source and available under the [MIT License](LICENSE).

