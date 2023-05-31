# Non Recursive Predictive Parser

This is a Python implementation of a Non Recursive Predictive Parser. It can be used to parse a given input string based on a specific grammar.

You can also find it hosted at [parser.aayushpokharel.com](https://parser.aayushpokharel.com)

## Grammer Used

This is the original grammer that was used to design the parser.
```
S -> ABC
A -> abA | ab
B -> b | BC
C -> c | cC
```
This is the equivaltent grammer used to implement the parser after removing ambiguities and immediate left-recursion.
```
S  -> AB'C'
A  -> abA' | ab
A' -> abA' | ε
B  -> bB' | ε
B' -> cB' | ε
C  -> cC' | ε
C' -> cC' | ε
```

## Requirements

- Python 3.x
- Flask

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/AayushPokharel/CompilerParser.git
   ```

2. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:

   ```
   python app.py
   ```

4. Open your web browser and visit `http://localhost:5000` to access the application.

## Usage

1. Enter an input string in the provided input form.
2. Click the "Parse" button to parse the input string.
3. The application will display the result of the parsing process, along with the computed First and Follow sets.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Simply copy the content and paste it into your README.md file. Remember to adjust any URLs or project-specific details as needed.
