# AI Tools Directory

## Overview
A web application for tracking and filtering AI tools, with a Google Sheets backend for easy management.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Google Cloud Project with Sheets API enabled
- Service Account Credentials

### Backend Setup
1. Clone the repository
2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Google Sheets
   - Create a Google Cloud Project
   - Enable Sheets API
   - Create a service account
   - Download service account key
   - Share your Google Sheet with the service account email

5. Configure environment variables
   - Set `SPREADSHEET_ID` in the script
   - Set path to service account JSON file

### Running the Application
```bash
# Run Flask backend
python app.py

# For production, use gunicorn
gunicorn app:app
```

## Deployment Considerations
- Use a production-ready WSGI server like Gunicorn
- Set up HTTPS
- Implement proper authentication for adding/editing tools