from flask import Flask, render_template, request, redirect

app = Flask(__name__)

"""
# The actual equivalent grammer used in parser
S  -> AB'C'
A  -> abA' | ab
A' -> abA' | ε
B  -> bB' | ε
B' -> cB' | ε
C  -> cC' | ε
C' -> cC' | ε
"""

class Parser:
    def __init__(self):
        self.first_sets = {}
        self.follow_sets = {}
        self.success = False  # Flag to indicate parsing success

    def parse(self,input_string):
        self.current_index = 0
        self.input_string = input_string
        if self.S():
            if self.current_index == len(self.input_string):
                self.success = True  # Set success flag if input is fully parsed
            else:
                self.success = False
        else:
            self.success = False

    def match(self, expected_token):
        if self.current_index < len(self.input_string) and self.input_string[self.current_index] == expected_token:
            self.current_index += 1
        else:
            raise ValueError(f"Expected '{expected_token}' but found '{self.input_string[self.current_index]}'")

    def compute_first_sets(self):
        for nt in ['S', 'A', 'B', 'C']:
            self.first_sets[nt] = set()

        self.first_sets['S'].add('a')
        self.first_sets['S'].add('b')
        self.first_sets['A'].add('a')
        self.first_sets['B'].add('b')
        self.first_sets['B'].add('c')
        self.first_sets['C'].add('c')

    def compute_follow_sets(self):
        for nt in ['S', 'A', 'B', 'C']:
            self.follow_sets[nt] = set()

        self.follow_sets['S'].add('$')  # End of input symbol
        self.follow_sets['S'].add('a')
        self.follow_sets['A'].add('a')
        self.follow_sets['A'].add('b')
        self.follow_sets['B'].add('a')
        self.follow_sets['B'].add('b')
        self.follow_sets['C'].add('a')
        self.follow_sets['C'].add('b')
        self.follow_sets['C'].add('c')

    def S(self):
        try:
            self.A()
            self.B()
            self.C()
            return True
        except ValueError:
            return False

    def A(self):
        try:
            self.match('a')
            self.match('b')
            self.A_prime()
            return True
        except ValueError:
            return False

    def A_prime(self):
        if self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'a':
            self.match('a')
            self.match('b')
            self.A_prime()
        else:
            return True

    def B(self):
        try:
            if self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'b':
                self.match('b')
            elif self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'c':
                self.C()
            return True
        except ValueError:
            return False

    def C(self):
        try:
            if self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'c':
                self.match('c')
                if self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'c':
                    self.C()
            return True
        except ValueError:
            return False


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_string = request.form['input_string']

        # Redirect to the result page
        return redirect('/result?input_string=' + input_string)

    # Render the input form template
    return render_template('input_form.html')


@app.route('/result')
def result():

    input_string = request.args.get("input_string","")

    # Create an instance of the parser
    parser = Parser()

    # Compute the First and Follow sets
    parser.compute_first_sets()
    parser.compute_follow_sets()

    # Parse the input string
    parser.parse(input_string)

    # Determine the result based on the parser's success flag
    result = 'Accepted' if parser.success else 'Rejected'

    # Print the result to the terminal
    print(f"Input String: {input_string}")
    print(f"First Sets: {parser.first_sets}")
    print(f"Follow Sets: {parser.follow_sets}")
    print(f"Result: {result}")

    # Render the result template with the computed sets
    return render_template('result.html', input_string=input_string, first_sets=parser.first_sets, follow_sets=parser.follow_sets, result=result)


if __name__ == '__main__':
    app.run(debug=True)