# -*- coding: utf-8 -*-
"""json-maker

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rx-HNFE-Gsj5cauLowvyjaVxMQUzP2GW
"""

import json
import re

def extract_placeholders(docx_content):
    placeholders = set()

    # Regular expression to match placeholders in the form {{text}}
    pattern = r"\{\{([^\}]*)\}\}"

    for line in docx_content.split('\n'):
        matches = re.findall(pattern, line)
        placeholders.update(matches)

    return placeholders

def create_json_from_placeholders(placeholders):
    data = {placeholder: "" for placeholder in placeholders}

    # Convert the dictionary to JSON string
    json_string = json.dumps(data, indent=2)

    return json_string

# input the text from docx file
docx_content = '''

{{reference_no}}
{{letter_date}}

{{insured_name}}
{{insured_address}}


{{attention_text}}
WITHOUT PREJUDICE

{{subject_text}}

{{opening_paragraph}}

{{doc_list}}

Thanking you and assuring you of our best and prompt services always.
Yours faithfully,

{{sender_name}}
Head of Claims
Encl: As started

Copy To:
{{copy_to_list}}

'''

placeholders = extract_placeholders(docx_content)
json_string = create_json_from_placeholders(placeholders)
print(json_string)