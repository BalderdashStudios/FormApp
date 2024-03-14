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

@app.route("/computerSelect")
def render_PPCSelect():
    proccesor = request.args['proccesor']
    
    if proccesor == "ppc":
        return render_template('RepairsForms/PPCSelect.html')
    elif proccesor == "intel":
        return render_template('RepairsForms/IntelSelect.html')

@app.route("/modelSelect")
def render_modelSelect():
    macModel = request.args['macModel']
    
    #PPC
    if macModel == "iMacG3":
        return render_template('RepairsForms/YearNumberG3.html')
    elif macModel == "iMacG4":
        return render_template('RepairsForms/IntelSelect.html')
    elif macModel == "iMacG5":
        return render_template('RepairsForms/IntelSelect.html')
    elif macModel == "PowerMacG4":
        return render_template('RepairsForms/IntelSelect.html')
    elif macModel == "PowerMacG5":
        return render_template('RepairsForms/IntelSelect.html')
    #Intel
    
    
    
@app.route("/infoComputer")
def render_infoComputer():
    version = request.args['version']
    
    #PPC G3
    if version == "1998OG":
        title = "1998 iMac G3"
        description = "The origional iMac."
        actions = "One important thing to be done to any iMac is to replace its clock battery also known as PRAM, or just C Battery. Here is a link to an iFixIt guide on how to do this. The reason we recomend this is due to the fact that these batties tend to leak and cause corrosion over time."
        imageMac = "Imac_G3_Bondi_Blue_side.jpg"
    elif version == "1998Late":
        title = "Late 1998 iMac G3"
        description = "The first revision of the iMac G3."
        actions = "One important thing to be done to any iMac is to replace its clock battery also known as PRAM, or just C Battery. Here is a link to an iFixIt guide on how to do this. The reason we recomend this is due to the fact that these batties tend to leak and cause corrosion over time."
        imageMac = "Imac_G3_Bondi_Blue_side.jpg"
    elif version == "1999OG":
        title = "1999 iMac G3"
        description = "This iMac G3 was the first revision to increase the clock speed of the Power PC G3 chip from 233 MHz to 266MHz."
        actions = "One important thing to be done to any iMac is to replace its clock battery also known as PRAM, or just C Battery. Here is a link to an iFixIt guide on how to do this. The reason we recomend this is due to the fact that these batties tend to leak and cause corrosion over time."
        imageMac = "Imac_G3_5_flavors_side_lineup.jpg"
    elif version == "1999Early":
        title = "333MHz 1999 iMac G3"
        description = "This iMac G3 increased the clock speed of the Power PC G3 chip from 266 MHz to a whopping 333MHz."
        actions = "One important thing to be done to any iMac is to replace its clock battery also known as PRAM, or just C Battery. Here is a link to an iFixIt guide on how to do this. The reason we recomend this is due to the fact that these batties tend to leak and cause corrosion over time."
        imageMac = "Imac_G3_5_flavors_side_lineup.jpg"
    elif version == "1999SG":
        title = "Second Generation iMac 1999"
        description = "This was the first of the second generation of the iMac G3, the most noticble feature is the new slot loading CD/DVD drive."
        actions = "One important thing to be done to any iMac is to replace its clock battery also known as PRAM, or just C Battery. Here is a link to an iFixIt guide on how to do this. The reason we recomend this is due to the fact that these batties tend to leak and cause corrosion over time."
        imageMac = "Imac_G3_Graphite_side.jpg"
    elif version == "2000OG":
        title = "2000 iMac G3"
        description = "This was the first iMac released in the 21st century. Woah."
        actions = "One important thing to be done to any iMac is to replace its clock battery also known as PRAM, or just C Battery. Here is a link to an iFixIt guide on how to do this. The reason we recomend this is due to the fact that these batties tend to leak and cause corrosion over time."
        imageMac = "Imac_G3_5_flavors_side_lineup.jpg"
    elif version == "2001OG":
        title = "2001 iMac G3"
        description = "These iMacs came in some intresting colors, if you've recently picked one of these up check if it's one of the rarier Blue Dalmatian or Flower Power colors."
        actions = "One important thing to be done to any iMac is to replace its clock battery also known as PRAM, or just C Battery. Here is a link to an iFixIt guide on how to do this. The reason we recomend this is due to the fact that these batties tend to leak and cause corrosion over time."
        imageMac = "Imac_G3_5_flavors_side_lineup.jpg"
    elif version == "2001Late":
        title = "Late 2001 iMac G3"
        description = "This was the last ever iMac G3 revision. It's G3 chip ranged from 500MHz to 700MHz."
        actions = "One important thing to be done to any iMac is to replace its clock battery also known as PRAM, or just C Battery. Here is a link to an iFixIt guide on how to do this. The reason we recomend this is due to the fact that these batties tend to leak and cause corrosion over time."
        imageMac = "Imac_G3_5_flavors_side_lineup.jpg"
    return render_template('RepairsForms/iMacG3/iMacG3.html' , title = title, description = description, actions = actions, imageMac = imageMac)
  
    
    
    
    

    
if __name__=="__main__":
    app.run(debug=True)


#Dictionary

my_dictionary = {
    "car" : "an automobile",
    "fact": "something that actually exists; reality, truth"
}

#First is key, second is value. print(md["the"]) |  md["dog"] = md["dog"]+1 | if "hi" id md keys