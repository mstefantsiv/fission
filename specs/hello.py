import os


def get_function_name():
    function_name = os.environ.get('FUNCTION_NAME')
    if function_name is None:
        raise EnvironmentError("Unable to retrieve function name.")
    return function_name


def main():
    # Usage
    function_name = get_function_name()
    print("Function name:", function_name)


if __name__ == "__main__":
    main()
