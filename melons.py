import csv

class Melon:
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless
        
    def __repr__(self):
        """Show info about melon in console"""
        return(f"<Melon: {self.melon_id}, {self.common_name}")
    
    def price_str(self):
        """Returns formatted price as a string"""
        return f"${self.price:.2f}"


melon_dict = {}   

with open("melons.csv") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        melon_id = row['melon_id']
        melon = Melon(
            melon_id,
            row['common_name'],
            float(row['price']),
            row['image_url'],
            row['color'],
            eval(row['seedless']))
        melon_dict[melon_id] = melon
        
# print(melon_dict)

def get_melon_ids(id):
    """returns the full melon object in the melon dict"""
    return melon_dict.get(id)

def get_list():
    """return list of melons"""
    return list(melon_dict.values())

# print(get_melon_ids('cren'))
# print(get_list(melon_dict))