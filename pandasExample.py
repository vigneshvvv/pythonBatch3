import pandas as pd

employees = {
    "Name": ["Vignesh", "Kumar", "Arun"],
    "Age": [25, 27, 30],
    "salary": [30000, 30000, 30000]
}

df = pd.DataFrame(employees)
df.to_excel("userDetails.xlsx", index=False)

df = pd.read_excel("userDetails.xlsx")
print(df)
print(df["Name"])

result = df[df["Age"] > 25]
print(result)

new_user = pd.DataFrame({
    "Name": ["Revanth"],
    "Age": [20],
    "salary": [35000]
})

df = pd.concat([df, new_user], ignore_index=True)

print(df)

names = df["Name"].tolist()
print(names)