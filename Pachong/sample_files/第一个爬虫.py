import csv

def getweb():
    file = open('E:/python/爬虫/sample_files/sample.html', mode='r',encoding='UTF-8')
    return file.readlines()

#web = getweb()
#print(web)

def extract_text(html_string):
    lines = []
    for line in html_string:
        new_line = line.strip()
        if new_line.endswith('</td>'):
            formatted = new_line.strip('</td>').split('>')[-1]
            lines.append(formatted)
    return lines

#html_string=getweb()
#web = extract_text(html_string)
#print(web)

def format_lines(lines):
    unit = []
    formatted_lines = [
        ['Account','Due Date','Amount','Date'],
    ]

    for line in lines:
        unit.append(line)
        if len(unit) == 4:
            formatted_lines.append(unit)
            unit = []

    return formatted_lines


def to_csv(formtted_string):
    file = open('result.csv','w+')
    writer = csv.writer(file)
    for unit in formtted_string:
        writer.writerow(unit)

def main():
    html_string = getweb()
    cleaned_text = extract_text(html_string)
    l = format_lines(cleaned_text)
    to_csv(l)

main()




