from .mounted_panda import MountedPanda
from .on_the_ground_panda import OnTheGroundPanda

from robosuite.robots import FixedBaseRobot, ROBOT_CLASS_MAPPING

ROBOT_CLASS_MAPPING.update(
    {
        "MountedPanda": FixedBaseRobot,
        "OnTheGroundPanda": FixedBaseRobot,
    }
)
