from mcstatus import MinecraftServer

ipserver = input('Server? ')

server = MinecraftServer.lookup(ipserver)

status = server.status()
print(f"The server has {status.players.online} players and replied in {status.latency} ms")

latency = server.ping()
print(f"The server replied in {latency} ms")

query = server.query()
print(f"The server has the following players online: {', '.join(query.players.names)}")