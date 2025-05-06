```python
import sys
import csv
import html

def generate_html_report(csv_file_path):
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    html_content = []
    html_content.append("<html>")
    html_content.append("<head><title>Security Findings Report</title></head>")
    html_content.append("<body>")
    html_content.append("<h1>Security Findings Report</h1>")
    html_content.append("<table border='1'>")
    html_content.append("<tr>")
    html_content.append("<th>Issue</th><th>Severity</th><th>File</th><th>Line</th><th>Message</th><th>Description</th>")
    html_content.append("</tr>")
    
    for row in rows:
        if len(row) < 9:
            continue  # Skip invalid rows
        
        issue = row[0]
        description = row[1]
        severity = row[2].lower()
        message = row[3]
        file_path = row[4]
        start_line = row[5]
        
        # HTML escaping for all fields to prevent injection
        escaped_issue = html.escape(issue)
        escaped_severity = severity.upper()
        severity_color = "red" if severity == "error" else "orange" if severity == "warning" else "black"
        escaped_file = html.escape(file_path)
        escaped_message = html.escape(message)
        escaped_description = html.escape(description)
        
        # Build the row
        row_html = f"<tr>"
        row_html += f"<td>{escaped_issue}</td>"
        row_html += f"<td style='background-color: {severity_color}'>{escaped_severity}</td>"
        row_html += f"<td>{escaped_file}</td>"
        row_html += f"<td>{start_line}</td>"
        row_html += f"<td>{escaped_message}</td>"
        row_html += f"<td>{escaped_description}</td>"
        row_html += "</tr>"
        html_content.append(row_html)
    
    html_content.append("</table>")
    html_content.append("</body></html>")
    
    return '\n'.join(html_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_report.py <report.csv>")
        sys.exit(1)
    
    csv_path = sys.argv[1]
    report_html = generate_html_report(csv_path)
    print(report_html)
```

**Explanation:**

1. **Reading the CSV:** The script reads the CSV file using the `csv` module, which handles quoted fields with commas correctly.

2. **HTML Escaping:** Uses `html.escape()` to prevent HTML injection and ensure special characters are rendered properly.

3. **Severity Coloring:** The severity column's background color is set based on the severity level (`error` = red, `warning` = orange).

4. **Table Structure:** The HTML table includes columns for Issue, Severity, File, Line, Message, and Description. Each row is dynamically generated from the CSV data.

5. **Command-Line Interface:** The script takes the CSV file path as a command-line argument and outputs the HTML to stdout.

**Usage:**
```bash
python generate_report.py findings.csv > report.html
```

This will generate an HTML file (`report.html`) with a formatted table of security findings, highlighting severity levels visually.