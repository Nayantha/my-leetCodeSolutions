def main():
    name = input("Enter the question title:")
    file_name = name.strip().replace(" ", "_").replace("-", "_").lower()
    print(file_name)
    with open(f"{file_name}.py", "w") as new_solution_file:
        ...
    # with open(f"./tests/test_{file_name}.py", "w") as new_test_solution_file:
    #     ...
    return file_name


if __name__ == '__main__':
    main()
