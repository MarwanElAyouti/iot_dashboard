# List all your DB models here if you want it be visible for alembic

from collections.abc import Sequence

from IoTDashboard.models.base import Base

"""
    e.g.:
        from collections.abc import Sequence

        from IoTDashboard.models.{model_name} import SomeModel

        __all__: Sequence = (Base, SomeModel)
"""

__all__: Sequence = (Base,)
