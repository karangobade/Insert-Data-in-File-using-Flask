from flask import Flask,request,render_template,redirect

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/submit',methods=["POST","GET"])
def submit():
    text=request.form.get("text")
    
    if text=="":
        return redirect('/submit')
    
    with open("text.txt","a+") as f:
        f.write(f"{text}\n")
        f.close()

    return render_template("home.html")
    
    

    

if __name__=="__main__":
    app.run(debug=True)