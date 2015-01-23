#!/usr/bin/python
# -*- coding: utf-8 -*-
import sublime, sublime_plugin, os.path, subprocess

settings                = sublime.load_settings("JuliaConsole.sublime-settings")
console2_location       = settings.get('console_location').encode("ascii")
console2_julia_tab_name = settings.get('console2_julia_tab_name').encode("ascii")
julia_location          = settings.get('julia_location').encode("ascii")

class JuliaConsoleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		f = self.view.file_name()
		cmds = [console2_location, "-t", console2_julia_tab_name, "-d", os.path.dirname(f)]
		process = subprocess.Popen(cmds)

class Console2Command(sublime_plugin.TextCommand):
	def run(self, edit):
		f = self.view.file_name()
		cmds = [console2_location, "-d", os.path.dirname(f)]
		process = subprocess.Popen(cmds)

class JuliaEvalStringCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		useSublimeConsole = settings.get('output_to_sublime_console')
		sels = self.view.sel()
		for sel in sels:
			jl_cmd = self.view.substr(sel).replace("\n", ";").replace("\"", "\\\"").replace("\\", "\\\\").encode("ascii")
			if useSublimeConsole:
				command = [julia_location, '-E', "%s" % jl_cmd]
				pipe = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
				output = str.join("", pipe.stdout.readlines())
				sts = pipe.wait()
				print output
			else:
				command = [console2_location, '-t', console2_julia_tab_name, '-r', "-P \"%s\"" % jl_cmd]
				process = subprocess.Popen(command)


class JuliaReloadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		f = self.view.file_name()
		command = [console2_location, '-t', console2_julia_tab_name, '-r', "-L %s" % os.path.abspath(os.path.basename(f)).encode("ascii")]
		process = subprocess.Popen(command)