from flask import Flask, render_template, url_for, request

app = Flask(__name__)

def spring_calculate(user_height, user_width):
    # create a nested list of the data we want to iterate through
    springs =   [[range(1980, 2196, 1), range(2000, 2415, 1), "1 X C680"],
                [range(2197, 2285, 1), range(2000, 2415, 1), "1 X D815"],
                [range(1980, 2285, 1), range(2416, 2600, 1), "1 X D780"],
                [range(1980, 2196, 1), range(2600, 2750, 1), "1 X D740"],
                [range(2196, 2285, 1), range(2600, 2750, 1), "1 X E910"],
                [range(1980, 2285, 1), range(2751, 2900, 1), "1 X E880"],
                [range(1980, 2285, 1), range(2901, 3000, 1), "1 X E880"],
                [range(1980, 2196, 1), range(3001, 3200, 1), "1 X E795"],
                [range(2197, 2285, 1), range(3001, 3201, 1), "1 X F905"],]

    # iterate through nested list 
    for spring in springs:
        if (user_height in spring[0]) and (user_width in spring[1]):
            print(spring[2])
            answer = spring[2]
            return answer

    return "spring not found"

@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        user_height = int(request.form.get('user_height'))
        user_width = int(request.form.get('user_width'))
        
        return render_template('form.html', spring = spring_calculate(user_height, user_width))
    
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=False)