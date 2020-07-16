from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template("home_page.html")

@app.route('/result')
def result():
	username = request.args.get('username')
	params=[]
	upperflag = False
	lowerflag = False
	lastdigit = False
	failed = False
	for ele in username:
		if ele.isupper():
			upperflag = True
		if ele.islower():
			lowerflag = True
	lastdigit = username[-1].isdigit()
	if upperflag and lowerflag and lastdigit:
		pass
	
	else:
		failed=True

		if not(upperflag):
			params.append("You did not use an uppercase character")
		if not(lowerflag):
			params.append("You did not use an lower	case character")			
		if not(lastdigit):
			params.append("You did not end your username with a digit")
			

	return render_template("result.html",params = params,failed=failed)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

if __name__=="__main__":
	app.run(debug=True)