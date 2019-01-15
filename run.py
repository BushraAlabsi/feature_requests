from feature_req import create_app

app = create_app()
print(app)
if __name__ == '__main__':
	app.run(debug=False)
