from flask import Flask, render_template, request, redirect, url_for

from bayes import compute_posterior

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        try:
            p_a = float(request.form['p_a'])
            p_b_given_a = float(request.form['p_b_given_a'])
            p_b_given_not_a = float(request.form['p_b_given_not_a'])
            result = compute_posterior(p_a, p_b_given_a, p_b_given_not_a)
        except (ValueError, KeyError) as e:
            error = 'Invalid input: ' + str(e)
        except ZeroDivisionError as e:
            error = str(e)
    return render_template('form.html', result=result, error=error)


if __name__ == '__main__':
    app.run(debug=True)
