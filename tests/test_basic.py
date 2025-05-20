def test_import():
    """Test that the package can be imported"""
    try:
        import pwnelle
        assert True
    except ImportError:
        assert False, "Failed to import pwnelle package"

def test_basic_functionality():
    """A basic test to ensure testing framework works"""
    assert True, "Basic assertion test" 