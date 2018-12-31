from flask import render_template, redirect,url_for
from feature_req import app, db
from feature_req.forms import RequestForm
from feature_req.models import Request


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
    allRequests = Request.query.all()
    return render_template("requests.html", title="home",requests= allRequests)


@app.route('/addRequest', methods=['GET','POST'])
def add():
    form = RequestForm()
    if form.validate_on_submit():
        request=Request(title= form.title.data, 
            description=form.description.data,
            product_area_id =form.productArea.data,
            client_id= form.client.data,
            target_date =form.targetDate.data,
            client_priority= form.clientPriority.data
            )
        db.session.add(request)
        db.session.commit()
        return redirect(url_for('requests'))
    return render_template('requestForm.html', title='add new', form=form)