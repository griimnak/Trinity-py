import os

#---------------------------------------------\
# A . P . I . S
# Automated . Pip . Installation . Script
#---------------------------------------------
# Relieves the need of cx_freeze, py2exe and
# and similar modules by automating the
# installation of modules required by your
# release/script, using pip.
#
# Written by griimnak
#---------------------------------------------/

class Apis(object):

	def __init__(self):	

		#---------------------------------------------\
		# Place your required modules in
		# >> self.modules_to_be_installed
		#---------------------------------------------/
		self.modules_to_be_installed = ['flask', 'passlib', 'gevent', 'pymysql']
		self.marked = []

		print(' [NOTICE] Automated Pip Installation Script >> LOADED!')
		print(' [NOTICE] Beginning check process..\n')

		self.checkIfExists()

	def checkIfExists(self):
		for item in self.modules_to_be_installed:
			try:
				__import__(item)
			except ImportError:
				print('\n * ' + item + ' [not found], marked for installation.\n')
				self.marked.extend([item])
			else:
				print(' * ' + item + ' found, requirement satisfied.')

		if self.marked:
			print(' * The following modules are marked for installation:')
			print(' * ' + str(self.marked).strip('[]'))

			confirm_install = input(' * Would you like to begin installing them now? y/n')
			if confirm_install == 'n':
				print(' * Installation aborted, exiting script..')
			elif confirm_install == 'y':
				self.beginInstall()
			else:
				print(' * "' + confirm_install + '" is not an option, exiting..')

	def beginInstall(self):
		print(' * Please define whether i should use pip or pip3.')
		pipcheck = input(" * Please type 'pip' or 'pip3' (without quotations) ")

		slave = None
		if pipcheck == "pip":
			slave = 'pip'
		elif pipcheck == "pip3":
			slave = "pip3"
		else:
			print(" [NOTICE] '" + pipcheck + "'", "is not an option, exiting..")

		for item in self.marked:
			try:
				print('\n * Attempting to install: ' + item + '\n')
				os.system(slave + ' install ' + item)
			except:
				print('\n * FAILED TO INSTALL: ' + item + '\n')

		print('\n [NOTICE] Automated Pip Installation Script >> FINISHED! Exiting..\n')

Apis()