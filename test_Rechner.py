# Minimaler Komponententest für die Funktion berechne() in Rechner.py
import pytest
from Rechner import berechne

def test_addition():
    assert berechne(2, 3, "+") == 6


