from dave import app, db, admin
from flask import render_template, request, redirect, request, url_for, jsonify, flash
from dave.models import Tool, myModelView, User
from dave.forms import LoginForm
from flask_login import login_user, current_user, logout_user

admin.add_view(myModelView(Tool, db.session))
admin.add_view(myModelView(User, db.session))

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/languages')
def languages():
    return render_template('language.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/tools', methods=['POST', 'GET'])
def tools():
    if request.method == 'POST':
        try:
            data = request.form['aim']
            tool = Tool.query.filter(Tool.title.like('%'+data+'%')).first()
            data = { 'id': tool.id, 'title': tool.title}
            return jsonify(data)
        except:
            pass
    tools = Tool.query.all()
    return render_template('tools.html', tools=tools)

@app.route('/tool/<int:tool_id>')
def tool(tool_id, methods=['POST', 'GET']):
    tool = Tool.query.get_or_404(tool_id)
    return render_template('tool.html', tool=tool)

@app.route('/am7jymb6', methods=['POST'])
def login():
    user = User.query.filter_by(email=request.form['email']).first()
    if user and user.password == request.form['passwd']:
        login_user(user)
        flash('You are logged Successfully.', 'success')
    return redirect('/3xf8z81HUddaTkyqZBXJm9PG')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/3xf8z81HUddaTkyqZBXJm9PG')

@app.errorhandler(404)
def error_404(error):
    return render_template('error_404.html'), 404

@app.errorhandler(403)
def error_403(error):
    return render_template('error_403.html'), 403

@app.errorhandler(500)
def error_500(error):
    return render_template('error_500.html'), 500
