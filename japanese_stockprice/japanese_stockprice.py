import rclpy
from rclpy.node import Node
import yfinance as yf
from std_msgs.msg import String

class JapaneseStockPrice(Node):
    def __init__(self):
        super().__init__('japanese_stockprice')
        self.publisher_ = self.create_publisher(String, 'stock_price_topic', 10)
        self.timer = self.create_timer(10, self.timer_callback)  # 10秒ごとに株価を更新
        self.get_logger().info("Japanese Stock Price has started.")
    
    def timer_callback(self):
        # 日本の株式市場の株価を取得（例えば、日経平均）
        ticker = yf.Ticker("^N225")  # 日経平均のティッカーシンボル
        stock_info = ticker.history(period="1d")  # 1日の株価データを取得
        if not stock_info.empty:
            latest_price = stock_info['Close'].iloc[-1]  # 最後の終値を取得
            msg = String()
            msg.data = f"日経平均の株価: {latest_price}円"
            self.publisher_.publish(msg)
            self.get_logger().info(f"Published stock price: {msg.data}")
        else:
            self.get_logger().warn("株価情報を取得できませんでした。")

def main(args=None):
    rclpy.init(args=args)
    node = JapaneseStockPrice()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

