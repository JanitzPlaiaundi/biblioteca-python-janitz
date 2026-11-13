from model.partner import Partner

class PartnerController:
    def __init__(self, partners = None):
        self.partners = partners

    def load_partners(self):
        try:
            self.partners = []
            with open("data/partners.txt", "r",encoding="utf-8") as f:
                for line in f:
                    partner_info = line.strip().split("|")

                    if len(partner_info) > 4:
                        partner_book_codes = [int(code.strip()) for code in partner_info[4].split(",") if code.strip()]
                        partner = Partner(int(partner_info[0]), partner_info[1], partner_info[2], int(partner_info[3]), partner_book_codes)
                    else:
                        partner = Partner(int(partner_info[0]), partner_info[1], partner_info[2], int(partner_info[3]))
                    self.partners.append(partner)
                return "Socios cargados correctamente"
        except FileNotFoundError:
            raise

    def write_partners(self):
        with open("data/partners.txt", "w", encoding="utf-8") as f:
            for partner in self.partners:
                books_str = ",".join(str(book) for book in (partner.books or []))
                f.write(f"{str(partner.code)}|{partner.name}|{partner.email}|{str(partner.phone)}|{books_str}\n")
        return "Se han actualizado los socios con exito"
    
    def assign_book(self, book_id, partner_id):
        try:
            for partner in self.partners:
                if partner.code == partner_id:
                    partner.books.append(book_id)
        except:
            raise

    def return_book(self, book_id, partner_id):
        try:
            for partner in self.partners:
                if partner.code == partner_id:
                    partner.books.remove(book_id)
        except:
            raise

    def partners_with_book(self):
        partners_with_book = []
        for partner in self.partners:
            if partner.books:
                partners_with_book.append(partner)
        return partners_with_book

    def create_partner(self, name, email, phone):
        try:
            last_partner = self.partners[-1]
            code = last_partner.code + 1
            partner = Partner(code, name, email, phone)
            self.partners.append(partner)
        except:
            raise