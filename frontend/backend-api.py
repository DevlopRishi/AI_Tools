from flask import Flask, jsonify, request
from flask_cors import CORS
from google_sheets_sync import GoogleSheetsSync

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Google Sheets configuration
SPREADSHEET_ID = 'your-spreadsheet-id'
sheets_sync = GoogleSheetsSync(SPREADSHEET_ID)

@app.route('/api/tools', methods=['GET'])
def get_tools():
    """Retrieve all AI tools"""
    tools_data = sheets_sync.get_all_tools()
    
    # Convert raw data to structured JSON
    tools = [
        {
            'name': row[0],
            'link': row[1],
            'type': row[2],
            'category': row[3] if len(row) > 3 else 'Uncategorized'
        }
        for row in tools_data[1:]  # Skip header row
    ]
    
    return jsonify(tools)

@app.route('/api/tools', methods=['POST'])
def add_tool():
    """Add a new tool"""
    tool_data = request.json
    
    # Validate input
    required_fields = ['name', 'link', 'type', 'category']
    if not all(field in tool_data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Convert to row format for Google Sheets
    row_data = [
        tool_data['name'], 
        tool_data['link'], 
        tool_data['type'], 
        tool_data['category']
    ]
    
    sheets_sync.add_tool(row_data)
    return jsonify({'message': 'Tool added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)