import re
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


def parse_time_expression(expression: str, base_time: datetime = None) -> datetime:
    """
    Parses a relative time expression like 'now()+1d+3h' and returns the resulting UTC datetime.

    Args:
        expression (str): Relative time string, must start with 'now()'.
        base_time (datetime, optional): Allows injecting a fixed base time for testing.

    Returns:
        datetime: Resulting datetime object in UTC.
    """
    if not expression.startswith("now()"):
        raise ValueError("Expression must start with 'now()'")

    current_time = base_time or datetime.utcnow()

    # Correct regex order: longer units before shorter (e.g., 'mon' before 'm')
    pattern = r"([+-])(\d+)(mon|y|d|h|m|s)"
    expression_body = expression[5:]  # skip 'now()'

    matches = re.findall(pattern, expression_body)

    # Check that the entire string was matched — helps detect unknown units like 'x'
    reconstructed = "".join(f"{op}{val}{unit}" for op, val, unit in matches)
    if reconstructed != expression_body.replace(" ", ""):
        raise ValueError(
            f"Invalid or unsupported time unit in expression: '{expression}'"
        )

    for operator, value, unit in matches:
        amount = int(value)
        if operator == "-":
            amount *= -1

        if unit == "s":
            current_time += timedelta(seconds=amount)
        elif unit == "m":
            current_time += timedelta(minutes=amount)
        elif unit == "h":
            current_time += timedelta(hours=amount)
        elif unit == "d":
            current_time += timedelta(days=amount)
        elif unit == "mon":
            current_time += relativedelta(months=amount)
        elif unit == "y":
            current_time += relativedelta(years=amount)

    return current_time
