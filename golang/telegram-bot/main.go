package main

import (
	"fmt"
	"os"

	"github.com/mymmrac/telego"
	th "github.com/mymmrac/telego/telegohandler"
	tu "github.com/mymmrac/telego/telegoutil"
)

func main() {
	botToken := "my:token"

	bot, err := telego.NewBot(botToken, telego.WithDefaultDebugLogger())
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	updates, _ := bot.UpdatesViaLongPolling(nil)
	bh, _ := th.NewBotHandler(bot, updates)

	bh.Handle(func(bot *telego.Bot, update telego.Update) {
		// Handler of /start command
		chatID := tu.ID(update.Message.Chat.ID)
		keyboard := tu.Keyboard(
			tu.KeyboardRow(
				tu.KeyboardButton("Start"),
				tu.KeyboardButton("Help"),
				tu.KeyboardButton("Support"),
			),
			tu.KeyboardRow(
				tu.KeyboardButton("Send Location").WithRequestLocation(),
				tu.KeyboardButton("Send Contact").WithRequestContact(),
				tu.KeyboardButton("Cancel"),
			),
		)

		message := tu.Message(
			chatID,
			"Now keyboard will appear",
		).WithReplyMarkup(keyboard)

		// _, _ = bot.CopyMessage(
		// 	tu.CopyMessage(
		// 		chatID,
		// 		chatID,
		// 		update.Message.MessageID,
		// 	),
		// )

		_, _ = bot.SendSticker(
			tu.Sticker(
				chatID,
				tu.FileFromID("CAACAgIAAxkBAAENqkdnmsC5xQMQiDOj0v3S_7v7xnN4UwACEgADuDxkCPvWERlPuuDMNgQ"),
			),
		)
		_, _ = bot.SendMessage(message)
	}, th.CommandEqual("stop"))

	bh.Handle(func(bot *telego.Bot, update telego.Update) {
		// Handler of any message
		chatID := tu.ID(update.Message.Chat.ID)
		_, _ = bot.CopyMessage(
			tu.CopyMessage(
				chatID,
				chatID,
				update.Message.MessageID,
			),
		)
	}, th.AnyMessage())

	bh.Start()

	defer bh.Stop()
	defer bot.StopLongPolling()

	// for update := range updates {
	// 	if update.Message != nil {
	// 		chatID := tu.ID(update.Message.Chat.ID)
	// 		keyboard := tu.Keyboard(
	// 			tu.KeyboardRow(
	// 				tu.KeyboardButton("Start"),
	// 				tu.KeyboardButton("Help"),
	// 				tu.KeyboardButton("Support"),
	// 			),
	// 			tu.KeyboardRow(
	// 				tu.KeyboardButton("Send Location").WithRequestLocation(),
	// 				tu.KeyboardButton("Send Contact").WithRequestContact(),
	// 				tu.KeyboardButton("Cancel"),
	// 			),
	// 		)

	// 		message := tu.Message(
	// 			chatID,
	// 			"Now keyboard will appear",
	// 		).WithReplyMarkup(keyboard)

	// 		_, _ = bot.CopyMessage(
	// 			tu.CopyMessage(
	// 				chatID,
	// 				chatID,
	// 				update.Message.MessageID,
	// 			),
	// 		)

	// 		_, _ = bot.SendSticker(
	// 			tu.Sticker(
	// 				chatID,
	// 				tu.FileFromID("CAACAgIAAxkBAAENqkdnmsC5xQMQiDOj0v3S_7v7xnN4UwACEgADuDxkCPvWERlPuuDMNgQ"),
	// 			),
	// 		)
	// 		_, _ = bot.SendMessage(message)
	// 	}
	// }
}
