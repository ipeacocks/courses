// https://tutorialedge.net/golang/consuming-restful-api-with-go

package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

func main() {
	response, err := http.Get("http://pokeapi.co/api/v2/pokedex/kanto/")

	if err != nil {
		fmt.Print(err.Error())
		os.Exit(1)
	}

	responseData, err := io.ReadAll(response.Body)
	if err != nil {
		log.Fatal(err)
	}
	// fmt.Println(string(responseData))

	// A struct to map our Pokemon's Species which includes it's name
	type PokemonSpecies struct {
		Name string `json:"name"`
	}

	// A Pokemon Struct to map every pokemon to.
	type Pokemon struct {
		EntryNo int            `json:"entry_number"`
		Species PokemonSpecies `json:"pokemon_species"`
	}

	// A Response struct to map the Entire Response
	type Response struct {
		Name    string    `json:"name"`
		Pokemon []Pokemon `json:"pokemon_entries"`
	}

	var responseObject Response
	json.Unmarshal(responseData, &responseObject)

	fmt.Println(responseObject.Name)
	fmt.Println(len(responseObject.Pokemon))

	for _, pokemon := range responseObject.Pokemon {
		fmt.Println(pokemon.Species.Name)
	}
}
