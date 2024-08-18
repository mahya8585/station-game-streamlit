import streamlit as st
import numpy as np
import pandas as pd

# st.title('PyLadies Tokyo ハンズオン!')

# st.markdown('## こんにちは :wave:')
# st.markdown('### PyLadies Tokyoです')
# st.markdown('- *Streamlit* はドキュメントが **充実** しているので ***[ここ]()*** をみればだいたい使い方がわかります。')

'''
# PyLadies Tokyo ハンズオン!
## こんにちは :wave:
### PyLadies Tokyoです
- *Streamlit* はドキュメントが **充実** しているので ***[ここ]()*** をみればだいたい使い方がわかります。
'''

df = pd.DataFrame({
    'A列': [1, 2, 3, 4],
    'B列': [10, 20, 30, 40],
    'C列': [100, 200, 300, 400],
})

st.write('st.writeを使ったDataFrameの表示')
st.write(df)

st.write('st.dataframeを使ったDataFrameの表示')
st.dataframe(df.style.highlight_max(axis=0), width=500, height=200)

st.subheader("PyLadies Tokyo 参加者推移")

data = [
    [15,22,5],
    [5,15,12],
    [41,40,21],
    [19,13,0],
    [23,27,0],
    [17,21,7],
    [28,8,8],
    [6,8,13],
    [7,10,20],
    [35,20,18],
    [13,9,8],
    [21,4,32],
]
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
chart_data = pd.DataFrame(
    data,
    columns=['2015', '2020', '2023'],
    index=pd.CategoricalIndex(months, categories=months, ordered=True)
)

st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)


df = pd.DataFrame({'col1': [1,2,3]})
df  # これでdfの中身がページに表示される

st.image('https://media.connpass.com/thumbs/f2/a0/f2a0bf698aead324fa01be237529af58.png', caption='connpassから取得', use_column_width=True)