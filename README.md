# Calculator CLI  

A simple and lightweight **command-line calculator** built with [Typer](https://typer.tiangolo.com/).  
This tool allows you to quickly perform basic arithmetic operations (addition, subtraction, multiplication, and division) directly from your terminal.  

---

## ✨ Features  

- Add, subtract, multiply, and divide numbers from the command line  
- Simple and intuitive CLI built with **Typer**  
- Handles division by zero safely  
- Installable as a Python package with a `calc` command  

---

## 📦 Installation  

Clone the repository and install with `pip`:  

```bash
git clone https://github.com/antonioIannotta/calculator-cli.git
cd calculator-cli
pip install .
```
This will install the CLI under the command calc.
If you want a development setup:

```bash
pip install -e .
```

## 🚀 Usage
Once installed, type calc --help to see available commands:
```bash
calc --help
```

Output:

```vbnet
Usage: calc [OPTIONS] COMMAND [ARGS]...

  A simple command line calculator.

Options:
  --help  Show this message and exit.

Commands:
  div  Divide two numbers
  mul  Multiply two numbers
  sub  Subtract two numbers
  sum  Add two numbers
```
## Examples
### Addition
```bash
calc sum 5 3
```
Output: 8.0

### Subtraction
```bash
calc sub 10 4
```

Output: 6.0

### Multiplication
```bash
calc mul 7 6
```
Output: 42.0

### Division
```bash
calc div 8 2
```
Output: 4.0

### Division by zero:
```bash
calc div 5 0
```
Raises: ZeroDivisionError