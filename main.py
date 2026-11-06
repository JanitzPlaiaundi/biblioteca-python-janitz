from view.view import View
from controllers.BookController import BookController
from controllers.PartnerController import PartnerController

bookController = BookController()
partnerController = PartnerController()
view = View(bookController, partnerController)
view.menu()
