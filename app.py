


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def return_event_pages():
	return render_template("main_page.html")


app.run(debug=True)
