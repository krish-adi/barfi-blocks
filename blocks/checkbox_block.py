from barfi import Block

checkbox_block = Block(name='Checkbox')

# Add the input and output interfaces
checkbox_block.add_input()
checkbox_block.add_output()

# Add an optional display text to the block
checkbox_block.add_option(name='display-option', type='display', value='This is a Block with Checkbox option.')

# Add the interface options to the Block
checkbox_block.add_option(name='checkbox-option-1', type='checkbox')

def checkbox_block_func(self):
    # Implement your computation function here 
    # Use the values from the input and input-options (checbox, slider, input-text..) with the
    # get_interface() and get_option() method

    # Get the value of the input interface
    input_1_value = self.get_interface(name='Input 1')

    # Get the value of the option
    checkbox_1_value = self.get_option(name='checkbox-option-1')

    # Implement your logic using the values
    # Here 
    # And obtain the value to set to the output interface
    # output_1_value = ...

    # Set the value of the output interface
    output_1_value = 0
    self.set_interface(name='Output 1', value=output_1_value)

# Add the compute function to the block
checkbox_block.add_compute(checkbox_block_func)