import subprocess
import os.path
import sys

from os import path

def copy_data(file_location, output_location):

	template_str = " if=" + file_location + " of=" + output_location + "disk.img status=progress bs=1M"
	exec_string = ''

	dd_loc = subprocess.check_output(["which", "dd"]).decode("utf-8").rstrip('\n')
	gdd_loc = subprocess.check_output(["which", "gdd"]).decode("utf-8").rstrip('\n')

	if path.exists(dd_loc):
		exec_string = dd_loc + template_str
	if path.exists(gdd_loc):
		exec_string = gdd_loc + template_str
	else:
		sys.exit("dd or gdd not found - please install")

	subprocess.run("sudo " + exec_string, shell=True, check=True, stdout=subprocess.PIPE)

def retrieve_files(output_location):

	foremost_loc = subprocess.check_output(["which", "foremost"]).decode("utf-8").rstrip('\n')

	if not path.exists(foremost_loc):
		sys.exit("foremost not found - please install")

	exec_string = "foremost -dv -i " + output_location + "disk.img -T"
	subprocess.run(exec_string, shell=True, check=True, stdout=subprocess.PIPE)


if __name__ == "__main__":

	try:
		sd_disk_loc = sys.argv[1]
		output_location = sys.argv[2]
	except:
		sys.exit("Missing argument")

	if output_location[-1] != '/':
		output_location = output_location + '/'	
	
	print("Copying data from Micro SD")
	copy_data(sd_disk_loc, output_location)
	print("Carving out files from disk img")
	retrieve_files(output_location)
