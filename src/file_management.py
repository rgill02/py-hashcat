################################################################################
###                                 Imports                                  ###
################################################################################
#Standard imports
import os
import re
import urllib.request
import shutil

#Third party imports
import requests
from pyunpack import Archive

#Our imports
from utils import what_os
import Hashcat

################################################################################
###                                Constants                                 ###
################################################################################
HASHCAT_URL = "https://hashcat.net/"

################################################################################
###                                Functions                                 ###
################################################################################
def app_dir():
	"""
	Determine parent directory for all files related to this program

	:return: full path to directory
	:rtype: str
	"""
	our_os = what_os()
	if our_os == "windows":
		return os.path.expanduser(os.path.join("~", "Documents", "tools", "pyhashcat"))
	elif our_os == "linux":
		#TODO implement for linux
		raise NotImplementedError("'app_dir' not implemented yet for linux'")
	elif our_os == "mac":
		#TODO implement for mac
		raise NotImplementedError("'app_dir' not implemented yet for mac")
	else:
		raise RuntimeError("Unknown operating system!")

################################################################################
def hashcat_dir():
	"""
	Determine hashcat directory

	:return: full path to directory
	:rtype: str
	"""
	return os.path.join(app_dir(), "hashcat")

################################################################################
def hashcat_exe_path():
	"""
	Determine the path to the hashcat executeable

	:return: full path to hashcat executeable
	:rtype: str
	"""
	our_os = what_os()
	if our_os == "windows":
		return os.path.join(hashcat_dir(), "hashcat.exe")
	elif our_os == "linux":
		#TODO implement for linux
		raise NotImplementedError("'hashcat_exe_path' not implemented yet for linux'")
	elif our_os == "mac":
		#TODO implement for mac
		raise NotImplementedError("'hashcat_exe_path' not implemented yet for mac")
	else:
		raise RuntimeError("Unknown operating system!")

################################################################################
def does_hashcat_exist():
	"""
	Determines if an instance of hashcat exists

	:return: True if it does, False if not
	:rtype: bool
	"""
	return os.path.exists(hashcat_exe_path())

################################################################################
def determine_latest_hashcat_version():
	"""
	Determines the latest hashcat version by pulling from their website

	:return: latest version number as a string
	:rtype: str
	"""
	#Fetch webpage
	r = requests.get(HASHCAT_URL)
	if r.status_code != 200:
		raise RuntimeError("Could not reach hashcat.net")

	#Find version in webpage
	regex_pattern = "<td>hashcat binaries</td>\s*<td>v(?P<ver>\d+.\d+.\d+)</td>"
	match = re.search(regex_pattern, r.text)
	if match:
		return match.group("ver")
	else:
		raise RuntimeError("Unable to determine latest version")

################################################################################
def download_latest_hashcat():
	"""
	Downloads the latest version of hashcat and saves it to the location given 
	by "app_dir"
	"""
	#Make sure parent directory exists so we have somewhere to put hashcat
	parent_dir = app_dir()
	if not os.path.exists(parent_dir):
		os.makedirs(parent_dir)

	#Make sure hashcat directory does not exist
	shutil.rmtree(hashcat_dir(), ignore_errors=True)

	#Download latest version
	ver = determine_latest_hashcat_version()
	url_target = HASHCAT_URL + "files/hashcat-" + ver + ".7z"
	hashcat_7z_loc = os.path.join(parent_dir, "hashcat.7z")
	try:
		os.remove(hashcat_7z_loc)
	except OSError:
		pass
	urllib.request.urlretrieve(url_target, hashcat_7z_loc)

	#Decompress downloaded file
	Archive(hashcat_7z_loc).extractall(parent_dir)

	#Renamed decompressed directory
	decompressed_dir = os.path.join(parent_dir, "hashcat-%s" % ver)
	os.rename(decompressed_dir, hashcat_dir())

	#Remove compressed file
	os.remove(hashcat_7z_loc)

################################################################################
def update_hashcat():
	"""
	Updates hashcat to the latest version if necessary. Make sure hashcat is 
	not running before you call this
	"""
	latest_ver = determine_latest_hashcat_version()

	hc = Hashcat.Hashcat()
	my_ver = hc.get_version()

	if my_ver != latest_ver:
		download_latest_hashcat()

################################################################################
###                                Test Code                                 ###
################################################################################
if __name__ == "__main__":
	print("py-hashcat parent directory = %s" % app_dir())
	print("Hashcat directory = %s" % hashcat_dir())
	print("Hashcat executable path = %s" % hashcat_exe_path())
	print("Latest hashcat version = %s" % determine_latest_hashcat_version())

	print("\nDownloading latest hashcat version...")
	download_latest_hashcat()
	print("Latest hashcat downloaded")



################################################################################
###                               End of File                                ###
################################################################################