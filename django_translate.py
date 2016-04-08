import sublime, sublime_plugin

class DjangoTranslateCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        translator_begin = "{% trans \'"
        translator_end = "\' %}"
        messages = list(self.view.sel())

        for message in messages:
            self.view.insert(edit, message.end(), translator_end)
            self.view.insert(edit, message.begin(), translator_begin)
            
        print('Added trans blocks.')
        
#{"keys": ["ctrl+shift+t"], "command": "django_translate"}
