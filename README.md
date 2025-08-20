# misora2_launch_uoa
## 内容
 - misora内部で以下のノードを立ち上げる
    - misora2_distribute_image/distribute_image_node：オペレータPCから受信した信号をもとに画像を送信するノード
    - misora2_pressure/pressure_node：圧力メータの読み取りノード
    - misora2_qr/qr_node：QRの読み取りノード
    - misora2_cracks/cracks_node：テストピース(クラック)の検査ノード
    - misora2_metal_loss/metal_loss_node：テストピース(減肉)の検査ノード
 - ミッションごとにファイルを分けている bringupP<<font color="red">ミッション番号1~4,6</font>>.launch.py
 
## 実行コード
~~~bash!
git clone git@github.com:WRS2025Pre-UoA/misora2_launch_uoa.git
cd [ワークスペース]
colcon build
source install/setup.bash
ros2 launch misora2_launch_uoa bringupP<1~6>.launch.py # 1~6は各ミッション番号
~~~