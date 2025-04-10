from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer, LoadComposableNodes
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    container = ComposableNodeContainer(
        name="misora_uoa_part", 
        package="rclcpp_components",
        executable="component_container_mt",#マルチスレッドの場合component_container_mt,シングルはcomponent_container
        namespace="P3",
        composable_node_descriptions=[
            ComposableNode(
                package="misora2_distribute_image",
                plugin="component_distribute_image::DistributeImage",
                name="distribute_image",
                extra_arguments=[{"use_intra_process_comms": True}],
                parameters=[{"mode": "P3"}]
            ),
            ComposableNode(
                package="misora2_cracks",
                plugin="component_cracks::EvaluateCracks",
                name="cracks",
                extra_arguments=[{"use_intra_process_comms": True}],
            ),
            ComposableNode(
                package="misora2_metal_loss",
                plugin="component_metal_loss::EvaluateMetalLoss",
                name="metal_loss",
                extra_arguments=[{"use_intra_process_comms": True}],
            )
        ],
        output="screen",
    )
  
    
    # load_composable_nodes = LoadComposableNodes(
    #     target_container="my_container",
    #     composable_node_descriptions=[
    #         ComposableNode(
    #             package="listener",
    #             plugin="Listener",
    #             name="listener",
    #             extra_arguments=[{"use_intra_process_comms": True}],
    #         ),
    #     ],
    # )
    
    return LaunchDescription([
        container, 
        # load_composable_nodes
    ])
