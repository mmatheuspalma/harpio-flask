class ComicParams:
    order   = "DESC"
    orderBy = "id"
    search  = ""

    def __init__(self, order, orderBy, search):
        if order:
            self.order   = order
        
        if orderBy:
            self.orderBy = orderBy

        self.search  = search