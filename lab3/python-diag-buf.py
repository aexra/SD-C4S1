import matplotlib.pyplot as plt
import numpy as np

# Определим задачи, их длительность и буферы
tasks = ['Анализ требований', 'Проектирование', 'Разработка', 'Тестирование', 'Документирование']
durations = [5, 20, 40, 15, 10] # Дни
buffers = [0, 2, 5, 3, 2]        # Буфер в днях (для некритических задач)

# Вычислим общую продолжительность с буферами
total_with_buffer = [d + b for d, b in zip(durations, buffers)]

fig, ax = plt.subplots(figsize=(12, 6))

y_pos = np.arange(len(tasks))

# Основная длительность задач
bars1 = ax.barh(y_pos, durations, color='steelblue', alpha=0.8, label='Основная длительность')

# Буферы задач
bars2 = ax.barh(y_pos, buffers, left=durations, color='lightcoral', alpha=0.8, label='Буфер')

ax.set_xlabel('Дни')
ax.set_ylabel('Задачи')
ax.set_title('Диаграмма буферов проекта')
ax.set_yticks(y_pos)
ax.set_yticklabels(tasks)
ax.legend()

# Добавим значения на диаграмме
for i, (dur, buf) in enumerate(zip(durations, buffers)):
    ax.text(dur/2, i, str(dur), ha='center', va='center', color='white', fontweight='bold')
    if buf > 0:
        ax.text(dur + buf/2, i, str(buf), ha='center', va='center', color='white', fontweight='bold')

ax.grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
