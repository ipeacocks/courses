package pointerplay_test

import (
	"pointerplay"
	"testing"
)

func TestDouble(t *testing.T) {
	t.Parallel()
	var x int = 12
	want := 24
	pointerplay.Double(&x)
	if want != x {
		t.Errorf("want %d, got %d", want, x)
	}
}
