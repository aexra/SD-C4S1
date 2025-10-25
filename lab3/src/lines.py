import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Определим гипотетические даты начала и текущую дату
start_date = datetime(2025, 11, 1)
current_date = datetime(2026, 2, 15)  # Примерно середина проекта

# Рассчитаем день проекта
project_day = (current_date - start_date).days

# Создадим примерные данные для линии исполнения
activities = ['Анализ', 'Проектирование', 'Разработка', 'Тестирование', 'Документирование', 'Сдача']
planned_completion = [15, 40, 65, 85, 95, 100]  # Процент выполнения по плану
actual_completion = [20, 45, 60, 30, 10, 5]     # Фактический процент выполнения

fig, ax = plt.subplots(figsize=(12, 6))
x = np.arange(len(activities))
width = 0.35

ax.bar(x - width/2, planned_completion, width, label='По плану', alpha=0.8)
ax.bar(x + width/2, actual_completion, width, label='Фактически', alpha=0.8)

ax.set_xlabel('Этапы проекта')
ax.set_ylabel('Процент выполнения (%)')
ax.set_title('Линия исполнения проекта')
ax.set_xticks(x)
ax.set_xticklabels(activities)
ax.legend()

# Добавим линии отклонения
for i in range(len(activities)):
    deviation = actual_completion[i] - planned_completion[i]
    ax.text(i, max(actual_completion[i], planned_completion[i]) + 2, 
            f'{deviation:+d}%', ha='center', va='bottom', 
            bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow' if deviation < 0 else 'lightgreen', alpha=0.7))

plt.tight_layout()
plt.show()
