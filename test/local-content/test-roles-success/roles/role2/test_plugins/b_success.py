"""A test plugin."""


def compatibility_in_test(element, container):
    """Return True when element contained in container."""
    return element in container


class TestModule:
    """Test plugin."""

    @staticmethod
    def tests():
        """Return tests."""
        return {
            "b_test_success": compatibility_in_test,
        }
