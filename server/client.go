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

	err := newClient.On("iniciar_compas", func(datas ...any) {
		log.Println("iniciar compas recibido", datas)
		mandar_a_todos(datas, playersMutex, players)
	})
	if err != nil {
		log.Println("failed to register iniciar_compas", "err", err)
		newClient.Disconnect(true)
	}

	err = newClient.On("pausar", func(datas ...any) {
		log.Println("pausar recibido", datas)
	})

	err = newClient.On("cambiar_cancion", func(datas ...any) {
		log.Println("cambiar_cancion recibido", datas)
	})

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

func mandar_a_todos(datas []any, playersMutex *sync.Mutex, players *[]*Player) {
	playersMutex.Lock()
	*players = []*Player{}
	for _, player := range *players {
		player.Socket.Emit("iniciar_compas", datas...)
	}
	playersMutex.Unlock()
}
