package context

import (
	"dev.sigpipe.me/dashie/myapp/models"
	"dev.sigpipe.me/dashie/myapp/models/errors"
	"gopkg.in/macaron.v1"
)

func AssignUser() macaron.Handler {
	return func(ctx *Context) {
		userName := ctx.Params("user")

		// Anonymous user doesn't really exists, that's nil
		if userName == "anonymous" {
			return
		}

		_, err := models.GetUserByName(userName)
		if err != nil {
			if errors.IsUserNotExist(err) {
				ctx.NotFound()
			} else {
				ctx.Handle(500, "GetUserByName", err)
			}
			return
		}
	}
}
