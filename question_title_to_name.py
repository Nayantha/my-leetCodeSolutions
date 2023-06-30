def main():
    name = input("Enter the question title:")
    file_name = name.strip().replace(" ", "_").lower()
    print(file_name)
    return file_name


if __name__ == '__main__':
    main()
