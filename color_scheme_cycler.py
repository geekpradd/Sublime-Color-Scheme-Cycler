import sublime, sublime_plugin 

def set_scheme(name):
	sublime.load_settings("Preferences.sublime-settings").set('color_scheme', name)

class SchemeCyclerCommand(sublime_plugin.WindowCommand):
	def run(self):
		print ('ok')
		sublime.status_message("Indexing Color Schemes..")
		self.initial = sublime.load_settings("Preferences.sublime-settings").get('color_scheme')
		self.syntax = list(sorted(sublime.find_resources("*.tmTheme") + sublime.find_resources("*.sublime-syntax")))
		sublime.status_message("Found {0} color schemes in total".format(len(self.syntax)))
		self.display_list(self.syntax)

	def display_list(self, iterable):
		items = [[x.split("/")[-1].capitalize(),x.split("/")[1]] for x in iterable]
		self.window.show_quick_panel(items,
                                     self.on_done,
                                     on_highlight=self.on_highlighted)

	def on_highlighted(self, index):
		set_scheme(self.syntax[index])

	def on_done(self, index):
		if index is -1:
			set_scheme(self.initial)
			sublime.status_message("Scheme change cancelled")
		else:
			sublime.status_message("Color Scheme {0} set!".format(self.syntax[index]))

