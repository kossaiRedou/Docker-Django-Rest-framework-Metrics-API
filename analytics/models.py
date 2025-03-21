import pandas as pd
import matplotlib.pyplot as plt
from django.db import models

class SalesData(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="datasets/")

    def load_data(self):
        return pd.read_csv(self.file.path)

    def get_top_products(self):
        df = self.load_data()
        return df.groupby('product')['sales'].sum().sort_values(ascending=False).to_dict()

    def plot_sales_trends(self):
        df = self.load_data()
        df['date'] = pd.to_datetime(df['date'])
        df_grouped = df.groupby('date')['sales'].sum()

        plt.figure(figsize=(8, 5))
        df_grouped.plot()
        plt.xlabel("Date")
        plt.ylabel("Total des ventes")
        plt.title("Tendance des ventes")
        plt.savefig(f"media/{self.name}_sales_trend.png")
