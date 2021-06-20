def getModuleLikePath(string):
    return string.replace(
        "./", ""
    ).replace(
        ".py", ""
    ).replace(
        "/", "."
    ).replace(
        "\\", "."
    )