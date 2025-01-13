package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"

	pb "example.com/m/proto"
	"google.golang.org/protobuf/proto"
)

func main() {
	// p := pb.Person{
	// 	Id:    1234,
	// 	Name:  "John Doe",
	// 	Email: "jdoe@example.com",
	// 	Phones: []*pb.Person_PhoneNumber{
	// 		{Number: "555-4321", Type: pb.PhoneType_PHONE_TYPE_HOME},
	// 	},
	// }
	// fmt.Println(p)

	book := &pb.AddressBook{People: []*pb.Person{
		{
			Name:  "Jack Buck",
			Id:    301,
			Email: "buck@example.com",
			Phones: []*pb.Person_PhoneNumber{
				{Number: "555-555-0000", Type: pb.PhoneType_PHONE_TYPE_MOBILE},
				{Number: "555-555-0001", Type: pb.PhoneType_PHONE_TYPE_HOME},
				{Number: "555-555-0002", Type: pb.PhoneType_PHONE_TYPE_WORK},
			},
		}}}

	fname := os.Args[1]

	// Write the new address book back to disk.
	// out, err := proto.Marshal(book)
	// if err != nil {
	// 	log.Fatalln("Failed to encode address book:", err)
	// }
	// if err := ioutil.WriteFile(fname, out, 0644); err != nil {
	// 	log.Fatalln("Failed to write address book:", err)
	// }

	// Read the existing address book.
	in, err := ioutil.ReadFile(fname)
	if err != nil {
		log.Fatalln("Error reading file:", err)
	}
	if err := proto.Unmarshal(in, book); err != nil {
		log.Fatalln("Failed to parse address book:", err)
	}
	fmt.Println(book)
}
