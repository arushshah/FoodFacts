from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
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
    
# Run the app :)
if __name__ == '__main__':
  app.run(debug=True)