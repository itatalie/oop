import sys
import os

# Добавляем путь к текущей директории (src/)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pytest
from main import Product, Category


def test_product():
    p = Product("Test", "Desc", 100.0, 5)
    assert p.name == "Test"
    assert p.price == 100.0


def test_category():
    p = Product("Test", "Desc", 100.0, 5)
    c = Category("TestCategory", "Desc", [p])
    assert c.name == "TestCategory"
    assert Category.product_count == 1
    assert Category.category_count == 1