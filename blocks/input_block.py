from barfi import Block

input_block = Block(name='Input')

# Add the input and output interfaces
input_block.add_input()
input_block.add_output()

# Add an optional display text to the block
input_block.add_option(name='display-option', type='display', value='This is a Block with Input option.')

# Add the interface options to the Block
input_block.add_option(name='input-option-1', type='input')

def input_block_func(self):
    # Implement your computation function here 
    # Use the values from the input and input-options (checbox, slider, input-text..) with the
    # get_interface() and get_option() method

    # Get the value of the input interface
    input_1_value = self.get_interface(name='Input 1')

    # Get the value of the option
    input_1_value = self.get_option(name='input-option-1')

    # Implement your logic using the values
    # Here 
    # And obtain the value to set to the output interface
    # output_1_value = ...

    # Set the value of the output interface
    output_1_value = 0
    self.set_interface(name='Output 1', value=output_1_value)

# Add the compute function to the block
input_block.add_compute(input_block_func)