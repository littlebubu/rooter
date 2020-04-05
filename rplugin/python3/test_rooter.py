# import pytest
# import json
# from rooter_remote import *
# from pathlib import Path


# with open(Path(__file__).parent / 'rooter_config.json') as config_file:
#     settings = json.load(config_file)

# patterns = settings["patterns"]

# def test_home():
#     assert get_root(patterns, Path('/home/brian')) == '/home/brian', "Home test failed"

# def test_project():
#     assert get_root(patterns, Path('/home/brian/projects/guessing_game/src')) == '/home/brian/projects/guessing_game', "Project test failed"

# def test_dotfiles():
#     assert get_root(patterns, Path('/home/brian/.config/nvim/plugin/mappings')) == '/home/brian/.config/nvim'

# def test_above_home():
#     assert get_root(patterns, Path('/home/brian/projects')) == '/home/brian/projects', "Test above home failed"

# def test_special_case():
#     assert get_root(patterns, Path('/usr/share')) == '/usr/share', "Special test failed"
