import os
import sys
import csv

def csv_to_html(file_csv = "sample.csv", html_filename = "index.html", delimiter = ",", quotechar = '"'):
    html = "<html><body><table>"
    with open(os.path.join(sys.path[0], file_csv), "r") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in spamreader:
            if spamreader.line_num == 1:
                html += "<tr>"
                for value in row:
                    html += "<th>{0}</th>".format(value)
                html += "</tr>"
            else:
                html += "<tr>"
                for value in row:
                    html += "<td>{0}</td>".format(value)
                html += "</tr>"
    html += "</table></body></html>"
    file = open(os.path.join(sys.path[0], html_filename),"w+")
    file.write(html)
    file.close
