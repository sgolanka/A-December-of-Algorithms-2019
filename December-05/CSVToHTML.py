# ---> Convert csv to html table <--- #
def convert_to_html(txt, num):
    """
    Convert a line of a csv file to a line of an html table
    :param txt: a String containing a line from a csv file
    :param num: an integer identifying which line this is (starting at 0)
    :return this_line: A line of an html table equivalent to txt
    """
    this_line = '<tr>'

    # line zero is assumed to be header row
    if num == 0:
        tag = '<th>'
        end_tag = '</th>'
    else:
        tag = '<td>'
        end_tag = '</td>'

    while ',' in txt:
        com_pos = txt.index(',')
        segment = txt[:com_pos]
        this_line += tag + segment + end_tag
        txt = txt[com_pos + 1:]
    this_line += tag + txt.strip() + end_tag
    this_line += '</tr>'

    return this_line


# set up sections of html file in separate strings
html_head = '<html>\n\t<body>\n\t\t<table>'
html_data = '\t\t\t'
html_foot = '\t\t</table>\n\t</body>\n</html>'

# read each line, convert to html, add to html_data
line_num = 0
with open('txt/data.csv', 'r') as csv_file:
    for line in csv_file:
        html_data += convert_to_html(line, line_num) + '\n\t\t\t'
        line_num += 1
    html_data = html_data.rstrip('\n\t\t\t')

# put the sections together, write to file
html_full = html_head + '\n' + html_data + '\n' + html_foot
html_file = open('txt/table.html', 'w+')
html_file.write(html_full)
html_file.close()
