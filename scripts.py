import sublime, sublime_plugin
import re

def move_to_next_pane(window):
        next_group = (window.active_group()+1) % window.num_groups()
        window.focus_group(next_group)


def move_to_prev_pane(window):
        next_group = (window.active_group() - 1)
        if (next_group < 0):
            next_group = window.num_groups() - 1
        window.focus_group(next_group)

class MoveByEmptyLineCommand(sublime_plugin.TextCommand):
    def run(self, edit, extend = False, forward = True):
        self.view.run_command("move", {"by": "lines", "forward": forward, "extend": extend})
        window = sublime.active_window()
        view = window.active_view()
        totalLines = len(view.lines(sublime.Region(0, view.size())))
        (row, col) = view.rowcol(view.sel()[0].begin())
        linePoint = view.line(view.sel()[0].begin())
        line = view.substr(view.line(linePoint))
        
        while (re.match("^\s*$", line) == None and row != 1 and row != 0 and row != totalLines and row != totalLines - 1):
            self.view.run_command("move", {"by": "lines", "forward": forward, "extend": extend})
            linePoint = view.line(view.sel()[0].begin())
            line = view.substr(view.line(linePoint))
            (row, col) = view.rowcol(view.sel()[0].begin())