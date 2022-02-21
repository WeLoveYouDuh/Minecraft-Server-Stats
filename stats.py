from mcstatus import MinecraftServer

ipserver = input('Server? ')

server = MinecraftServer.lookup(ipserver)

status = server.status()

statsbanner = f"""
        :::   :::    ::::::::          :::::::: ::::::::::: ::: ::::::::::: :::::::: 
      :+:+: :+:+:  :+:    :+:        :+:    :+:    :+:   :+: :+:   :+:    :+:    :+: 
    +:+ +:+:+ +:+ +:+               +:+           +:+  +:+   +:+  +:+    +:+         
   +#+  +:+  +#+ +#+               +#++:++#++    +#+ +#++:++#++: +#+    +#++:++#++   
  +#+       +#+ +#+                      +#+    +#+ +#+     +#+ +#+           +#+    
 #+#       #+# #+#    #+#        #+#    #+#    #+# #+#     #+# #+#    #+#    #+#     
###       ###  ########          ########     ### ###     ### ###     ########   

                         ONLINE PLAYERS > {status.players.online}
                         PING > {status.latency}

"""

print (statsbanner)

