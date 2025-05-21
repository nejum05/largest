from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        try:
            raw = request.form['numbers']
            n = int(request.form['n'])
            nums = [float(x) for x in raw.replace(',', ' ').split()]
            sorted_nums = sorted(nums, reverse=True)

            if n < 1 or n > len(sorted_nums):
                error = f"n must be between 1 and {len(sorted_nums)}"
            else:
                result = sorted_nums[n - 1]

        except ValueError:
            error = "Please enter valid numbers and an integer for n."
        except Exception as e:
            error = f"Unexpected error: {e}"

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
