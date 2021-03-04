from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

class ToDo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __rep__(self):
        return '<Task %r>' %self.id
        #when the method is invoked it returns the task and the id of the task

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        # retrives the user input using the field name 'content'
        task_content=request.form['content']
        #create an instant of the database model
        new_task=ToDo(content=task_content)

        #push the new task to the database
        try:
            db.session.add(new_task)
            db.session.commit()
            # redirect back to the index page
            return redirect('/')
        except:
            return "Oops We ran into an error!!"
    else:
        task=ToDo.query.order_by(ToDo.date_created).all()
        return render_template('index.html',tasks=task)
#create a separate route for deleting the tasks 
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete=ToDo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Oops we encountered a problem deleting your task"
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    task_to_update=ToDo.query.get_or_404(id)
    if request.method=='POST':        
        task_to_update.content=request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Issue updating the task"
    else:
        return render_template('update.html',task=task_to_update)
    



if __name__=="__main__":
    app.run(debug=True)

