import ipaddress

def subnet_calculator(ip, subnet_prefix):
    try:
        # Create an IP network object
        network = ipaddress.IPv4Network(f"{ip}/{subnet_prefix}", strict=False)

        # Extract information
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        first_usable = list(network.hosts())[0]
        last_usable = list(network.hosts())[-1]
        total_hosts = network.num_addresses - 2  # -2 for network and broadcast addresses

        # Calculate the next network address
        next_network_address = network_address + network.num_addresses

        # Display the results
        print(f"IP Address: {ip}")
        print(f"Subnet Prefix: /{subnet_prefix}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"Network Address: {network_address}")
        print(f"Broadcast Address: {broadcast_address}")
        print(f"First Usable IP: {first_usable}")
        print(f"Last Usable IP: {last_usable}")
        print(f"Total Usable Hosts: {total_hosts}")
        print(f"Next Network Address: {ipaddress.IPv4Address(next_network_address)}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Input: IP address and subnet prefix (e.g., 192.168.1.10/24)
    ip = input("Enter IP Address (e.g., 192.168.1.1): ")
    subnet_prefix = input("Enter Subnet Prefix (e.g., 24): ")

    # Call the calculator function
    subnet_calculator(ip, subnet_prefix)

