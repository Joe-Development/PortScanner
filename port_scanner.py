import socket
from prettytable import PrettyTable
from colorama import Fore, Style

def port_scan(target_host, target_ports):
    print(f"[+] Scanning ports on: {target_host}\n")

    table = PrettyTable()
    table.field_names = [Fore.BLUE + "Port", Fore.BLUE + "Status" + Style.RESET_ALL]

    for target_port in target_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, target_port))
        if result == 0:
            table.add_row([target_port, Fore.GREEN + "Open" + Style.RESET_ALL])
        else:
            table.add_row([target_port, Fore.RED + "Closed" + Style.RESET_ALL])
        sock.close()

    print(table)

def main():
    target_host = input("[+] Enter the target host IP address >> ").strip()
    target_ports = list(map(int, input("[+] Enter the target ports (comma-separated) >> ").split(',')))

    port_scan(target_host, target_ports)

if __name__ == "__main__":
    main()
