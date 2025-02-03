# SPDX-FileCopyrightText: 2025 Yuki Nishijima
# SPDX-License-Identifier: BSD-3-Clause

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class NetworkUsagePublisher(Node):
    def __init__(self):
        super().__init__("network_usage_pub")
        self.pub = self.create_publisher(Float64, "network_usage", 10)
        self.create_timer(1.0, self.publish_network_usage)
    def publish_network_usage(self):
        net_info = psutil.net_io_counters()
        sent_bytes = net_info.bytes_sent  # 送信バイト数
        recv_bytes = net_info.bytes_recv  # 受信バイト数
        msg = Float64()
        msg.data = float(sent_bytes + recv_bytes)  # 送受信バイト数の合計
        self.pub.publish(msg)
        self.get_logger().info(f"Network Usage: {sent_bytes + recv_bytes} bytes")
def main():
    rclpy.init()
    node = NetworkUsagePublisher()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()
