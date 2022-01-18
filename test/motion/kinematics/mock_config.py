
"""Shared mock data"""

from src.motion.leg_config import LegConfig

def mock_leg_config() -> LegConfig:
    """Mock frame data

    Returns:
        LegConfig: mock config
    """
    return LegConfig(66.0, 31.0, 77.0)
