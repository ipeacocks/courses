package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	// Open the file using os.Open (we'll read and seek multiple times)
	f, err := os.Open("/tmp/dat")
	check(err)
	defer f.Close() // Ensure file is closed when function exits

	// Read the entire file content into memory (if needed)
	dat, err := io.ReadAll(f) // io.ReadAll reads the entire content
	check(err)
	fmt.Print(string(dat)) // Print the entire content of the file

	// Read 5 bytes from the file
	b1 := make([]byte, 5)
	n1, err := f.Read(b1)
	check(err)
	fmt.Println(string(b1[:n1]))  // Print only the valid bytes
	fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))

	// Seek to the 6th byte and read 2 bytes
	o2, err := f.Seek(6, io.SeekStart)
	check(err)
	b2 := make([]byte, 2)
	n2, err := f.Read(b2)
	check(err)
	fmt.Printf("%d bytes @ %d: %s\n", n2, o2, string(b2[:n2]))

	// Seek 4 bytes ahead from the current position
	_, err = f.Seek(4, io.SeekCurrent)
	check(err)

	// Seek 10 bytes from the end of the file (check if the file is large enough first)
	_, err = f.Seek(-10, io.SeekEnd)
	check(err)

	// Seek to the 6th byte again and use io.ReadAtLeast to ensure we read at least 2 bytes
	o3, err := f.Seek(6, io.SeekStart)
	check(err)
	b3 := make([]byte, 2)
	n3, err := io.ReadAtLeast(f, b3, 2)
	check(err)
	fmt.Printf("%d bytes @ %d: %s\n", n3, o3, string(b3))

	// Seek to the start of the file to use bufio.Reader
	_, err = f.Seek(0, io.SeekStart)
	check(err)

	r4 := bufio.NewReader(f)
	b4, err := r4.Peek(5)
	check(err)
	fmt.Printf("5 bytes: %s\n", string(b4))
}