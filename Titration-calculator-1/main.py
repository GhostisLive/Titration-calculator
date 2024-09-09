from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        # Get form data with default values if not provided
        titrant = request.form.get("titrant", "Not specified")
        speed = request.form.get("speed", "Not specified")
        titrate = request.form.get("titrate", "Not specified")
        normality = request.form.get("normality", "0.0")
        volume = request.form.get("volume", "0.0")
        indicator = request.form.get("indicator", "Not specified")
        
        try:
            # Convert to float for calculations
            normality = float(normality)
            volume = float(volume)
            
            # Perform a basic calculation (example: amount of titrant needed)
            calculation = normality * volume  # Example calculation, adjust as needed

            # Store the results in a dictionary to pass to the template
            result = {
                'titrant': titrant,
                'speed': speed,
                'titrate': titrate,
                'normality': f"{normality} N",
                'volume': f"{volume} ml",
                'indicator': indicator,
                'calculation': f"{calculation:.2f}"  # Format result to two decimal places
            }
        except ValueError:
            # Handle the case where conversion to float fails
            result = {
                'error': 'Invalid input for normality or volume. Please enter valid numbers.'
            }

    return render_template('main.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
