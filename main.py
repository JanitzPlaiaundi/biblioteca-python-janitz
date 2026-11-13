from view.view import View
from controllers.book_controller import BookController
from controllers.partner_controller import PartnerController

bookController = BookController()
partnerController = PartnerController()
view = View(bookController, partnerController)
view.execute()