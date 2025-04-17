from time_parser import parse_time_expression


def main():
    """
    Simple CLI application for parsing relative time expressions
    like 'now()+1d+3h'.

    This script uses the parse_time_expression function
    to convert user-input strings
    into calculated UTC datetime values.
    """

    user_input = input("Enter time expression (e.g., 'now()+1d+3h'): ")
    try:
        parsed_time = parse_time_expression(user_input)
        print("Resulting UTC time:", parsed_time.isoformat() + "Z")
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
