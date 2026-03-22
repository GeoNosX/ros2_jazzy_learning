import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    
    # 1. Find the exact folder paths for your two installed packages
    pubsub_path = get_package_share_directory('py_pubsub')
    param_path = get_package_share_directory('python_parameter_event_handler')

    # 2. Tell ROS 2 to INCLUDE the PubSub launch file
    pubsub_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pubsub_path, 'launch', 'pubsub_launch.py')
        )
    )

    # 3. Tell ROS 2 to INCLUDE the Parameter launch file... AND pass it an argument!
    param_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(param_path, 'launch', 'dynamic_launch.py')
        ),
        launch_arguments={'start_value': '500'}.items()  # <--- We are injecting the argument right here!
    )

    # 4. Push the master start button!
    return LaunchDescription([
        pubsub_launch,
        param_launch
    ])