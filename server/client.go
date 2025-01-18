package main

import (
	"log"
	"sync"

	"github.com/zishang520/socket.io/v2/socket"
)

func manageClientConnection(clients []any, playersMutex *sync.Mutex, players *[]*Player) {

	newClient := clients[0].(*socket.Socket)
	newClientID := newClient.Id()

	log.Println("connection established. new client: ", newClientID)

	err := newClient.On("replicar", func(datas ...any) {
		log.Println("evento replicar recibido")

		// TODO: mutex for each player, not only for the list
		playersMutex.Lock()
		// players[newClient.Id()].InvertGravity()

		for _, player := range *players {
			player.Socket.Emit("replica", datas)
		}
		playersMutex.Unlock()
	})
	if err != nil {
		log.Println("evento replicar recibido", "err", err)
		newClient.Disconnect(true)
	}

	err = newClient.On("unirme_sesion", func(datas ...any) {
		log.Println("evento unirme_sesion")

		// TODO: mutex for each player, not only for the list
		playersMutex.Lock()
		// players[newClient.Id()].InvertGravity()

		for _, player := range *players {
			player.Socket.Emit("replica", datas)
		}
		playersMutex.Unlock()
	})
	if err != nil {
		log.Println("evento replicar recibido", "err", err)
		newClient.Disconnect(true)
	}

	err = newClient.On("disconnect", func(...any) {
		log.Println("client disconnected", newClient.Id())
		// delete(players, newClientID)
		playersMutex.Lock()
		*players = []*Player{}
		playersMutex.Unlock()
	})
	if err != nil {
		log.Println("failed to register on disconnect message", "err", err)
		newClient.Disconnect(true)
	}

	newPlayer := &Player{
		Socket: newClient,
		PosX:   0,
		PosY:   0,
	}

	playersMutex.Lock()
	// players[newClientID] = Player{
	// 	Socket: newClient,
	// }
	if len(*players) == 0 {
		*players = []*Player{newPlayer}
	} else {
		(*players)[0] = newPlayer
	}
	playersMutex.Unlock()
}
