from datetime import datetime
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
    return "Hello World"

    # today = datetime.today().strftime("%B %-d, %Y")
    # rendered_template = render_template('invoice.html',
    #                                     date=today)
    #
    # html = HTML(string=rendered_template)
    # rendered_pdf = html.write_pdf('./static/invoice.pdf')
    # return send_file("./static/invoice.pdf")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


#
# html = HTML('invoice.html')
# html.write_pdf('invoice.pdf')
