################################################################################
###                                 Imports                                  ###
################################################################################
#Standard imports
import subprocess

#Our imports
import file_management as fm

################################################################################
###                                Class Def                                 ###
################################################################################
class Hashcat:
	"""
	Interface to hashcat executable
	"""
	############################################################################
	def __init__(self):
		#Check if hashcat exists
		if not fm.does_hashcat_exist():
			#Hashcat does not exist so download it
			fm.download_latest_hashcat()

		#Hashcat now exists so save important directory and executable locations
		self.exe = fm.hashcat_exe_path()
		self.exe_dir = fm.hashcat_dir()

	############################################################################
	def get_version(self):
		"""
		Gets the current version of hashcat

		:return: current hashcat version
		:rtype: str
		"""
		res = subprocess.run([self.exe, "--version"], capture_output=True, 
							 text=True, cwd=self.exe_dir)
		return res.stdout.strip()[1:]

	############################################################################
	def update(self):
		"""
		Updates to latest version if necessary. There should be no other 
		instance of hashcat running while calling this
		"""
		fm.update_hashcat()

################################################################################
###                                Test Code                                 ###
################################################################################
if __name__ == "__main__":
	hc = Hashcat()
	
	print("Current hashcat version = %s" % hc.get_version())

################################################################################
###                               End of File                                ###
################################################################################