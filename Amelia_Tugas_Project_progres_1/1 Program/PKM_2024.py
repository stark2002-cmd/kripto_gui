# Import pustaka yang diperlukan
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Membuat Dataset Sederhana
data = {
    'nilai_ujian': [65, 70, 50, 40, 85, 78, 55, 45, 90, 80],
    'kehadiran': [80, 85, 60, 50, 95, 88, 70, 60, 98, 92],
    'waktu_belajar': [3, 4, 2, 1, 5, 4, 2, 1, 5, 4],
    'label_kesulitan': [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
}
df = pd.DataFrame(data)

# 2. Memisahkan Fitur dan Label
X = df[['nilai_ujian', 'kehadiran', 'waktu_belajar']]
y = df['label_kesulitan']

# 3. Split Data menjadi Training dan Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Membuat dan Melatih Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 5. Prediksi dan Evaluasi Model
y_pred = model.predict(X_test)
print("Akurasi:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 6. Visualisasi Data
sns.scatterplot(x='nilai_ujian', y='kehadiran', hue='label_kesulitan', data=df)
plt.xlabel("Nilai Ujian")
plt.ylabel("Kehadiran")
plt.title("Visualisasi Data Kesulitan Belajar")
plt.show()
