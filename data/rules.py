class Rules:
    
    def applyRules(self, cell_value, number_neighbours):
        if(cell_value == 0 and number_neighbours==3):
            return 1
        elif(cell_value == 1 and (number_neighbours < 2 or number_neighbours > 3)):
            return 0
        return cell_value