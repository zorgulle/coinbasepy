class Balance:
    def __init__(self, amount=None, currency=None):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

class Account:
    def __init__(self, id=None, name=None, primary=None, type=None, currency=None,
                 balance=None, created_at=None, updated_at=None, resource=None, resource_path=None,
                 ready=None):
        self.id = id
        self.name=name
        self.primary=primary
        self.type=type
        self.currency=currency
        self.balance=balance
        self.created_at=created_at
        self.updated_at=updated_at
        self.resource=resource
        self.resource_path=resource_path
        self.ready=ready

    def __eq__(self, __o: object) -> bool:
        return (self.id == __o.id
            and self.name==__o.name
            and self.primary==__o.primary
            and self.type==__o.type
            and self.currency==__o.currency
            and self.balance==__o.balance
            and self.created_at==__o.created_at
            and self.updated_at==__o.updated_at
            and self.resource==__o.resource
            and self.resource_path==__o.resource_path
            and self.ready==__o.ready)
