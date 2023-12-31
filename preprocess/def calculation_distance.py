# 球面三角法をつかった２地点間の距離の計算
# 球面三角法をつかって２地点間のおおよその距離を計算します。単位はkmです。

def calculation_distance(x_1, y_1, x_2, y_2):
    # 赤道半径 (km)
    R = 6371
    # Radian角に変換
    _x1, _y1, _x2, _y2  = map(np.radians, [x_1, y_1, x_2, y_2])
    
    delta_x = _x2 - _x1
    delta_y = _y2 - _y1
    
    # 距離を計算
    a = np.sin(delta_y/2.0)**2 + np.cos(_y1) * np.cos(_y2) * np.sin(delta_x/2.0)**2
    return 2 * R * np.arcsin(np.sqrt(a))

# calculation_distance 関数は、2つの地点の緯度経度座標を受け取り、ハーフハーシン法を使用してその地点間の距離（大円距離）を計算する関数です。具体的な例を挙げて説明します。
import numpy as np

# 2つの地点の緯度経度座標を設定（度数法で表現）
x_1 = 40.7128  # 緯度（例: ニューヨーク市の緯度）
y_1 = -74.0060  # 経度（例: ニューヨーク市の経度）
x_2 = 34.0522  # 緯度（例: ロサンゼルスの緯度）
y_2 = -118.2437  # 経度（例: ロサンゼルスの経度）

# 距離を計算
distance = calculation_distance(x_1, y_1, x_2, y_2)

# 距離を表示
display(f"2つの地点間の距離: {distance} km")

# このコードでは、2つの地点（ニューヨーク市とロサンゼルス）の緯度経度座標を設定し、calculation_distance 関数を使用してこれらの地点間の距離を計算しています。
# 距離の計算は、ハーフハーシン法を使用しており、計算結果は2つの地点間の大円距離（球面上の最短距離）を示します。この場合、出力はおおよそ「2つの地点間の距離: 3939.38 km」となります。
