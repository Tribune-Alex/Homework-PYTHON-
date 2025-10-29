def camel_to_snake(name):
    result = ""
    for char in name:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result.lstrip('_')

print(camel_to_snake("AlexTodua"))
print(camel_to_snake("LovesJavaScript"))
print(camel_to_snake("LovesPython"))
print(camel_to_snake("LovesWeb"))