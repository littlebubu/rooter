import os
import pynvim


class Rooter():
    """A class to manage the rooter."""

    def __init__(self, working_dir, patterns=['.git']):
        """Initialize rooter class"""
        self.initial_dir = working_dir
        self.working_dir = working_dir
        self.patterns = patterns

    def run_rooter(self):
        """
        Runs the rooter repeatedly until something or nothing is found.
        """
        while True:
            if not self.check_home(self.working_dir):
                if self.check_patterns():
                    return self.working_dir
                else:
                    self.working_dir = self.go_up_dir(self.working_dir)
            else:
                return self.initial_dir

    def check_patterns(self):
        """
        Checks if a pattern is found in the supplied directory.
        """
        listdir = os.listdir(self.working_dir)
        for pattern in self.patterns:
            if pattern in listdir:
                return True
            else:
                return False

    @staticmethod
    def check_home(directory):
        """
        Checks if the supplied directory is at home or one level above.
        """
        if directory == '/home/brian':
            return True
        else:
            return False

    @staticmethod
    def go_up_dir(directory):
        """Returns the directory that is one above the supplied directory."""
        new_directory = os.path.split(directory)[0]
        return new_directory


@pynvim.plugin
class RooterPlugin:

    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.function('Rooter')
    def rooter(self, args):
        self.nvim.command("let cwd = getcwd()")
        rooter = Rooter(self.nvim.eval("cwd"))
        final_dir = rooter.run_rooter()
        self.nvim.command("cd {}".format(final_dir))
        self.nvim.command("echo 'should have just changed dir'")


if __name__ == '__main__':
    path = '/home/brian/projects/guessing_game/src/main.rs'
    rooter = Rooter(path)
    print(rooter.run_rooter())
