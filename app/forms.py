from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Home page with search field
@app.route('/index/', methods=['POST', 'GET'])
def index():
    return render_template('form_submit.html')


# shows results of food search
@app.route('/results/', methods=['POST'])
def results():
    name=request.form['yourname']
    food_data = []
    
    data = open("data.csv", "r")
    counter = 0
    
    for row in data:
    	parts = row.split(",")
    	if name.replace(" ","").lower()[0:2] == parts[0].replace(" ","").lower()[0:2]:
           counter += 1
    	   for i in range(12):
    		  food_data.append(parts[i])
    	   break
        
    if counter == 0:
        return render_template('form_action.html', found=False)

    return render_template('form_action.html', name=name, data = parts, found=True)
    
if __name__ == '__main__':
  app.run(debug=True)
