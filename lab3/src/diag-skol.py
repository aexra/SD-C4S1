import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Определим фазы проекта и их изначальные/текущие даты
phases = ['Инициация', 'Планирование', 'Анализ и проектирование', 'Разработка', 'Тестирование', 'Документирование', 'Сдача проекта']

# Изначальные даты завершения
original_end_dates = [datetime(2025, 11, 25), datetime(2025, 12, 23), datetime(2026, 1, 22), datetime(2026, 3, 5), datetime(2026, 4, 16), datetime(2026, 4, 24), datetime(2026, 6, 10)]
# Текущие даты завершения
current_end_dates = [datetime(2025, 11, 25), datetime(2025, 12, 25), datetime(2026, 1, 25), datetime(2026, 3, 10), datetime(2026, 4, 20), datetime(2026, 4, 26), datetime(2026, 6, 15)]

# Преобразуем в дни
start_date = datetime(2025, 11, 1)
original_days = [(d - start_date).days for d in original_end_dates]
current_days = [(d - start_date).days for d in current_end_dates]

# Вычислим скольжение
slippage = [curr - orig for curr, orig in zip(current_days, original_days)]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Диаграмма скольжения
y_pos = np.arange(len(phases))
ax1.barh(y_pos, slippage, color=['red' if x > 0 else 'green' for x in slippage])
ax1.set_yticks(y_pos)
ax1.set_yticklabels(phases)
ax1.set_xlabel('Скольжение (дни)')
ax1.set_title('Диаграмма скольжения')
ax1.grid(axis='x', linestyle='--', alpha=0.6)

# Добавим значения на столбцах
for i, v in enumerate(slippage):
    ax1.text(v + (0.5 if v >= 0 else -0.5), i, str(v), va='center', ha='left' if v >= 0 else 'right')

# Сравнение изначальных и текущих дат
x = np.arange(len(phases))
width = 0.35

ax2.bar(x - width/2, original_days, width, label='Изначальная дата завершения', alpha=0.8)
ax2.bar(x + width/2, current_days, width, label='Текущая дата завершения', alpha=0.8)

ax2.set_xlabel('Фазы проекта')
ax2.set_ylabel('Дни с начала проекта')
ax2.set_title('Сравнение изначальных и текущих дат завершения')
ax2.set_xticks(x)
ax2.set_xticklabels(phases, rotation=45, ha='right')
ax2.legend()

plt.tight_layout()
plt.show()
