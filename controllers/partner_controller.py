from model.partner import Partner

class PartnerController:
    def __init__(self, partners = None):
        self.partners = partners

    def charge_partners(self):
        try:
            self.partners = []
            with open("data/partners.txt", "r",encoding="utf-8") as f:
                for line in f:
                    partner_info = line.strip().split("|")

                    if len(partner_info) > 4:
                        partner_book_codes = [code.strip() for code in partner_info[4].split(",") if code.strip()]
                        partner = Partner(int(partner_info[0]), partner_info[1], partner_info[2], int(partner_info[3]), partner_book_codes)
                    else:
                        partner = Partner(int(partner_info[0]), partner_info[1], partner_info[2], int(partner_info[3]))
                    self.partners.append(partner)
        except FileNotFoundError as e:
            print(e.strerror)

    def assign_book(self, book_id, partner_id):
        self.charge_partners()
        for partner in self.partners:
            if partner.code == partner_id:
                partner.books.append(book_id)
                return self.write_partners()

        return f"No se encontró un socio con el código {partner_id}."

    def return_book(self, book_id, partner_id):
        self.charge_partners()
        for partner in self.partners:
            if partner.code == partner_id:
                partner.books.remove(book_id)
                return self.write_partners()
        return f"No se encontró un socio con el código {partner_id}."

        

    def write_partners(self):
        with open("data/partners.txt", "w", encoding="utf-8") as f:
            for partner in self.partners:
                f.write(f"{str(partner.code)}|{partner.name}|{partner.email}|{str(partner.phone)}|{','.join(partner.books or [])}\n")
        return "Se han actualizado los socios con exito"

    def partners_with_book(self):
        self.charge_partners()
        partners_with_book = []
        for partner in self.partners:
            if partner.books:
                partners_with_book.append(partner)
        return partners_with_book

    def create_partner(self, name, email, phone):
        self.charge_partners()
        try:
            last_partner = self.partners[-1]
            code = last_partner.code + 1
            partner = Partner(code, name, email, phone)
            self.partners.append(partner)
            return self.write_partners()
        except Exception as e:
            return e