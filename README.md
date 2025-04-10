# misora2_launch_uoa
## 内容
 - misora内部で立ち上げるlaunchファイル
 - 立ち上げ内容
    - distribute_imageノード
    - pressureノード
    - qrノード
    - cracksノード
    - metal_lossノード
 - 各ミッションごとにlaunchファイルを分けている
    - launch/bringup<ミッション番号 P1,P2,P3,P4,P6>.launch.py
 
## 実行コード
~~~bash!
colcon build
source install/setup.bash
ros2 launch misora2_launch_uoa bringupP<>.launch.py
~~~