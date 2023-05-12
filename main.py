from options import Options
def main():
    me = Options()
    me.create_inventory("q.csv")
    me.create_inventory1("old.csv")
    me.create_inventory2("quotes.csv")
    #me.print_list()
    me.choice('q.csv','old.csv','q1.csv')
    #me.print_list()
    #print("Hello")
    #me.spectacular("q.csv", "old.csv", "q1.csv")
    
main()