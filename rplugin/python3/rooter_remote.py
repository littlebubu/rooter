from pathlib import Path
import pynvim


class Rooter():
    """A class to manage the rooter."""

    def __init__(self, working_dir, patterns=['.git']):
        """Initialize rooter class"""
        self.initial_dir = working_dir
        self.working_dir = Path(working_dir)
        self.patterns = patterns

    def run_rooter(self):
        """
        Runs the rooter repeatedly until something or nothing is found.
        """
        while True:
            if not self.is_special_case(self.working_dir):
                if self.find_patterns():
                    return str(self.working_dir)
                else:
                    self.working_dir = self.working_dir.parent
            else:
                return self.initial_dir

    def find_patterns(self):
        """
        Checks if a pattern is found in the supplied directory.
        """
        # listdir = os.listdir(self.working_dir)
        for pattern in self.patterns:
            matches = self.working_dir.glob(f'*{pattern}')
            if self.peek(matches):
                return True
        return False

    @staticmethod
    def is_special_case(directory):
        """
        Checks if the supplied directory is at home or one level above.
        """
        if directory.parent.parent == Path('/'):
            return True
        else:
            return False

    @staticmethod
    def peek(iterable):
        try:
            next(iterable)
        except StopIteration:
            return False
        else:
            return True


@pynvim.plugin
class RooterPlugin:

    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('Rooter', nargs='*', range='')
    def rooter(self, args, range):
        # find directory that contains current file
        self.nvim.command("let path = expand('%:p:h')")

        path = self.nvim.eval('path')
        rooter = Rooter(path)
        final_dir = rooter.run_rooter()

        self.nvim.command("cd {}".format(final_dir))
        self.nvim.command("echo 'cwd: {}'".format(final_dir))


if __name__ == '__main__':
    path = '/home/brian/projects/guessing_game/src/main.rs'
    rooter = Rooter(path)
    print(rooter.run_rooter())
