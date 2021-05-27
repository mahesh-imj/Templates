def __openShpfile(self):
        """
        Open a shapefile and read in the contents, pop up the attribute menu 
        with the attributes of the shapefile
        """   
        print "open shape file!"
        directory="C:/Users/sjha1/Documents/GitHub/Simulator_GUI/Python-Sample/data/states/48States.shp"
        #tkFileDialog.askopenfilename(filetypes=[("SHAPE_FILE","*.shp")])
        print directory
        
        if directory == "":
            return
        
        self.shapes, self.shp_type, self.bbox = shp_reader.read_shp(directory)
        #read corresponding dbf data
        dbfFile = dbf.DbfLoader(directory[:-3] + "dbf")
        
        t = dbfFile.table2list()
        varNames = dbfFile.get_field_names()
        variables = {}
        for variable in varNames:
            variables[variable] = [record[varNames.index(variable)] for record in t]
            
        if self.dbfdata!=None:
            self.attibmenu.delete(0, len(self.dbfdata)-1)
            
        #add attributes into menu
        for key in variables.keys():
            self.__addAttribute(key)
        
        self.dbfdata = variables
        self.menubar.entryconfig(2, state=Tkconstants.NORMAL)
        self.__updateCanvas("STATE_NAME")
