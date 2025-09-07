from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Guide, User
from . import db
from sqlalchemy import or_
from .forms import GuideForm
import markdown
from flask_login import login_required, logout_user, current_user
views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    
    search_query = ''
    
    if request.method == 'POST':
        search_query = request.form.get('search', "").strip()
        
        guides = Guide.query.filter(or_(
            Guide.title.ilike('%' + search_query + '%'),
            Guide.content.ilike('%' + search_query + '%')
        )).all()
        
    else:
        guides = Guide.query.all()
        
    return render_template('index.html', guides = guides, search_query = search_query)

@views.route('/add', methods = ['GET', 'POST'])
@login_required
def add():
    if current_user.role != 'admin':
        flash('You do not permission to access this page.', category = 'warning')
        
        return redirect(url_for('views.home'))
    
    form = GuideForm()
    
    if form.validate_on_submit():
        
       guide = Guide(title = form.title.data, content = form.content.data) 
       db.session.add(guide)
       db.session.commit()
       flash('Guide successfully added!', category='success')
        
       return redirect(url_for('views.home'))
   
    return render_template('add.html', form = form)

@views.route('/edit/<int:id>', methods = ['GET', 'POST'])
@login_required
def edit(id):
    if current_user.role != 'admin':
        flash('You do not permission to access this page.', category = 'warning')
        
        return redirect(url_for('views.home'))
    
    guide = Guide.query.get(id)
    form = GuideForm(obj=guide)
    
    if form.validate_on_submit():
        
        guide.title = form.title.data
        guide.content = form.content.data
        
        db.session.commit()
        
        flash('Guide successfully updated!', category='success')
        
        return redirect(url_for('views.home'))
        
    return render_template('add.html', form = form)


@views.route('/delete/<int:id>', methods = ['POST'])
@login_required
def delete(id):
    if current_user.role != 'admin':
        flash('You do not permission to access this page.', category = 'warning')
        
        return redirect(url_for('views.home'))
    
    guide = Guide.query.get(id)
    
    db.session.delete(guide)
    db.session.commit()
    
    flash('Guide successfully deleted!', category='success')
    
    return redirect(url_for('views.home'))

@views.route('/view_guides/<int:id>')
@login_required
def view_guides(id):
    guide = Guide.query.get(id)
    
    html_content = markdown.markdown(guide.content)
    
    return render_template('view_guides.html', guide = guide, content = html_content)

@views.route('/logout')
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('auth.login'))

@views.route('/users', methods = ['GET', 'POST'])
@login_required
def users():
    if current_user.role != 'admin':
        flash('You do not permission to access this page.', category = 'warning')
        
        return redirect(url_for('views.home'))
        
    search_query = ''
    
    if request.method == 'POST':
        search_query = request.form.get('search', "").strip()
        
        users = User.query.filter(or_(
            User.email.ilike('%' + search_query + '%'),
            User.first_name.ilike('%' + search_query + '%'),
            User.last_name.ilike('%' + search_query + '%')
        )).order_by(User.last_name).all()
    else:
        users = User.query.order_by(User.last_name).all()
        
    return render_template('users.html', users = users, search_query = search_query)

@views.route('/view_user/<int:id>', methods = ['GET', 'POST'])
@login_required
def view_user(id):
    if current_user.role != 'admin':
        flash('You do not permission to access this page.', category = 'warning')
        
        return redirect(url_for('views.home'))
    
    user = User.query.get(id)
    
    if request.method == 'POST':
        role = request.form.get('role').lower()
        
        user.role = role
        db.session.commit()
        
        return redirect(url_for('views.view_user', id = user.id))
        
    return render_template('view_user.html', user = user)