import sublime, sublime_plugin, os.path, subprocess

console2 = "C:\Program Files\Console2\Console.exe"

class JuliaConsoleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		f = self.view.file_name()
		cmds = [console2, "-t", "julia", "-d", os.path.dirname(f)]
		process = subprocess.Popen(cmds)

class Console2Command(sublime_plugin.TextCommand):
	def run(self, edit):
		f = self.view.file_name()
		cmds = [console2, "-d", os.path.dirname(f)]
		process = subprocess.Popen(cmds)