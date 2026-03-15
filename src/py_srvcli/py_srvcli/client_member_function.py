import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MinimalClientAsync(Node):
    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli=self.create_client(AddTwoInts, "add_two_ints")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not available, waiting again...")
        self.req=AddTwoInts.Request()
    
    def send_request(self,a,b): 
        self.req.a=a
        self.req.b=b
        return self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    minimal_client = MinimalClientAsync()
    
    # Grab the numbers we type in the terminal!
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    
    future = minimal_client.send_request(a, b)
    rclpy.spin_until_future_complete(minimal_client, future)
    
    response = future.result()
    minimal_client.get_logger().info(
        f"Result of add_two_ints: {a} + {b} = {response.sum}")

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()