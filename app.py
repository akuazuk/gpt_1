from flask import Flask, render_template, request

from bankruptcy import bankruptcy_probabilities

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    probabilities = None
    params = {}
    if request.method == 'POST':
        try:
            params['target_cash'] = float(request.form['target_cash'])
            params['weekly_min'] = float(request.form['weekly_min'])
            params['weekly_max'] = float(request.form['weekly_max'])
            params['high_risk_day'] = int(request.form.get('high_risk_day', 30))
            params['prob_at_high_risk'] = float(request.form.get('prob_at_high_risk', 0.8))
            params['bankruptcy_day'] = int(request.form.get('bankruptcy_day', 37))

            probs_min = bankruptcy_probabilities(
                params['target_cash'],
                params['weekly_min'],
                params['high_risk_day'],
                params['prob_at_high_risk'],
                params['bankruptcy_day'],
            )
            probs_max = bankruptcy_probabilities(
                params['target_cash'],
                params['weekly_max'],
                params['high_risk_day'],
                params['prob_at_high_risk'],
                params['bankruptcy_day'],
            )
            days = list(range(1, params['bankruptcy_day'] + 1))
            probabilities = {'days': days, 'min': probs_min, 'max': probs_max}
        except (ValueError, KeyError) as e:
            params['error'] = str(e)
    return render_template('form.html', params=params, probabilities=probabilities)


if __name__ == '__main__':
    app.run(debug=True)
