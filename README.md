# studying
Studying and learning 

1. Кредитный скоринг 

Перевод, разбор и комментари решения:
https://www.kaggle.com/kabure/predicting-credit-risk-model-pipeline/notebook
Благодарность автору: https://www.kaggle.com/kabure/code

Описание исследования:

Данное исследование позволяет увидеть интересные статистики и факты о кредитных рейтингах клиентов, зависимости размера, срока кредита от возраста клиента, пола, занимаемой должности, наличия собственности и т.д. Также исследования позволяет увидеть зависимость кредитного рейтинга и риска от различных показателей. Кроме того, исследование предназначено для предсказания кредитного рейтинга клиента. 

В первой части исследование приводятся некоторые интересные статистики. Все исследования представлены в виде графиков, гистограммы (Histogram), скрипичного графика (Violin), диаграммы размаха (Box plot).

На основании датасета были определены количество клиентов банка с хорошим и плохим кредитным рейтигом, распределение хороших и плохих кредитных рейтингов по возрастам в количественном соотношении и по плотности. Рассматривается распределение размера кредита по возрастным группам, занимамой должности. Распределение кредитного рейтинга в зависмости от жилищных условий клиентов. 

В результате исследования можно сделать следующие выводы:
- Имеется зависимость между наличием собственности и хорошим кредитным рейтингом. 
- Большая часть клиентов имеет хорошый кредитный рейтинг. 
- Клиенты в возрасте 26-27 лет берут кредиты чаще, чем представители других возрастных категорий. 
- Мужчины берут кредит чаще, чем женщины, независимо от кредитного рейтинга. 
- В то же время, в основном размер кредита, которые берут мужчины, больше размера кредитов, которые берут женщины. 
- Чаще всего берут кредиты представители профессии, отнесенные в категорию 2. 
- Однако размер кредита больше у представителей професии, входящию в категорию 3.
- Наиболее распространенный размер кредита находится в диапазоне $0-5000. 
- Клиенты с небольшим количеством средств на сберегательном счете берут кредиты чаще всего, также размер кредита у этой группы клиентов наибольший. - Больше всего кредитов берут с целью покупки машины или техники, меньше всего на домашние нужды и отпуск. 
- Самые большие кредиты берутся с целью отпуска или других трат. 
- Кредиты чаще всего берут на срок от 12 до 24 месяцев. 
- Чем больше размер кредита, тем на больший срок он берется. 

В другой части исследования, с целью предсказания кредитного рейтинга, автор сравнивает разные алгоритмы ML и создает модели. Первая модель использует Случайный лес, вторая модель использует модель Гаусса.
