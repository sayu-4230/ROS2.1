import rclpy
from rclpy.node import Node
import pytz
from datetime import datetime
from std_msgs.msg import String

class TimeConverterNode(Node):
    def __init__(self):
        super().__init__('time_converter_node')
        self.publisher_ = self.create_publisher(String, 'uk_time', 10)
        self.timer = self.create_timer(10.0, self.timer_callback)  # 10秒ごとに時刻を取得

        # 日本（JST）タイムゾーンの定義
        self.japan_tz = pytz.timezone('Asia/Tokyo')
        # イギリス（GMT/BST）タイムゾーンの定義
        self.uk_tz = pytz.timezone('Europe/London')

    def timer_callback(self):
        # 日本の現在時刻を取得
        japan_time = datetime.now(self.japan_tz)
        
        # 日本の時刻をイギリスの時刻に変換
        uk_time = japan_time.astimezone(self.uk_tz)
        
        # メッセージの作成
        message = String()
        message.data = f"日本の時刻: {japan_time.strftime('%Y-%m-%d %H:%M:%S')} | イギリスの時刻: {uk_time.strftime('%Y-%m-%d %H:%M:%S')}"
        
        # トピックに時刻を公開
        self.publisher_.publish(message)
        self.get_logger().info(f"Published: {message.data}")

def main(args=None):
    rclpy.init(args=args)
    node = TimeConverterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

