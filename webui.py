from flask import Flask, render_template, request
import privateGPT  # the python file with the above script

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/query', methods=['POST'])
def query():
    question = request.form.get('question')
    answer = privateGPT.main(question)  # make sure your main function returns the answer and accepts a question as argument
    return render_template('answer.html', answer=answer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
