def getSelectedOption(options):
    selectedOption = ""

    while selectedOption not in options:
        for option in options:
            print(f"- {option}")

        selectMessage = "Please type one of the options from the list above: "
        selectedOption = input(selectMessage)

        if selectedOption in options:
            print(f"You selected {selectedOption}")

            break

        errorParts = [
            "Your selection is invalid",
            "Please make sure to type an option from the list bellow"
        ]

        for errorPart in errorParts:
            print(errorPart)

    return selectedOption
