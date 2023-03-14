

class AgreementRow:
    def __init__(self, manufacturerMatch:str, productMatch:str, categoryNameMatch:str,percentageDiscount:float):
        self.ManufacturerMatch = manufacturerMatch
        self.ProductMatch = productMatch
        self.CategoryNameMatch = categoryNameMatch
        self.PercentageDiscount = percentageDiscount

class Agreement:
    def __init__(self, email:str):
        self.Email = email
        self.AgreementRows = []


class CurrentUserContext:
    def __init__(self):
        self.Agreements = []
