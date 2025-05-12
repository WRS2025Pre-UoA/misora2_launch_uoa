# misora2_launch_uoa
## 内容
 - misora内部で以下のノードを立ち上げる
    - misora2_distribute_image：オペレータPCから受信した信号をもとに画像を送信するノード
    - misora2_pressure：圧力メータの読み取りノード
    - misora2_qr：QRの読み取りノード
    - misora2_cracks：テストピース(クラック)の検査ノード
    - misora2_metal_loss：テストピース(減肉)の検査ノード
 - ミッションごとにファイルを分けている bringupP[<font color="red">ミッション番号1~4,6</font>].launch.py
 
## 実行コード
~~~bash!
git clone git@github.com:WRS2025Pre-UoA/misora2_launch_uoa.git
colcon build
source install/setup.bash
ros2 launch misora2_launch_uoa bringupP<1~4,6>.launch.py
~~~