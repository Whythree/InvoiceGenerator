from datetime import datetime
from functools import reduce
from weasyprint import HTML
import flask
import os
from flask import Flask, render_template, send_file,request

app = Flask(__name__)

@app.route("/")
#Von Home muss eine JSON an /create-invoice gesendet werden mit einer Form.
def home():
    print("Hello World")
    return render_template("home.html")


@app.post("/create-invoice")
def create_invoice():
    request_data = request.get_json()
    # ToDo Feed request data to template and build pdf
    print(f"Submitted Data: {request_data}")


    # Sum nimmt eine Liste
    # Ich brauche also eine Liste - Ich habe ja schon eine Liste an Dictionaries
    total_sum = 0


    print(f"Total Sum: {total_sum}")


    today = datetime.today().strftime("%B %-d, %Y")
    rendered_template = render_template('invoice.html',
                                        date=today,
                                        items = request_data
                                        )

    html = HTML(string=rendered_template)
    rendered_pdf = html.write_pdf('./static/invoice.pdf')
    return send_file("./static/invoice.pdf",None,True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


#
# html = HTML('invoice.html')
# html.write_pdf('invoice.pdf')
