import re, sys

# python listify.py classlist.html
make_txt = True # creates classlist.txt with "Firstname Lastname" format
make_csv = True # creates classlist.csv with "Lastname, Firstname" format

if len(sys.argv) > 1:
    html_file_name = sys.argv[1]
else:
	print("Must supply the file name for a classlist html file:")
	print("python listify.py classlist.html")
	sys.exit(0) # end program

html_file = open(html_file_name,"r") # r for read-only
html_content = html_file.read()

# txt file
if make_txt:
	txt_file_name = html_file_name[:-4] + "txt"
	txt_file = open(txt_file_name, "w+") # w+ for create file and write

	first_last_names = re.findall(r"\['([\w|\s|-]+)',''\]", html_content) # regex ['(letters|spaces|hyphens)','']

	for name in first_last_names:
		txt_file.write(name + "\n")

	print("Created {} with {} names".format(txt_file_name, len(first_last_names)))

	txt_file.close()

# csv file
if make_csv:
	csv_file_name = html_file_name[:-4] + "csv"
	csv_file = open(csv_file_name, "w+") # w+ for create file and write

	last_comma_first_names = re.findall(r'title="Compose.*".(.+)</a>', html_content) # regex title="Compose...".(all characters)</a>

	csv_file.write("Last, First\n")
	for name in last_comma_first_names:
		csv_file.write(name + "\n")

	print("Created {} with {} names".format(csv_file_name, len(last_comma_first_names)))

	csv_file.close()

html_file.close()