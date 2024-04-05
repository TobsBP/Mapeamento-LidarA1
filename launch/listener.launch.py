from launch import LaunchDescription
from launch_ros.actions import Node

def gerenrate_launch_description():
  return LaunchDescription([
    Node(
      package='demo_nodes_py',
      executable='listener'
    )
  ])