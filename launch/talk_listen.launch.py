import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    network_usage = launch_ros.actions.Node(
        package='network_usage',
        executable='network_usage_pub',
        )
    listener = launch_ros.actions.Node(
        package='network_usage',
        executable='listener',
        output='screen'
        )

    return launch.LaunchDescription([network_usage_pub, listener])
