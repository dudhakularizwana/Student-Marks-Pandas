import pandas as pd

data = {
    'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj', 'Ravi', 'Natasha', 'Riya'],
    'Age': [17, 17, 18, 17, 18, 17, 17],
    'Gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F'],
    'Marks': [90, 76, 'NaN', 74, 65, 'NaN', 71]
}

df = pd.DataFrame(data)

print(df)

c = avg = 0

for ele in df['Marks']:
    if str(ele).isnumeric():
        c += 1
        avg += ele

avg /= c

df = df.replace(
    to_replace="NaN",
    value=avg
)

print(df)

df['Gender'] = df['Gender'].map({
    'M': 2,
    'F': 1
}).astype(float)

print(df)

df = df[df['Marks'] >= 75].copy()

df.drop(
    columns=['Age'],
    errors='ignore',
    inplace=True
)

print(df)
