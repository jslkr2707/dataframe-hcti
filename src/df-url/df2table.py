import pandas as pd

import style

df = pd.read_csv('C:/Users/fred8/Documents/GitHub/df-url/src/df-url/test.csv')

class df2Table:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.col = df.columns.tolist()
        self.index = df.index.tolist()

    def setHeader(self):
        header = '<thead><tr><th></th>'
        for c in self.col:
            header += f'<th>{c}</th>'
        header += "</tr></thead>"
        return header
    
    def setBody(self):
        rows = len(self.index)
        body = '<tbody>'
        for i in range(rows):
            index = self.index[i]
            body += f'<tr><td>{index}</td>'
            for j in range(len(self.col)):
                value = self.df.iloc[i][self.col[j]]
                body += f'<td>{value}</td>'
            body += '</tr>'
        
        body += '</tbody>'
        return body

    def toHtml(self):
        result = "<table>" + self.setHeader() + self.setBody() + "</table>"
        return result
    

    

