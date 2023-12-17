from options import Options
def main():
    options = Options()
    options.create_inventory("original.csv")
    options.create_inventory1("old.csv")
    options.create_inventory2("quotes.csv")
    options.choice('original.csv','old.csv','notUsed.csv')
main()