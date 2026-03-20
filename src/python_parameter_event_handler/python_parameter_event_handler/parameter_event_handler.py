import rclpy 
from rclpy.node import Node
import rclpy.parameter
from rclpy.parameter_event_handler import ParameterEventHandler

class ParameterEventHandlerNode(Node):
    def __init__(self):
        super().__init__("node_with_parameters")
        self.declare_parameter("an_int_param", 0)
        self.handler = ParameterEventHandler(self)
        self.callback_handler = self.handler.add_parameter_callback(
            parameter_name="an_int_param",
            node_name='node_with_parameters',
            callback=self.callback
        )
    def callback(self, p: rclpy.parameter.Parameter):
        self.get_logger().info(f"Instant update detected! {p.name} is now: {p.value}")

def main():
    rclpy.init()
    node = ParameterEventHandlerNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()