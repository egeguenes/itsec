import socket

# a little script to get the ip addres from a url

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None

def main():
    url = input("Give the url : ")

    ip_address = get_ip_address(url)

    if ip_address:
        print(f"The IP address of {url} is {ip_address}")
    else:
        print(f"Failed to retrieve the IP address for {url}")

if __name__ == "__main__":
    main()
