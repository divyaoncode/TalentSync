from flask import Flask, render_template, request, redirect, session, url_for
import database

app = Flask(__name__)
app.secret_key = 'talentsync_secret_key'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = database.get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['role'] = user['role']
            session['name'] = user['name']
            session['cgpa'] = user['cgpa']
            
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('student_dashboard'))
        else:
            return "Invalid Credentials! Please try again."
            
    return render_template('login.html')

@app.route('/student_dashboard')
def student_dashboard():
    if 'user_id' not in session or session['role'] != 'student':
        return redirect(url_for('login'))
        
    student_cgpa = session['cgpa']
    
    conn = database.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM jobs WHERE min_cgpa <= %s"
    cursor.execute(query, (student_cgpa,))
    eligible_jobs = cursor.fetchall()
    conn.close()
    
    return render_template('student_dashboard.html', name=session['name'], jobs=eligible_jobs)

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
        
    conn = database.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """
        SELECT users.name, users.branch, jobs.company_name, jobs.job_role, applications.status 
        FROM applications 
        JOIN users ON applications.student_id = users.id 
        JOIN jobs ON applications.job_id = jobs.id
    """
    cursor.execute(query)
    applications = cursor.fetchall()
    conn.close()
    
    return render_template('admin_dashboard.html', name=session['name'], applications=applications)

if __name__ == '__main__':
    app.run(debug=True)