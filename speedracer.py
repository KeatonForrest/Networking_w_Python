import speedtest

test = speedtest.Speedtest()

print("Loading server list...")
test.get_servers()
print("Getting best server...")
best = test.get_best_server()

print(f"Found: {best['host']} located in {best['country']}")

print("Perfomring download test...")
download_result = test.download()
print("Performing upload test...")
upload_result = test.upload()
ping_result = test.results.ping

print(download_result)
print(upload_result)
print(ping_result)
