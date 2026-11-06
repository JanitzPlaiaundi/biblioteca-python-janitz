from model.partner import Partner

class PartnerController:
    def __init__(self, partners = []):
        self.partners = partners

    
    def charge_partners(self, charged_books):
        
        try:
            with open("data/partners.txt", "r",encoding="utf-8") as f:
                for line in f:
                    if(line == ""):
                        break
                    partner_info = line.split("|")
                    parter_book_codes = partner_info[4].split(",")

                    if len(parter_book_codes) > 0:
                        book_list = []
                    
                        for id in parter_book_codes:
                            for book in charged_books:
                                if book.code == id:
                                    book_list.append(book)
                        partner = Partner(partner_info[0], partner_info[1], partner_info[2], partner_info[3], book_list)
                    else:
                        partner = Partner(partner_info[0], partner_info[1], partner_info[2], partner_info[3])
                    self.partners.append(partner)
        except FileNotFoundError as e:
            print(e.strerror)