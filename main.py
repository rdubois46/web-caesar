from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

form = """
    <!DOCTYPE = HTML>
        <html>
            <head>
                <style>
                    form {{
                        background-color: #eee;
                        padding: 20px;
                        margin: 0 auto;
                        width: 540px;
                        font: 16px sans-serif;
                        border-radius: 10px;
                    }}
                    textarea {{
                        margin: 10px 0;
                        width: 540px;
                        height: 120px;
                    }}
                </style>
            </head>
            <body>
                <form action="/" method="POST">
                    <label for="rot">
                        Rotate by:
                        <input type="text" id="rot" name="rot" value="0" />
                    </label>
                    
                    <textarea name="text" id="text">
                    {0}              
                    </textarea>

                    <input type="submit" value="Submit Query">
                </form>
            </body>
        </html>
"""

@app.route("/")
def index():
    return form.format("")

# Within encrypt, store the values of these request 
# parameters in local variables, converting data types 
# as necessary. Then, encrypt the value of the text 
# parameter using rotate_string. Return the encrypted 
# string wrapped in <h1> tags, to be rendered in the browser.

@app.route("/", methods=['POST'])
def encrypt():
    rotation_number = int(request.form['rot'])
    user_string = request.form['text']

    encrypted_string = rotate_string(user_string, rotation_number)

    return form.format(encrypted_string)


app.run()