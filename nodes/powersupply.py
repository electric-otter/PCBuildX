import time

# Virtual Power Supply Simulation
class VirtualPowerSupply:
    def __init__(self):
        self.channels = {0: 0.0, 1: 0.0}  # Channel 0 and Channel 1, initialized with 0V
    
    def set_voltage(self, channel, voltage):
        """Simulate setting the voltage on the channel."""
        if voltage < 0:
            print("Error: Voltage cannot be negative. Please enter a valid voltage.")
            return
        self.channels[channel] = voltage
        print(f"Channel {channel} voltage set to {voltage} V")
    
    def get_voltage(self, channel):
        """Return the current voltage for the given channel."""
        return self.channels[channel]
    
    def display_status(self):
        """Display the current voltage of all channels."""
        print("\nCurrent Power Supply Status:")
        for channel, voltage in self.channels.items():
            print(f"Channel {channel}: {voltage} V")
    
    def run(self):
        """Main simulation loop for user input."""
        while True:
            user_input = input("\nEnter voltage (V) for Channel 0 and Channel 1 (or type 'exit' to quit): ")
            
            if user_input.lower() == "exit":
                print("Exiting simulation...")
                break
            
            try:
                voltage = float(user_input)
            except ValueError:
                print("Invalid voltage entered. Please enter a numeric value.")
                continue
            
            # Simulate setting the voltage for both channels
            self.set_voltage(0, voltage)  # Apply to Channel 0
            self.set_voltage(1, voltage)  # Apply to Channel 1
            self.display_status()  # Display current status of power supply

            # Optional: Sleep to simulate delay in voltage change
            time.sleep(1)

# Initialize the virtual power supply simulation
virtual_psu = VirtualPowerSupply()
virtual_psu.run()
