from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def about_me(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("database.txt", "a") as file:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        databaza = file.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open("database.csv", newline='',"a") as file2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer = csv.writer(file2, delimiter=",")
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "couldnot save to database"
    else:
        return "something went wrong"
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    
