from df2table import df2Table
import style
import imageurl

import pandas as pd

# code example

dataframe = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6]], columns = ['a', 'b', 'c']
)

HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
HCTI_API_USER_ID = 'your id'
HCTI_API_KEY = 'your key'

tbl = df2Table(dataframe)
html_code = tbl.toHtml()
css_code = style.generalStyle(["table, th, tr, td"], {"border": "2px solid black", "text-align": "center"})

hcti = imageurl.export(HCTI_API_ENDPOINT, HCTI_API_USER_ID, HCTI_API_KEY, html_code, css_code)
print(hcti)