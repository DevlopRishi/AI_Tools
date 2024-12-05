import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

class GoogleSheetsSync:
    def __init__(self, spreadsheet_id):
        # Setup Google Sheets API credentials
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'
        
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
        self.service = build('sheets', 'v4', credentials=credentials)
        self.spreadsheet_id = spreadsheet_id

    def get_all_tools(self):
        """Retrieve all AI tools from the spreadsheet"""
        sheet_range = 'Tools!A:F'  # Adjust range as needed
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id, 
            range=sheet_range
        ).execute()
        
        return result.get('values', [])

    def add_tool(self, tool_data):
        """Add a new tool to the spreadsheet"""
        sheet_range = 'Tools!A:F'
        value_input_option = 'RAW'
        
        values = [tool_data]
        body = {
            'values': values
        }
        
        result = self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id, 
            range=sheet_range,
            valueInputOption=value_input_option, 
            body=body
        ).execute()
        
        return result

    def update_tool(self, row_index, tool_data):
        """Update an existing tool in the spreadsheet"""
        sheet_range = f'Tools!A{row_index}:F{row_index}'
        value_input_option = 'RAW'
        
        body = {
            'values': [tool_data]
        }
        
        result = self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id, 
            range=sheet_range,
            valueInputOption=value_input_option, 
            body=body
        ).execute()
        
        return result

# Example usage
if __name__ == '__main__':
    SPREADSHEET_ID = 'your-spreadsheet-id'
    sheets_sync = GoogleSheetsSync(SPREADSHEET_ID)
    
    # Retrieve tools
    tools = sheets_sync.get_all_tools()
    
    # Add a new tool
    new_tool = ['Claude', 'https://claude.ai/', 'App', 'AI Chatbot', 'Text-based', 'Anthropic']
    sheets_sync.add_tool(new_tool)
