""" Component 5 - statement formatter v1
"""

symbol = "*"
text = "Maori Quiz"
sides = "$" * 5

formatted_text = f"{sides} {text} {sides}"
top_bottom = "*" * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)