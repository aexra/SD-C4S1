import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Определим контрольные точки и их планируемые даты
milestones = ['Начало проекта', 'Завершение анализа', 'Завершение проектирования', 'Завершение разработки', 'Завершение тестирования', 'Завершение проекта']
planned_dates = [datetime(2025, 11, 1), datetime(2025, 12, 15), datetime(2026, 1, 30), datetime(2026, 3, 15), datetime(2026, 4, 30), datetime(2026, 6, 10)]

# Текущие оценки дат (с учетом прогресса)
current_estimates = [datetime(2025, 11, 1), datetime(2025, 12, 18), datetime(2026, 2, 5), datetime(2026, 3, 25), datetime(2026, 5, 10), datetime(2026, 6, 20)]

# Преобразуем в дни для графика
start_date = datetime(2025, 11, 1)
planned_days = [(d - start_date).days for d in planned_dates]
current_days = [(d - start_date).days for d in current_estimates]

fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(milestones))
width = 0.35

bars1 = ax.bar(x - width/2, planned_days, width, label='Планируемая дата', alpha=0.8)
bars2 = ax.bar(x + width/2, current_days, width, label='Текущая оценка', alpha=0.8)

ax.set_xlabel('Контрольные события')
ax.set_ylabel('Дни с начала проекта')
ax.set_title('Диаграмма прогнозирования контрольных событий')
ax.set_xticks(x)
ax.set_xticklabels(milestones, rotation=45, ha='right')
ax.legend()

# Добавим подписи с датами
for i, (planned, current) in enumerate(zip(planned_days, current_days)):
    ax.text(i - width/2, planned + 2, f'{planned_dates[i].strftime("%d.%m.%y")}', 
            ha='center', va='bottom', rotation=90)
    ax.text(i + width/2, current + 2, f'{current_estimates[i].strftime("%d.%m.%y")}', 
            ha='center', va='bottom', rotation=90)

plt.tight_layout()
plt.show()
