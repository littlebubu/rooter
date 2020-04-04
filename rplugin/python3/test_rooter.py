import pytest
from rooter_remote import Rooter


def test_home():
    rooter = Rooter('/home/brian')
    assert rooter.run_rooter() == '/home/brian', "Home test failed"

def test_project():
    rooter = Rooter('/home/brian/projects/guessing_game/src')
    assert rooter.run_rooter() == '/home/brian/projects/guessing_game', "Project test failed"

def test_dotfiles():
    rooter = Rooter('/home/brian/.config/nvim/plugin/mappings')
    assert rooter.run_rooter() == '/home/brian/.config/nvim'

def test_above_home():
    rooter = Rooter('/home/brian/projects')
    assert rooter.run_rooter() == '/home/brian/projects', "Test above home failed"

def test_special_case():
    rooter = Rooter('/usr/share')
    assert rooter.run_rooter() == '/usr/share', "Special test failed"
