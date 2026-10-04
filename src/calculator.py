from simpleeval import SimpleEval
from simpleeval import InvalidExpression
ALLOWED_FUNCTIONS = {}
ALLOWED_NAMES = {}
def calculate(expression):
    if not expression or not expression.strip():
        return None, "Expression is empty"
    s = SimpleEval(functions=ALLOWED_FUNCTIONS, names=ALLOWED_NAMES)
    try:
        result = s.eval(expression)
    except (InvalidExpression, SyntaxError):
        return None, "Invalid expression"
    except ZeroDivisionError:
        return None, "Cannot divide by zero"
    except Exception as e:
        return None, f"Error: {str(e)}"
    if isinstance(result, float):
        result = round(result, 10)
    return result, None