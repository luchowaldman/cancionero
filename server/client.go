package main

import (
	"log"

	"github.com/zishang520/socket.io/v2/socket"
)

var rooms = map[string]*Room{}

func manageClientConnection(clients []any) {
	newClient := clients[0].(*socket.Socket)
	newClientID := newClient.Id()

	log.Println("connection established. new client: ", newClientID)

	newPlayer := NewPlayer(newClient)

	err := newClient.On("changeGravity", func(datas ...any) {
		log.Println("changeGravity event received")

		if newPlayer.Room == nil {
			log.Println("changeGravity event received when the player is not in a room, ignoring message")

			return
		}

		if !newPlayer.Room.GameStarted.Load() {
			log.Println("changeGravity event received when the game has not yet started, ignoring message")

			return
		}

		// TODO: mutex for each player, not only for the list
		newPlayer.Room.Mutex.Lock()
		newPlayer.Character.InvertGravity()
		newPlayer.Room.Mutex.Unlock()
	})
	if err != nil {
		log.Println("failed to register on changeGravity message", "err", err)
		newClient.Disconnect(true)

		return
	}

	err = newClient.On("iniciarJuego", func(datas ...any) {
		log.Println("iniciarJuego event received")

		if newPlayer.Room == nil {
			log.Println("iniciarJuego event received when the player is not in a room, ignoring message")

			return
		}
		return
	})
	if err != nil {
		log.Println("failed to register on iniciarJuego message", "err", err)
		newClient.Disconnect(true)

		return
	}

	err = newClient.On("unirme_sesion", func(datas ...any) {
		if len(datas) == 2 {
			sesion := datas[0].(string)
			usuario := datas[1].(string)

			log.Println("unirSala event received with:", sesion, usuario)

			room, roomExists := rooms[sesion]
			if !roomExists {

				log.Println("crearSala event received with:", sesion, usuario)
				removeFromRoom(newPlayer)
				newRoom := NewRoom(sesion)
				newRoom.ID = sesion
				newPlayer.Name = usuario
				newRoom.AddPlayer(newPlayer)
				rooms[newRoom.ID] = newRoom
				log.Println("Room ", newRoom.ID, " created, waiting for players")
				return
			}

			removeFromRoom(newPlayer)
			newPlayer.Name = usuario
			room.AddPlayer(newPlayer)
		} else {
			log.Println("unirSala event received without correct params")
		}
	})
	if err != nil {
		log.Println("failed to register on unirSala message", "err", err)
		newClient.Disconnect(true)

		return
	}

	err = newClient.On("replicar", func(datas ...any) {
		log.Println("replicar event received with:", datas)
		if len(datas) > 2 {
			sesion := datas[0].(string)
			usuario := datas[1].(string)
			log.Println("replicar event received with:", sesion, usuario, datas[2])
			newPlayer.Room.Replicar(newPlayer.ID, usuario, datas[2])

		}
	})
	if err != nil {
		log.Println("failed to register on crearSala message", "err", err)
		newClient.Disconnect(true)

		return
	}

	err = newClient.On("disconnect", func(...any) {
		log.Println("client disconnected", newClient.Id())

		newPlayer.Socket = nil

		removeFromRoom(newPlayer)
	})
	if err != nil {
		log.Println("failed to register on disconnect message", "err", err)
		newClient.Disconnect(true)

		return
	}
}

func removeFromRoom(player *Player) {
	if player.Room != nil {
		roomID := player.Room.ID

		playersAmount := player.Room.RemovePlayer(player)
		if playersAmount == 0 {
			delete(rooms, roomID)
		}
	}
}
