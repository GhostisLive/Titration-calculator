from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    calculation = None
    if request.method == 'POST':
        titrant = request.form.get("titrant")
        speed = request.form.get("speed")
        titrate = request.form.get("titrate")
        normality = float(request.form.get("normality", 0))  # Convert to float for calculations
        volume = float(request.form.get("volume", 0))  # Convert to float for calculations
        indicator = request.form.get("indicator")

        # Perform a basic calculation (example: amount of titrant needed)
        # Assuming normality (N) and volume (mL) of titrate, and a simple calculation
        # For demonstration purposes, let's assume the result is calculated as:
        calculation = normality * volume  # Example calculation, adjust as needed

        # Store the results in a dictionary to pass to the template
        result = {
            'titrant': titrant,
            'speed': speed,
            'titrate': titrate,
            'normality': f"{normality} N",
            'volume': f"{volume} ml",
            'indicator': indicator,
            'calculation': calculation 
        }

    return render_template('main.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
