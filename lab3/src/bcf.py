import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Определим временные рамки проекта
start_date = datetime(2025, 11, 1)
end_date = datetime(2026, 6, 10)
current_date = datetime(2026, 2, 15)

# Примерные даты для контрольных точек
milestones = ['Начало', 'Анализ завершен', 'Проектирование завершено', 'Разработка завершена', 'Тестирование завершено', 'Проект завершен']

# Базовый план (изначальные оценки)
baseline_dates = [
    start_date,
    start_date + timedelta(days=30),
    start_date + timedelta(days=60),
    start_date + timedelta(days=120),
    start_date + timedelta(days=180),
    end_date
]

# Текущее состояние (фактические/обновленные оценки)
current_dates = [
    start_date,
    start_date + timedelta(days=32),  # Небольшая задержка
    start_date + timedelta(days=65),  # Небольшая задержка
    start_date + timedelta(days=125), # Небольшая задержка
    start_date + timedelta(days=185), # Небольшая задержка
    start_date + timedelta(days=225)  # Прогнозируемая задержка
]

# Прогноз на будущее (с учетом текущих тенденций)
forecast_dates = [
    start_date,
    start_date + timedelta(days=32),
    start_date + timedelta(days=65),
    start_date + timedelta(days=128),  # Увеличенная задержка
    start_date + timedelta(days=190),  # Увеличенная задержка
    start_date + timedelta(days=235)  # Увеличенная задержка
]

# Преобразуем даты в числовые значения для графика
baseline_days = [(d - start_date).days for d in baseline_dates]
current_days = [(d - start_date).days for d in current_dates]
forecast_days = [(d - start_date).days for d in forecast_dates]

fig, ax = plt.subplots(figsize=(12, 8))

x = np.arange(len(milestones))

ax.plot(x, baseline_days, 'o-', label='Базовый план', linewidth=2, markersize=8)
ax.plot(x, current_days, 's-', label='Текущее состояние', linewidth=2, markersize=8)
ax.plot(x, forecast_days, '^-', label='Прогноз на будущее', linewidth=2, markersize=8)

ax.set_xlabel('Контрольные точки')
ax.set_ylabel('Дни с начала проекта')
ax.set_title('BCF-анализ: Базовый план - Текущее состояние - Прогноз на будущее')
ax.set_xticks(x)
ax.set_xticklabels(milestones, rotation=45, ha='right')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
