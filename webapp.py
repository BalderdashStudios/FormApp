from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
@app.route("/p3")
def render_page3():
    return render_template('page3.html')
    
@app.route("/temp")
def render_temp():
    return render_template('RepairsForms/YearNumber.html')

@app.route("/yearNumber")
def render_yearNumber():
    proccesor = request.args['proccesor']
    
    return render_template('RepairsForms/YearNumber.html')



    
if __name__=="__main__":
    app.run(debug=False)


#Dictionary

my_dictionary = {
    "car" : "an automobile",
    "fact": "something that actually exists; reality, truth"
}

#First is key, second is value. print(md["the"]) |  md["dog"] = md["dog"]+1 | if "hi" id md keys