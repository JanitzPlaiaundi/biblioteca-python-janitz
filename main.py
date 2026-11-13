from view.view import View
from controllers.book_controller import BookController
from controllers.partner_controller import PartnerController

book_controller = BookController()
partner_controller = PartnerController()
view = View(book_controller, partner_controller)
view.execute()