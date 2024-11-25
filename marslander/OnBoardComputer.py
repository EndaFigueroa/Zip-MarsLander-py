class OnBoardComputer:
    
    def get_next_burn(self, burn_interval,gas):
        if gas >=10200:
            burn=200
        else:
            if burn_interval%2!=0:
                burn=200
            else:
                burn=0
        # print(burn)  # hack!
        return burn
