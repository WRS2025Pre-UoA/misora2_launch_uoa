from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer, LoadComposableNodes
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    container = ComposableNodeContainer(
        name="misora_uoa_part", 
        package="rclcpp_components",
        executable="component_container_mt",#マルチスレッドの場合component_container_mt,シングルはcomponent_container
        namespace="P4",
        composable_node_descriptions=[
            ComposableNode(
                package="misora2_distribute_image",
                plugin="component_distribute_image::DistributeImage",
                name="distribute_image",
                extra_arguments=[{"use_intra_process_comms": True}],
                parameters=[{"mode": "P4"}, {"check_duration_sec": 1.0}, {"timer_interval_ms": 100}], #画像を何millisec間隔で流すか、また何s間流すか],
                remappings=[("raw_image" , "/arm_color_thermal_camera/selected_image_raw/compressed")]
            ),
            ComposableNode(
                package="misora2_qr",
                plugin="component_qr::DetectQR",
                name="qr",
                extra_arguments=[{"use_intra_process_comms": True}],
            ),
        ],
        output="screen",
    )
    
    return LaunchDescription([
        container, 
    ])
