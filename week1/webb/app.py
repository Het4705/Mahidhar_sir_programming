from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)

#*Data storage in memory (for demonstration purposes)
data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    email = request.form.get('email')

    # Append data to the in-memory list (you might want to use a database in a real-world scenario)
    data.append({'Name': name, 'Age': age, 'Email': email})

    return redirect('/')

@app.route('/download')
def download():
    # Create a Pandas DataFrame from the collected data
    df = pd.DataFrame(data)

    # Determine the path to the static directory
    static_dir = os.path.join(app.root_path, 'static')

    # Save the DataFrame to an Excel file in the static directory
    excel_path = os.path.join(static_dir, 'collected_data.xlsx')
    df.to_excel(excel_path, index=False)

    # Provide the Excel file for download
    return redirect('/static/collected_data.xlsx')


if __name__ == '__main__':
    app.run(debug=True)
