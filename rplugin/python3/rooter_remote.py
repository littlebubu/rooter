from pathlib import Path
import pynvim
import json


def get_root(patterns, working_dir):
    initial_dir = working_dir
    current_dir = working_dir
    while True:
        if not is_special_case(current_dir):
            if find_patterns(patterns, current_dir):
                return str(current_dir)
            else:
                current_dir = current_dir.parent
        else:
            return str(initial_dir)


def find_patterns(patterns, working_dir):
    """
    Checks if a pattern is found in the supplied directory.
    """
    # listdir = os.listdir(self.working_dir)
    for pattern in patterns:
        matches = working_dir.glob(f'*{pattern}')
        if peek(matches):
            return True
    return False


def is_special_case(directory):
    """
    Checks if the supplied directory is at home or one level above.
    """
    if directory.parent.parent == Path('/'):
        return True
    else:
        return False

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

    @pynvim.function('Rooter')
    def rooter(self, args):
        """Rooter nvim command."""
        self.nvim.chdir(get_root(['.git'],
                                 Path(self.nvim.eval("expand('%:p:h')"))
                                 ))

    # @pynvim.command('RooterConfig', nargs='*', range='')
    # def rooter_config(self, args, range):
    #     """Nvim command to open the rooter_config json file."""
    #     self.nvim.command(f"e {self.config_path}")

    @pynvim.autocmd('BufEnter', pattern='*')
    def autorooter(self):
        self.nvim.call('Rooter')
