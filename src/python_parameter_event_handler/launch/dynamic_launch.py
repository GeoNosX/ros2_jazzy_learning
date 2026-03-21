from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    
    # 1. Create a "Substitution" variable. This acts as a catcher's mitt for the terminal input.
    start_value_config = LaunchConfiguration('start_value')

    # 2. Declare the Argument. This tells ROS 2 what the argument is named and gives it a default value if the user forgets to type one.
    start_value_arg = DeclareLaunchArgument(
        'start_value',
        default_value='99',
        description='The starting integer value for our parameter'
    )

    # 3. Set up the Node, and map the configuration variable into the node's parameters!
    param_node = Node(
        package='python_parameter_event_handler',
        executable='node_with_parameters',
        name='my_dynamic_node',
        parameters=[{
            'an_int_param': start_value_config
        }],
        output='screen'
    )

    # 4. Return both the Argument and the Node
    return LaunchDescription([
        start_value_arg,
        param_node
    ])