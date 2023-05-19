################################################################################
###                                 Imports                                  ###
################################################################################
#Standard imports
import os

#Our imports
from utils import what_os

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
		return os.path.expanduser(os.path.join("~", "Documents", "pyhashcat"))
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
###                                Test Code                                 ###
################################################################################
if __name__ == "__main__":
	print("py-hashcat parent directory = %s" % app_dir())
	print("Hashcat directory = %s" % hashcat_dir())
	print("Hashcat executable path = %s" % hashcat_exe_path())

################################################################################
###                               End of File                                ###
################################################################################