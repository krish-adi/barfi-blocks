from barfi import Block

plain_block = Block(name='Plain')

# Add the input and output interfaces
plain_block.add_input()
plain_block.add_output()

def plain_block_func(self):
    # Implement your computation function here 
    # Use the values from the input with the
    # get_interface() method

    # Get the value of the input interface
    input_1_value = self.get_interface(name='Input 1')

    # Implement your logic using the values
    # Here 
    # And obtain the value to set to the output interface
    # output_1_value = ...

    # Set the value of the output interface
    # output_1_value = ...
    output_1_value = 0
    self.set_interface(name='Output 1', value=output_1_value)

# Add the compute function to the block
plain_block.add_compute(plain_block_func)