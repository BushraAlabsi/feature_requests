from flask import render_template
from feature_req import app
from feature_req.forms import RequestForm


requests1 = [
    {
        'title': 'Corey Schafereeee',
        'description': 'Blog Post 1',
        'client': 'First post content',
        'target_date': 'April 20, 2018',
        'area': 'pa1',
        'client_priority':'1'
    },
    {
        'title': 'Jane Doe',
        'description': 'Blog Post 2',
        'client': 'Second post content',
        'target_date': 'April 21, 2018',
        'area': 'pa2',
        'client_priority':'2'
    }
]

@app.route("/")
@app.route("/requests")
def requests():
    return render_template("requests.html", title="home",requests= requests1)


@app.route('/addRequest')
def add():
	form = RequestForm()
	if form.validate_on_submit():
		print(form.title.data)
	return render_template('requestForm.html', title='add new', form=form)
	