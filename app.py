from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/regex', methods=['GET', 'POST'])
def regex_matcher():
    result = ''
    highlighted_text = ''
    matches = []
    case_insensitive = False
    
    if request.method == 'POST':
        # Check if 'pattern' and 'text' are in the form data
        pattern = request.form.get('pattern', '')
        text = request.form.get('text', '')
        case_insensitive = 'case_insensitive' in request.form  # Check if the option is selected
        
        if pattern and text:  # Ensure both fields are filled
            try:
                # Attempt to compile the regex pattern to ensure it's valid
                flags = re.IGNORECASE if case_insensitive else 0
                compiled_pattern = re.compile(pattern, flags)

                matches = compiled_pattern.findall(text)  # Find all matches

                if matches:
                    result = "✅ Matches found:"
                    # Highlight matches in the text
                    highlighted_text = re.sub(f'({re.escape(pattern)})', r'<span class="highlight">\1</span>', text, flags=flags)
                else:
                    result = "❌ No matches found."
            except re.error:
                result = "⚠️ Invalid regex pattern."
        else:
            result = "⚠️ Please fill in both the pattern and text fields."

    return render_template('regex_matcher.html', result=result, matches=matches, highlighted_text=highlighted_text)

@app.route('/email', methods=['GET', 'POST'])
def email_validator():
    result = ''
    
    if request.method == 'POST':
        if 'refresh' in request.form:
            # Clear the result when the refresh button is clicked
            result = ''
        else:
            email = request.form.get('email', '')
            # Improved regex pattern for email validation
            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            
            if re.match(email_pattern, email):
                result = "✅ This is a valid email address!"
            else:
                result = "❌ This is not a valid email address."

    return render_template('email_validator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
