
from BOs import UserBO

class User:
    """User class for managing user data."""

    def __init__(self, user_bo: UserBO):
        """Initialize a User instance with a UserBO object."""
        if not isinstance(user_bo, UserBO):
            raise ValueError("user_bo parameter must be an instance of UserBO")
        self.user_bo = user_bo

    def __getattr__(self, attr):
        """Delegate attribute access to UserBO object."""
        return getattr(self.user_bo, attr)

    def __str__(self):
        return f"User: {self.user_bo.name}, Email: {self.user_bo.email}, ID: {self.user_bo.uid}"
