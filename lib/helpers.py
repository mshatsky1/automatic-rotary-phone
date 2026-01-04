# Helper functions

def helper_function_2(x):
    """Helper function for iteration 2."""
    return x * 2

def format_output(data):
    """Format output data."""
    return str(data).upper()

def sanitize_input(input_str):
    """Sanitize user input."""
    if not isinstance(input_str, str):
        return str(input_str)
    return input_str.strip().replace("\n", "").replace("\r", "")
