from flask import Flask, request, jsonify
import json
import re

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h2>Text Converter</h2>

    <label for="input-text">Input Text:</label><br>
    <textarea id="input-text" placeholder="Enter text here"></textarea><br><br>

    <button onclick="convertText()">Convert</button><br><br>

    <label for="output-text">Output Text:</label><br>
    <textarea id="output-text" placeholder="Output will appear here" readonly></textarea>

    <script>
        function convertText() {
            var inputText = document.getElementById('input-text').value;
            fetch('/convert', {
                method: 'POST',
                body: JSON.stringify({text: inputText}),
                headers:{
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.text())
            .then(data => {
                document.getElementById('output-text').value = data;
            });
        }
    </script>
    '''

@app.route('/convert', methods=['POST'])
def convert():
    def extract_placeholders(docx_content):
        placeholders = []
    
        # Regular expression to match placeholders in the form {{text}}
        pattern = r"\{\{([^\}]*)\}\}"
    
        for line in docx_content.split('\n'):
            matches = re.findall(pattern, line)
            for match in matches:
                if match not in placeholders:
                    placeholders.append(match)
    
        return placeholders

    def create_json_from_placeholders(placeholders):
        data = {}
        for placeholder in placeholders:
            data[placeholder] = ""
    
        # Convert the dictionary to JSON string
        json_string = json.dumps(data, indent=2)
    
        return json_string

    text = request.json['text']
    placeholders = extract_placeholders(text)
    json_string = create_json_from_placeholders(placeholders)
    
    return json_string

if __name__ == '__main__':
    app.run()
