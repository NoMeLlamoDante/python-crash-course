# Strings
language = " python "
languages = "Langages:\nPython\nC\nJavascript"
# Tabulation
print(f"\t{language}")
# New Line
print(f"{languages}")
# Stripping White Spaces
print(f"'{language.rstrip()}'")
print(f"'{language.lstrip()}'")
print(f"'{language.strip()}'")
# Remove prefixes
url = "https://www.youtube.com"
simple_url = url.removeprefix("https://")
print(simple_url)

