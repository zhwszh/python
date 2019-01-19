
def get_html()
    file = open('./web_sample/sample.html', 'r')
    return file.readlines()

def extrat_text(html_string):
    lines = []
    for line in html_string:
        new_line = line.strip()
        if new_line.endswith('</td>'):
            formatted = new_line.strip('</td>').split('>')[-1]
            lines.append(formatted)
    return lines

def format_lines(lines):
    unit = []
    formatted_lines = [
        ['Account', 'Due Date', 'Amount', 'Date'],
    ]
    for line in lines:
        unit.append(line)
        if len(unit) == 4:
            formatted_lines.append(unit)
            unit = []
    return formatted_lines

def to_csv(formatted_string)
    pass

html_string = getweb()
cleaned_text = extract_text(html_string)
l = format_lines(cleaned_text)
print(l)