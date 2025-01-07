import rclpy
from rclpy.node import Node
from std_ msgs.msg import Int16

class Talker(Node):
    def __init__(self):
        super().__init__("taker")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(0.5, self.cd)
        self.n = 0


    def cd(self):
        msg = Int16()
        msg.date = self.n
        self.pub.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
