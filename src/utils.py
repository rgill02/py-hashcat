################################################################################
###                                 Imports                                  ###
################################################################################
#Standard imports
from sys import platform

################################################################################
###                            Utility Functions                             ###
################################################################################
def what_os():
	"""
	Determines what operating system we are running on: windows, mac, or linux

	:return: "windows" if we are running on windows, "mac" if we are running on 
		macos, "linux" if we are running on some version of linux, or "other" if 
		we are running on some other unknown operating system
	:rtype: str
	"""
	if platform == "linux" or platform == "linux2":
		return "linux"
	elif platform == "darwin":
		return "mac"
	elif platform == "win32":
		return "windows"
	else:
		return "OTHER"

################################################################################
###                                Test Code                                 ###
################################################################################
if __name__ == "__main__":
	print("This operating system is a version of %s" % what_os())

################################################################################
###                               End of File                                ###
################################################################################