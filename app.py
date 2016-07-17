from flask import Flask
from flask import render_template
from flask import request


# instanitate an app
app = Flask(__name__)

# define what to return
@app.route('/')
def my_func(var1=0, var2=0, var3=0): # this call needs these default values provided in order to work

	# Extract the input variables from the url post
	var1 = request.args.get('var1', var1)
	var2 = request.args.get('var2', var2)
	var3 = request.args.get('var3', var3)

	# data preprocessing and validation
	var1 = float(var1)
	var2 = float(var2)
	var3 = float(var3)

	########################################################
	# Score thr input variables through a predictive model
	########################################################
	out1 = var1 + var2
	out2 = var3

	# pack the scored outputs into a dictionary to render in the browser
	context = {'out1' : out1, 'out2' : out2}

	# return the scored data
	return render_template("allinone.html", **context)




########################################################
# return the venues
########################################################
@app.route('/venues')
def return_event_pages():
	return render_template("venue_page.html")

########################################################
# Shutting down flask server
########################################################
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


# run the app
app.run(host='0.0.0.0')


