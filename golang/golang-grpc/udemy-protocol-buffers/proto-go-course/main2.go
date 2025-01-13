package main

import (
	"fmt"

	pb "example.com/m/proto"
)

func addPerson(person *pb.Person, personList []*pb.Person) []*pb.Person {
	// Append the new person to the list
	personList = append(personList, person)
	return personList
}

func main() {
	// Initialize personList
	var personList = []*pb.Person{}
	var person2 *pb.Person = &pb.Person{Name: "My name 2", Id: 2, Email: "2@example.com"}
	var person3 *pb.Person = &pb.Person{Name: "My name 3", Id: 3, Email: "3@example.com"}
	var person4 *pb.Person = &pb.Person{Name: "My name 4", Id: 4, Email: "4@example.com"}

	// Add person2 and person3 to the personList
	personList = addPerson(person2, personList)
	personList = addPerson(person3, personList)
	personList = addPerson(person4, personList)

	// Create an address book with the updated personList
	var address_book = &pb.AddressBook{
		People: personList,
	}

	// Print the address book
	fmt.Println(address_book)
}
